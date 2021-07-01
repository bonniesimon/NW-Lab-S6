import smtplib 
from email.mime.text import MIMEText 
sender = 'admin@example.com' 
receivers = ['info@example.com'] 
port = 1025 
msg = MIMEText('Mail sent to server from client. This is the message') 
msg['Subject'] = 'Message sent from Client' 
msg['From'] = 'client@clientMachine.com' 
msg['To'] = 'server@serverMachine.com' 
server = smtplib.SMTP('localhost', port) 
server.sendmail(sender, receivers, msg.as_string()) 
print("Successfully sent email") 
server.quit() 