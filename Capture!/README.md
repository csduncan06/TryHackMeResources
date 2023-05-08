# <p align="center">Capture! Brute Force Attack</p>

<p align="center">
Exploit code that can be executed on the THM box <a href="https://tryhackme.com/room/capture">Capture!</a>
</p>

## Description
This is a Python script that brute forces a login to the tryhackme Capture box with a given list of username and passwords. It includes the ability to automatically solve the Captcha if it is detected as active on the login page. 

## How it works
It takes two input files: a list of usernames (usernames.txt) and a list of passwords (passwords.txt).

The script starts by sending a POST request to the login page with a username and a dummy password (comingsoon) as the initial payload. If the server returns the message "does not exist", this tells us that the username is not valid and cycles onto the next username.
If the websites HTML response does not contain the message "does not exist", we can tell the username is a valid account on the website and then proceeds to brute force the password of the specific account by sending POST requests with different passwords within the given list. 


The login page will get protected by a CAPTCHA if a few login attempts have been failed. IF the CAPTCHA is detected by using the CAPTCHA Signature, the script extracs the question from the HTML source and solves the mathematical equation and then updates the POST web request payload to include the CAPTCHA solution.



