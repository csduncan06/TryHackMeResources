# TryHackMe ~ IOS Forensics
[Link to the THM room](https://tryhackme.com/room/iosforensics)

**Task 2 -** What is Digital Forensics and how is it Used Today?

- ***Question 1***. What would look more suspicious? **an empty hard drive** or **a full hard drive**?
<br>*Answer **:** an empty hard drive*

- ***Question 2***. What is the definition for an abstract view of a hard drive?
<br>*Answer **:** image*

<br>**Task 6 -** Data Acquisition & Trust Certificates

- ***Question 1***. What is the name of a forensics tool that couldn't be used in a court of law, because data could be written to the device being analysed?
<br>*Answer **:** iFunbox* 

- ***Question 2***. You've found an iPhone with no passcode lock, what acquisition method would you use?
<br>*Answer **:** direct Acquisition*

- ***Question 3***. What is the name of the certificate that gets stored on a computer when it becomes trusted?
<br>*Answer **:** trust certificate*

**Task 9 -** 9. Scenario: Operation JustEncase (Deploy)
*access the machine via attackbox or RDP (if connected to THM vpn)*

- ***Question 1***. Who was the recepient of the SMS message sent on 23rd of August 2020?

  - Step 1 : Open `DB Browser (SQLite)` on the desktop <br>
![step1](img/img1.png)
  - Step 2 : Select the `Open Database` option <br>
![step2](img/img2.png)
  - Step 2. Navigate to the directory`C:\Users\cmnatic\Desktop\OpJustEncase\var\mobile\Library\SMS` and open `sms.db` <br>
![step3](img/img3.png)
  - Step 3. Select `Browse Data` just below the `Open Database` button and change the `Table` to `message` <br>
![step4](img/img4.png)
  - Step 4: In the row named date, we can see the date we are looking for (23rd of August 2020,) navigate to the recipient 
<br>*Answer **:** Lewis Randall* 

- ***Question 2***. What did the SMS message say?
This can be found by scrolling along the data in the same column, row name `text`
<br>*Answer **:** Did you get the goods?* 

- ***Question 3***. Looking at the address book, what is the first name of the other person in the contacts?
Repeat the steps from Question 1. This time open the database `C:\Users\cmnatic\Desktop\OpJustEncase\var\mobile\Library\AddressBook\AddressBook.sqlitedb` 
and table `ABPerson`. Make sure in file manager you change `SQLite database files` to `All files` 
<br>*Answer **:** jenny?* 

- ***Question 4***. Following on from Question #3, what is their listed "Organization"
<br>*Answer **:** transportation* 

- ***Question 5***. Investigate their browsing history, what is the address of the website that they have bookmarked?
Step 1. Open the database `C:\Users\cmnatic\Desktop\OpJustEncase\var\mobile\Library\Safari\Bookmarks.db`
Step 2. Select `Browse Data` and change the `Table` to `bookmarks`
Here we can see the websites the device owner has bookmarked
<br>*Answer **:** https://blog.cmnatic.co.uk* 

- ***Question 6***. The suspected received an email, what is the  **remote_id**  of the sender?
Step 1. This time Open `OpJustEncase` folder on the desktop, navigate to the directory `C:\Users\cmnatic\Desktop\OpJustEncase\var\mobile\Library\Mail` and drag the file named `Envelope Index` to the `Browse Data` tab in `SQLite`.
Step 2. Change `Table` to messages.
Here we can see the **remote_id** of the sender
<br>*Answer **:** 51.32.56.12* 

- ***Question 7***. What is the name of the company on one of the images stored on the suspects phone?
Using file explorer we can find the name images on the device. Navigate to the directory `C:\Users\cmnatic\Desktop\OpJustEncase\var\mobile\Media\DCIM\DCIM` and we can see the file names of the images
<br>*Answer **:** Tryhackme* 

- ***Question 8***. What is the value of the cookie that was left behind?
Using Notepad++ open the file `C:\Users\cmnatic\Desktop\OpJustEncase\var\mobile\Library\Cookies\com.apple.itunesstored.plist`
<br>*Answer **:** THM{COOKIES!!!}* 
