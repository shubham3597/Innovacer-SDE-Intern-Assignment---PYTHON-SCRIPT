# REGEX IMPORTING FOR EMAIL VALIDATION
import re

# import the smtplib module for Drafting & Sending Emails
import smtplib

# importing MYSQL CONNECTOR for database connectivity
import mysql.connector

import time
import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("<-------------------SUMMER INTERN HIRING CHALLENGE------------------>", "\n")
print("<---------------------------INNOVACCER------------------------------->", "\n")
print("<-----------------------SDE INTERN ASSIGNMENT------------------------>", "\n")
print("WELCOME TO PYTHONFLIX - ALL THE SOLUTION TO LATEST TV SERIES WILL BE FOUND HERE", "\n")


# PLEASE DO NOT FORGET TO INITIALSE THE FOLLOWING VARIABLES WITH YOUR DESIRED CREDENTIALS SO AS TO BE THE SENDER OF THE EMAIL
# ALSO THE SERVER IS USING GMAIL SMTP CLIENT THEREFORE, PLEASE TURN ON THE ACCESS TO LESS SECURE APPS UNDER YOUR GMAIL ACCOUNT SETTINGS
MY_ADDRESS = 'YOUR_GMAIL_ID'
PASSWORD = 'YOUR_PASSWORD'

db = mysql.connector.connect(
    host = "den1.mysql6.gear.host",
    user ="innovaccersde",
    passwd = "Vr99w8w?~8Su",
    database = "innovaccersde"
)
print("Connection Established with MySQL", db._host, "Server", "\n")

dbCursor = db.cursor()

## EMAIL REGEGX verifies if the user has entered a valid email or not
EMAIL_REGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")

def main():

    # Takes the EmailID Input from User
    emailId = input ('Please Enter your Email: \n')

    # EMAIL ID Check
    if not EMAIL_REGEX.match(emailId):
        print('Wrong Input, please try again!')
        
    else:
        print ('\n')
        print('Hello', emailId)
        print ('\n')

        # Takes the TV Series Input from User Separated by Commas
        tvSeries = input("Enter the TV series separated by commas: ")

        tvSeriesSplit = tvSeries.split(',')
        tvSeriesList = [str(item.strip()).upper() for item in tvSeriesSplit]
        # print('List of TV Series', tvSeriesList)
        print ('\n')

        rowCount = 0
        # adding the message to the message template
        message = ''

        for item in tvSeriesList:

            query = "SELECT * FROM TV_SERIES where TV_SERIES_NAME = %s" 

            dbCursor.execute(query, (str(item).upper(), ))

            dbResult = dbCursor.fetchall()

            #print(dbResult)
            if(len(dbResult) == 0):
                print("No Results Found for ", str(item).upper()," in the database." , "\n")

            else:
                for row in dbResult:
                    
                    print((rowCount + 1) ,row[0])
                    message += str((rowCount + 1)) + ". " +  str(row[0]) + " \n"
                    if(row[1] == 1):
                        print("NEXT EPISODE WILL AIR ON: ", row[2], "\n")
                        message += str("    NEXT EPISODE WILL AIR ON: ") + str(row[2]) + str("\n") + str("\n")
                    elif(row[1] == 0 and row[3] == 1):
                        print("NEXT SEASON SHALL BE AVAILABLE FROM: ", row[4].strftime("%Y"), "ONWARDS \n")
                        message += str("    NEXT SEASON SHALL BE AVAILABLE FROM: ") + str(row[4].strftime("%Y")) + str(" ONWARDS \n") + str("\n")
                    elif(row[5] == 1):
                        print("THIS SHOW HAS FINISHED STREAMING CONTENT\n")
                        message += str("    THIS SHOW HAS FINISHED STREAMING CONTENT\n") + str("\n")
                    rowCount = rowCount + 1

        if(rowCount != 0):
            # Prints out the message body for our sake
            print('The Following Data is being sent to', emailId,'...', '\n')
            print(message)

            smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)
            smtp.starttls()
            smtp.login(MY_ADDRESS, PASSWORD)

            # create a message
            msg = MIMEMultipart()       

            # setup the parameters of the message
            msg['From']='ADMIN'
            msg['To']=emailId
            msg['Subject']="INFO FROM PYTHONFLIX"

            # add in the message body
            msg.attach(MIMEText(message, 'plain'))

            # send the message via the server set up earlier.
            smtp.send_message(msg)
            del msg
            print('Please Check your Inbox!', "\n")

            # Terminate the SMTP session and close the connection
            smtp.quit()

            print("<----------------CODE SUBMITTED BY--------------------->", "\n")
            print("<------------------SHUBHAM SINGH----------------------->", "\n")
            print("<---------------------NSIT----------------------------->", "\n")

if __name__ == '__main__':
    main()