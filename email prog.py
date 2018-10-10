import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
username = input("Enter mail id")
print(username)
password = input("Enter password")
print(password)
# me == my email address
# you == recipient's email address
from = "Enter sender-id"
to = "Enter receiver-id"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = from
msg['To'] = to

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!.Welcome to my page"
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
