""" Sends you an email when your grade is online.

This script scrapes the website of Reutlingen-University and checks if the master thesis grade is
listed. If so, you get a notification via email.
"""
import sys
from datetime import datetime
import smtplib
import logging

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("headless")
options.add_argument("disable-gpu")


class CheckGrade:
    """ This class contains two methods.

    open_website
        Opens the university website and navigates to the grades table.
    send_mail:
        Depedning whether the grade is online, the user will get an email.
    """
    def __init__(self):
        self.no_exceptions = True
        self.exception_text = None
        self.subject = None
        self.text = None
        self.message = None
        self.sender_address = None
        self.receiver_address = None
        self.account_password = None

    def open_website(self):
        """ Traverse to all necessary webpages to see whether grade is online.

        After accessing every new page, there is a short break to wait until website
        and all elements are fully loaded.
        """
        logging.basicConfig(level=logging.INFO, filename=str(datetime.now)+'.log')

        # Start Browser and open University Website
        driver = webdriver.Chrome(executable_path='chromedriver', options=options)
        try:
            driver.get('https://hip.reutlingen-university.de/qisserver/rds?state=user&type=0')
        except NoSuchElementException:
            self.no_exceptions = False
            self.exception_text = "Login Page not found"
            logging.error(self.exception_text)

        # Login Mask
        try:
            driver.find_element_by_id('asdf').send_keys('USERNAME')
            driver.find_element_by_id('fdsa').send_keys('PASSWORD')
            driver.find_element_by_id('loginForm:login').click()
        except NoSuchElementException:
            self.no_exceptions = False
            self.exception_text = "Login failed"
            logging.error(self.exception_text)

        driver.implicitly_wait(2)

        # Prüfungsverwaltungs Page
        try:
            driver.get('https://hip.reutlingen-university.de/qisserver/'
                       'rds?state=change&type=1&moduleParameter=studyPOSMenu'
                       '&nextdir=change&next=menu.vm&subdir=applications&'
                       'xml=menu&purge=y&navigationPosition=functions%'
                       '2CstudyPOSMenu&breadcrumb=studyPOSMenu&topitem='
                       'functions&subitem=studyPOSMenu')
        except NoSuchElementException:
            self.no_exceptions = False
            self.exception_text = "Prüfungsverwaltungs Page not found"
            logging.error(self.exception_text)

        driver.implicitly_wait(2)

        # Notenspiegel Page
        try:
            driver.find_element_by_xpath('//*[@id="wrapper"]/div[7]/div[2]/div/'
                                         'form/div/ul/li[3]/a').click()
        except NoSuchElementException:
            self.no_exceptions = False
            self.exception_text = "Notenspiegel Page not found"
            logging.error(self.exception_text)

        driver.implicitly_wait(2)

        # Bachelor/Master Button
        try:
            driver.find_element_by_xpath('//*[@id="wrapper"]/div[7]/div[2]/form/ul/li/a[1]').click()
        except NoSuchElementException:
            self.no_exceptions = False
            self.exception_text = "Bachelor/Master Button not found"
            logging.error(self.exception_text)

        driver.implicitly_wait(2)

        # "Your Major" Button
        try:
            driver.find_element_by_xpath('/html/body/div/div[7]/div[2]/'
                                         'form/ul/li/ul/li/a[1]').click()
        except NoSuchElementException:
            self.no_exceptions = False
            self.exception_text = "Computer Science Button not found"
            logging.error(self.exception_text)

        driver.implicitly_wait(2)

        # List of all Grades
        try:
            rows = driver.find_elements_by_xpath('//*[@id="wrapper"]/div[7]/div[2]'
                                                 '/form/table[2]/tbody/tr')
        except NoSuchElementException:
            self.no_exceptions = False
            self.exception_text = "Table of grades not found"
            logging.error(self.exception_text)

        # check for new entries
        number_of_rows_without_thesis = 75

        if len(rows) > number_of_rows_without_thesis:
            self.send_mail(True)
        else:
            self.send_mail(False)

        driver.close()
        logging.info("Close")

    def send_mail(self, is_grade_online):
        """ Sends a mail if script fails or if grade is online

        You will either get an email that a certain webpage could not be found or if the grade
        is online.
        """
        if not self.no_exceptions:
            self.text = self.exception_text
            self.subject = "ERROR"

        elif is_grade_online:
            self.text = 'Please check your grade. It is online!!!'
            self.subject = "Grade is online!"

        else:
            sys.exit()

        self.message = f"Subject: {self.subject}\n\n{self.text}"
        self.sender_address = "EMAIL_ADDRESS"
        self.receiver_address = "EMAIL_ADDRESS"
        self.account_password = "GMAIL_PASSWORD"

        smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # Endpoint for the SMTP Gmail server
        smtp_server.login(self.sender_address, self.account_password)
        smtp_server.sendmail(self.sender_address, self.receiver_address, self.message)
        smtp_server.close()


checker = CheckGrade()
checker.open_website()
