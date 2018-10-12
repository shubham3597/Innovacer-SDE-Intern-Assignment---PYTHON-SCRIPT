# Innovacer-SDE-Intern-Assignment---PYTHON-SCRIPT

As per the Problem Statement mentioned here (http://innovaccer.com/hackercamp), I have succesfully implemented a bug free and totally working 
python script which requires email address and list of favourite TV series for multiple users as input.

It records the input EMAIL ID and SHOW RESPONSE and store it in the `email_responses` table of the database. <br />
Our MySQL Database is hosted on the GEARHOST Server and following are the credentials of the Database 
accession(Kindly use `PHP MyAdmin` or `MySQL Workbench` to suffice the need)<br />

    host = "den1.mysql6.gear.host"
    user ="innovaccersde"
    passwd = "Vr99w8w?~8Su"
    database = "innovaccersde"

Also a single email is being sent to the input email address with all the
appropriate response for every TV series. It fetches the content right away from the `tv_series` table and the content of the mail could
depend on the following use cases:
1. Exact date is mentioned for next episode.
2. Only year is mentioned for next season.
3. All the seasons are finished and no further details are available.

The data in the database can be subject to change and was being pushed only for testimonial and development purposes, presently I have 3 Major tv shows and those are:
1. Game of Thrones
2. Friends
3. Narcos

This script also handles the errors, validations and no response cases as well. It is being written in a well structured and properly formatted manner

<h1>For Development Purposes</h1>

<b> PLEASE DO NOT FORGET TO INITIALSE THE `MY_ADDRESS = 'YOUR_GMAIL_ID'` & `PASSWORD = 'YOUR_PASSWORD'` ON LINE 24 & 25 RESPECTIVELY WITH YOUR DESIRED CREDENTIALS SO AS TO BE THE SENDER OF THE EMAIL</b>

<b>ALSO THE SERVER IS USING GMAIL SMTP CLIENT THEREFORE, PLEASE TURN ON THE ACCESS TO LESS SECURE APPS UNDER YOUR GMAIL ACCOUNT SETTINGS.</b>

If you want to work with your `localDB` kindly import the `innovacer.sql` database into your system and accordingly change your settings from `line 27-31`


