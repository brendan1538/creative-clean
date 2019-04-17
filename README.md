# creative-clean
A script that walks through a directory, looks for old files with a certain extension, and deletes them automatically if they're older than a specified number of days.

------------------------------------------

CreativeClean
(MacOS)

About
CreativeClean is a solution to the inevitable clutter of old creative (Photoshop files, PNG’s, MP4’s, etc.) It can either run manually each time or in the background, and only removes files that have not been modified in a set span of time.

Set-up / Customization
1.	Place the creative-clean.py file in the highest folder you want cleaned. It will begin there and work down through every sub-directory.
2.	Open up the creative-clean.py script in a text editor such as VSCode or Atom.
3.	Adjust the timedelta below to how many days back you’d like to keep creative ( the default keeps everything modified within the past 30 days). <br>
     a.	dline = (datetime.datetime.today() +
   	         datetime.timedelta(-30)).strftime('%m/%d/%Y')
4.	Add any other extensions for files you’d like to be deleted to the following tuple <br>
     a.	extensions = ('.png', '.jpg', '.psd', '.mov', '.mp4')
5.	The very last line calculates how often to run the script. The default is 30 days (d * o, where d = number of seconds in one day and o = the span between each occurrence of the script running). You can adjust o to fit your desired number of days between each run. <br>
     a.	time.sleep(86400*30)  # Run every 30 days


Running

1.	Open up a terminal window and cd into the directory where you put creative-clean.py
2.	Type python3 creative-clean.py and press enter to run the script.
3.	Hit CTRL + Z to pause the script
4.	Note your Job #
5.	Type bg %JOBNUMBER and press enter (replace JOBNUMBER with the number you found from step 4).
6.	The script will now be running in the background. If you need to restart your machine, the job will be interrupted and you will need to repeat steps 1 – 5 again.

Notes
	If you need to kill the process at any time, one of the easiest ways to do this is by hitting CMD + Space and searching for Activity Monitor. Look through the active processes and you should see a terminal process that says “open”. You can select and kill that process and the script will not longer run in the background.
