from datetime import datetime
import smtplib
from email.message import Message
import mysql.connector
import logging
import pytz 


IST = pytz.timezone('Asia/Kolkata') # Indian standard time

Log_format = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(filename='/home/path/to/birthday.log',
                              level=logging.DEBUG,
                              format=Log_format,
                              )
logging.info("hello")
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
        msg = "Hey It's Darsh, Darsh Modi I want to wish you the many many Happy Returns Of the day and Happy Birthday to you {}. Keep Smiling ..!".format(name_of_recepients)
        body = "Subject:{}\n\n {}".format(subject,msg) #we have to add Subject part here like this ..

        
        try:
            server = smtplib.SMTP("smtp.gmail.com",587)
            server.ehlo()
            # print(server.ehlo())
            server.starttls()
            server.login(user,password)
            server.sendmail(user,to,body)
            logging.info("Email sent to :{} with E-mail: {} at {}".format(name_of_recepients,to,datetime.now(IST).strftime("%d,%B %Y  %X")))
            server.quit()
            
        except Exception as e :
            print("error ",e)
else :
   pass