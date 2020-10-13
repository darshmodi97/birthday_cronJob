from datetime import datetime
import smtplib
from email.message import Message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="birthday"
)

today = datetime.now()
date = today.strftime("%d")
month = today.strftime("%m")
print(date, month)
cursor = conn.cursor()
query =  "select * from Users "\
"where DAY(DOB) = '%s' and MONTH(DOB) = '%s';" %(date,month)
cursor.execute(query)
row = cursor.fetchall()
print(row)

user = "darsh.modi1111@gmail.com"
password = "vnswpyprvlyuwesz"

if row :
    for i in row:
        
        to = i[4] # recipients
        name_of_recepients = i[1] # name 
        subject = "Happy Birthday"
        msg = "Hey It's Darsh, Darsh Modi wants to wish you the many many Happy Returns Of the day and Happy Birthday to you {}. Keep Smiling ..!".format(name_of_recepients)
        body = "Subject:{}\n\n {}".format(subject,msg) #we have to add Subject part here like this ..
        
        # \U0001F382
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        # print(server.ehlo())
        server.starttls()
        server.login(user,password)
        server.sendmail(user,to,body)
        server.quit()
else :
   pass