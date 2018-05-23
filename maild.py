#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


# In[2]:


email_user = 'automailpy3@gmail.com'
email_password = 'auto_mailpy3'
email_send = 'nikhilsai313@gmail.com'
subject = 'system issue'


# In[4]:


msg = MIMEMultipart()
msg['From'] = "Diagnostics"
msg['To'] = "Admin"
msg['Subject'] = subject


# In[5]:


body = 'system stats are in the attachment'
msg.attach(MIMEText(body,'plain'))


# In[6]:


filename='diskspike.png'
attachment =open(filename,'rb')


# In[7]:


part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)


# In[9]:


msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


# In[10]:


server.sendmail(email_user,email_send,text)
server.quit()

