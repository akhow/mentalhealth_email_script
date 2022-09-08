# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")
TodayDate = d1.split("/")

link = "https://www.roblox.com/games/9326398826/MentalCheck"

therapists = {
    "Karl Eriksen": "akhowe@email.wm.edu",
    "Janice Wang": "akhowe@email.wm.edu",
    "Stephen Steelberg": "akhowe@email.wm.edu",
    "Luisa Buendia": "akhowe@email.wm.edu",
    "Dianne Felton": "akhowe@email.wm.edu",
    "Haruki Nakamura": "akhowe@email.wm.edu",
    "Lisa Fu": "akhowe@email.wm.edu",
    "Claire Hunt": "akhowe@email.wm.edu",
    "Jakobi Bryant": "akhowe@email.wm.edu",
    "Jessica Blankenship": "akhowe@email.wm.edu",
    "Ai Run Man": "akhowe@email.wm.edu",
    "Kim Johnson": "akhowe@email.wm.edu",
    "Moses McGee": "akhowe@email.wm.edu",
    "Janice Lee": "akhowe@email.wm.edu",
    "Mac Donaldson": "akhowe@email.wm.edu",
    "Thomas Scott": "akhowe@email.wm.edu",
    "Jesus Gonzalez": "akhowe@email.wm.edu"
}

genLoc = "Office"
genTherapist = "Jakobi Bryant"

sender = "WMMentalCheck@gmail.com"

smtp_server_name = 'smtp.gmail.com'
port = '587' # for normal messages
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls() # this is for secure reason
server.login(sender, "CSCI417E")

#ALEX: Make sure to change the directory to something that works for you
f = open("Data.csv", 'r')
next(f)
for x in f:
    answers = x.split(',')
    recipient = answers[1]
    
    if(answers[2] == "Regular"):
        therapyType = answers[3]
        location = answers[4]
        for i in range(5,16):
            if answers[i] != '':
                therapist = answers[i]
                if therapist == 'Any':
                    therapist = genTherapist #change to more random method

    elif(answers[2] == "Expedited"):
        therapyType = "General"
        location = genLoc #change to more random method
        therapist = genTherapist #change to more random method
    
    therapyDate = answers[16]
    therapyTime = answers[17].rstrip()
    
    ScheduledDate = therapyDate.split("/")
    #print(int(ScheduledDate[1])-int(TodayDate[0]))
    #So this section sets reminder emails!
    if(therapist in therapists):
        if((int(ScheduledDate[2])==int(TodayDate[2])) and (int(ScheduledDate[0])==int(TodayDate[1]))):
            if(int(ScheduledDate[1])-int(TodayDate[0])==-1):
                text = "Greetings,\nyou have a " + therapyType + " Counseling session with " + therapist + " in our " + location + " room on " + therapyDate + " (Tomorrow) at " + therapyTime + ". Further information will be sent soon.\n\nThanks,\nMentalCheck"
                msg = MIMEText(text)
                msg['Subject'] = "MentalCheck Counseling Appointment Confirmation"
                msg['From'] = sender
                msg['To'] = recipient
                server.send_message(msg)
        if((int(ScheduledDate[2])==int(TodayDate[2])) and (int(ScheduledDate[0])==int(TodayDate[1]))):
            if(int(ScheduledDate[1])-int(TodayDate[0])==0):
                text = "Greetings,\nyou have a " + therapyType + " Counseling session with " + therapist + " in our " + location + " room on " + therapyDate + " (Today) at " + therapyTime + ". Further information will be sent soon.\n\nThanks,\nMentalCheck"
                msg = MIMEText(text)
                msg['Subject'] = "MentalCheck Counseling Appointment Confirmation"
                msg['From'] = sender
                msg['To'] = recipient
                server.send_message(msg)

        recipientTherapist = therapists[therapist]
        text = "Greetings,\nYou have a " + therapyType + " Counseling session with " + recipient + " in our " + location + " room on " + therapyDate + ", " +therapyTime + ". The room link will be " + link + ". Please confirm this with " + recipient + ".\nThanks,\nMentalCheck"
        therapistMSG = MIMEText(text)
        therapistMSG['Subject'] = "New MentalCheck Appointment Scheduled"
        therapistMSG['From'] = sender
        therapistMSG['To'] = recipientTherapist
        server.send_message(therapistMSG)
    elif(therapist not in therapists):
        text = "Greetings,\nYour meeting will not be scheduled since " + therapist + " is not in our records. Please schedule another meeting.\nApologies,\nMentalCheck"
        msg = MIMEText(text)
        msg['Subject'] = "MentalCheck Counseling Appointment Confirmation"
        msg['From'] = sender
        msg['To'] = recipient
        server.send_message(msg)





    

#server.login(sender, getpass(prompt="Email Password: "))

server.quit()
