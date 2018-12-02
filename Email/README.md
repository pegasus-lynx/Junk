#Email Scripts :
The basic purpose of this script is to get the data of a group of emails from GMail.

The script uses the following modules:
- imaplib
    - This module is used for making connection, logging in.
    - It has also been used for selecting the folder, and searching for emails.
- email
    - This module has been used to create a message object for the email.
- csv
    - This module is used for reading and writing data in the csv file.

###Logging In[Imp]:
    Due to security constraint, Gmail does not allow the script to directly access the email.
    You need to generate an app password for getting access to the mails.
    Follow the link to generate password. []
    