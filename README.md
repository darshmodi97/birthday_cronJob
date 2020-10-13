- This is simple mail sending script using python
- I have written a script for sending birthday wishing mail at 12:00AM on someone's birthday by fetching the data from the database .

# Use crontab module :
1. First of all you have to download cron using this command in terminal
		- sudo apt-get install cron

2. After successfully installation you have to type the command in terminal 
		- crontab -e 
   now press i then following script 
	  0 0 * * python /home/path/to/birthdaymsg.py


		-The syntax is basically this:

		.---------------- minute (0 - 59) 
		|  .------------- hour (0 - 23)
		|  |  .---------- day of month (1 - 31)
		|  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ... 
		|  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7)  OR sun,mon,tue,wed,thu,fri,sat 
		|  |  |  |  |
		*  *  *  *  *  command to be executed
		
	- now press ESC then colon(:) type "wq" and press Enter and it's done !!	


3. change the code in scripting file for change the location to save the log file.
4. database dump file is provided.
