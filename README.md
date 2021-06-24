# Automatic grade notification
This script informs me whenever my university grades are online. 

## Reason of doing this:
After you have completed your exam or submitted a paper or thesis, you will not receive a response if your grade is online. So there is no official timeframe in which the grades should be online, and neither is the professor obliged to let you know.

Nervously waiting and checking your grades every 5 minutes isn't the best thing to do on your vacation.

So I wrote a Python script that uses the Selenium framework to search my university's website. I deployed this script on my home server using a Raspberry Pi to trigger this script every x hours between 7:00 a.m. and 9:00 p.m.
As soon as the grad is online, I'll receive an email.

