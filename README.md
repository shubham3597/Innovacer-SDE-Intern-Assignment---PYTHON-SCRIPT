# Innovacer-SDE-Intern-Assignment---PYTHON-SCRIPT

As per the Problem Statement mentioned here (http://innovaccer.com/hackercamp), I have succesfully implemented a bug free and totally working 
python script which requires email address and list of favourite TV series for multiple users as input.

It records the input EMAIL ID and SHOW RESPONSE and store it in the `email_responses` table of the database. <br />
Our MySQL Database is hosted on the GEARHOST Server and following are the credentials of the Database 
accession(Kindly use PHP MyAdmin or MySQL Workbench to suffice the need)<br />

    host = "den1.mysql6.gear.host"<br />
    user ="innovaccersde"<br />
    passwd = "Vr99w8w?~8Su"<br />
    database = "innovaccersde"<br />

Also a single email is being sent to the input email address with all the
appropriate response for every TV series. The content of the mail could
depend on the following use cases:
1. Exact date is mentioned for next episode.
2. Only year is mentioned for next season.
3. All the seasons are finished and no further details are available.
