import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
username = input("Enter mail id")
print(username)
password = input("Enter password")
print(password)
# me == my email address
# you == recipient's email address
me = "creativityshah@gmail.com"
you = "shahr399@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = ""
html = """
<html>
  <head></head>
  <body>
   <h6> welcome!</h6>
   <a href="https://www.facebook.com/"> <img src="https://scontent.fmaa1-1.fna.fbcdn.net/v/t1.0-1/p200x200/1382062_574357299267862_1997202362_n.png?_nc_cat=1&oh=448f87984388f6475b1a7f7baf401116&oe=5C0AFCF1"/></a>
   <h5> Welcome</h5>
   <a href="https://twitter.com/login"> <img src="https://a.slack-edge.com/ae7f/img/services/twitter_512.png"width="200" height="200"/> </a>
  </body>
</html>"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login(username, password)
mail.sendmail(me, you, msg.as_string())
mail.quit()
'''<html>
  <head></head>
  <body>
   <h6> welcome!</h6>
   <a href="https://www.facebook.com/"> <img src="https://scontent.fmaa1-1.fna.fbcdn.net/v/t1.0-1/p200x200/1382062_574357299267862_1997202362_n.png?_nc_cat=1&oh=448f87984388f6475b1a7f7baf401116&oe=5C0AFCF1"/></a>
   <h5> Welcome</h5>
   <a href="https://twitter.com/login"> <img src="https://a.slack-edge.com/ae7f/img/services/twitter_512.png"width="200" height="200"/> </a>
  </body>
</html>'''
'''
import os
import re
import signal
import datetime
import time
import smtplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import Encoders
from email.mime.base import MIMEBase
file_incoming_path="Test/"
TotalFile=set(["FG06.tar.gz","CLG1_backlog.tar.gz","FP01.tar.gz","FP02.tar.gz","ASB.zip","ASBd.zip","ASBd2.zip","ASBd3.zip","ASBd4.zip","ASBd5.zip"])
#print TotalFile
ls=set(os.listdir(file_incoming_path))
#print ls
ReceivedFileList=list(TotalFile.intersection(ls))#FG06.tar.gz,#CLG1_backlog.tar.gz
NotReceivedFileList=list(ls.union(TotalFile)-ls.intersection(TotalFile))
#print NotReceivedFileList
#print ReceivedFileList
FileDescriptionName=list()
process_date_found=list()
start_time_found=list()
start_utc_time_found=list()
file_size_found=list()
color=list()
TAR='[\w\W\d\_\s]+.tar.gz' # Regular Expression
ZIP='[\w\W\d\_@\s]+.zip'    # Regular Expression
CompiledTar=re.compile(TAR)
CompiledZip=re.compile(ZIP)
#print CompiledTar
#print CompiledZip
Today10am = str(datetime.time(hour=10 , minute=0, second=0, microsecond=0))
print Today10am
for i in ReceivedFileList:
 if CompiledTar.match(i):
      FileDescriptionName.append(i[::-1].split('.', 1)[1].split('.', 1)[1][::-1])
      process_date_found.append(datetime.datetime.now().strftime("%d-%m-%Y"))
      file_size_found.append(str(((os.path.getsize(file_incoming_path+i)))))
      TimeArrived=datetime.datetime.now().time().strftime('%H:%M %p')
      start_utc_time_found.append(datetime.datetime.utcnow().strftime("%H:%M %p"))
      if TimeArrived > Today10am:
        start_time_found.append(datetime.datetime.now().time().strftime('%I:%M %p'))
        print "arrived delay"
        color.append("yellow")
      if TimeArrived <= Today10am:
        start_time_found.append(datetime.datetime.now().time().strftime('%I:%M %p'))
        print "arrived on time"
        color.append("green")
 if CompiledZip.match(i):
     FileDescriptionName.append(i[::-1].split('.',1)[1][::-1])
     process_date_found.append(datetime.datetime.now().strftime("%d-%m-%Y"))
     file_size_found.append(str(((os.path.getsize(file_incoming_path+i)))))
     TimeArrived=datetime.datetime.now().time().strftime('%H:%M %p')     
     start_utc_time_found.append(datetime.datetime.utcnow().strftime("%H:%M %p"))
     if TimeArrived > Today10am:
       print "arrived delay"
       start_time_found.append(datetime.datetime.now().time().strftime('%I:%M %p')) 
       color.append("yellow")
     if TimeArrived <= Today10am:
       start_time_found.append(datetime.datetime.now().time().strftime('%I:%M %p'))
       print "arrived on time"
       color.append("green")
for i in NotReceivedFileList:
    if CompiledTar.match(i):
       FileDescriptionName.append(i[::-1].split('.', 1)[1].split('.', 1)[1][::-1])
       process_date_found.append(datetime.datetime.now().strftime("%d-%m-%Y"))
       start_time_found.append("N/A")
       start_utc_time_found.append("N/A")
       file_size_found.append("not mentioned")
       color.append("red")
    if CompiledZip.match(i):
       FileDescriptionName.append(i[::-1].split('.',1)[1][::-1])
       process_date_found.append(datetime.datetime.now().strftime("%d-%m-%Y"))
       start_time_found.append("N/A")
       file_size_found.append("not mentioned")
       start_utc_time_found.append("N/A")
       color.append("red")
      
print FileDescriptionName
print color
print process_date_found
print start_time_found
print start_utc_time_found
print file_size_found


style="background:"
style1="style="
fromaddr = "creativityshah@gmail.com"
toAddr ="aakashkumar667@gmail.com"
#toadr = ', '.join(str(e) for e in toAddr)
#print toadr
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toAddr
msg['Subject'] = "Daily record count Status"
part = MIMEBase('application', "octet-stream")
Encoders.encode_base64(part)
html = '<html> <head>  </head> <body> <h1>Statistics</h1> <table style="border-collapse: collapse;" border="1" width="1000" cellspacing="0" cellpadding="0"> <tr style="background: #4d20bc;"> <td colspan="2" rowspan="3" style="margin-left:15px"; class="decorate">Feeding&nbsp;System</td> <td rowspan="3" class="decorate" style="margin-left:15px";>File&nbsp;Size</td> <td rowspan="3" class="decorate" style="margin-left:15px";>File&nbsp;Dated</td><td rowspan="3" class="decorate" style="margin-left:15px";> Type </td> <td rowspan="3" class="decorate" style="margin-left:15px";> Critical/Non&nbsp;Critical </td><td colspan="4" width="256" class="decorate" style="margin-left:100px";>Cut-off&nbsp;Time</td><td rowspan="3" class="decorate" style="margin-left:5px";>Status</td> </tr> <tr style="background: #4d20bc;"> <td colspan="2" class="decorate" style="margin-left:45px"; >Standard </td><td colspan="2" class="decorate" style="margin-left:45px";> Actual </td> </tr> <tr style="background: #4d20bc;"> <td class="decorate" style="margin-left:20px";>IST </td><td class="decorate" style="margin-left:20px";>CET </td> <td class="decorate" style="margin-left:20px";>IST </td> <td class="decorate" style="margin-left:20px";>CET </td></tr>'
for i in xrange(0, len(FileDescriptionName)):
 html+='<tr><td style="background:pink";></td><td '+"style=\"font-size:14px;\""+''+">"+''.join(FileDescriptionName[i:i+1])+'</td><td>' + '</td><td>'.join(file_size_found[i:i+1])+'</td><td>' + '</td><td>'.join(process_date_found[i:i+1])+'</td><td>Outbound</td><td>Non-crictal</td><td>10:00&nbsp;AM</td><td>5:30&nbsp;PM</td><td>' + '</td><td>'.join(start_time_found[i:i+1])+'</td><td>' + '</td><td>'.join(start_utc_time_found[i:i+1])+'</td><td '+''+style1+'"'+style+'" "'.join(color[i:i+1])+';">&nbsp;</td></tr>'
html+='</table><p>Status : <span style="color:green;"> GREEN </span> - File arrival on-time, <span style="color:yellow;"> YELLOW</span> - File arrival delayed, <span style="color:red;"> RED </span> - File not received in time and previous day file is used for load</p></body></html>'

part2 = MIMEText(html, 'html')
msg.attach(part2)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "sh123@45ah")
text = msg.as_string()
server.sendmail(fromaddr, toAddr, text)
print "mail sent successfully"
server.quit()
# write to another file'''