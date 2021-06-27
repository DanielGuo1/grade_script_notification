[![Python](https://img.shields.io/badge/Build-Python3.x-blue.svg?style=flat-square&logo=Python&logoColor=white)](https://www.python.org/) 
[![Selenium](https://img.shields.io/badge/Selenium-3.141.0-green.svg?style=flat-square&logo=Selenium&logoColor=white)](https://www.selenium.dev/) 

<h1 align="center">Automatic grade notification</h1>
<p align="center">
  <a> 
    <img src="https://github.com/DanielGuo1/grade_script_notification/blob/main/images/graduation.jpeg" alt="Logo" width="550" height="300">
  </a>
  <p align="center">
    This script informs me whenever my university grades are online
  </p>
</p>


## About The Project
At my university (Hochschule Reutlingen) after you have completed your exam or submitted a paper or thesis, you will not receive a response if your grade is online. So there is no official timeframe in which the grades should be online, and neither is the professor obliged to let you know.

Nervously waiting and checking your grades every 5 minutes isn't the best thing to do on your vacation.

So I wrote a Python script that uses the Selenium framework to search my university's website. I deployed this script on my home server using a Raspberry Pi to trigger this script every x hours between 7:00 a.m. and 9:00 p.m.
As soon as the grad is online, I'll receive an email.

### Built With

* [Python](https://www.python.org/)
* [Selenium](https://www.selenium.dev/)

<!-- GETTING STARTED -->
## Getting Started

If you want to run this code locally, get a copy and follow these simple steps.

### Prerequisites

You need to download python and selenium in order to run the script [Download Python here](https://www.python.org/downloads/).

   
### Selenium Installation

1. Open your Chrome Browser 
2. Click on the three dots (top right) to expand the settings
3. Help -> About Google Chrome
4. Note the Version (89.0..., 90.0..., 91.0...)
5. Visit the [Selenium WebDriver website](https://sites.google.com/a/chromium.org/chromedriver/downloads)
6. Download the zip-Archive
7. Put the `chromedriver.exe` from the zip-Archive in the same folder after downloading the project (further down) – alternatively you can:
  * put it into `C:\Windows` straight away or if you're experiencing issues
  * put it somewhere else, but you should make sure the folder is in your %PATH%-variable
8. If you configured this step improperly, the bot will fail with this error - or a similar one
   `selenium.common.exceptions.WebDriverException: Message: 'chromedriver.exe' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home`
   OR `WebDriverException: unknown error: cannot find Chrome binary error with Selenium in Python for older versions of Google Chrome`
   
### Installation

1. Clone the repo
 ```sh
 git clone https://github.com/DanielGuo1/grade_script_notification.git
 ```
2. Put your University login credentials in `grade_script.py`:
```python
driver.find_element_by_id('asdf').send_keys('USERNAME')
driver.find_element_by_id('fdsa').send_keys('PASSWORD')
```
3. Enter your Gmail account credentials in `grade_script.py`:
```python
self.sender_address = "EMAIL_ADDRESS"
self.receiver_address = "EMAIL_ADDRESS"
self.account_password = "GMAIL_PASSWORD"
```
4. Run `grade_script.py`:
```python
python3 grade_script.py
```
