import smtplib  

fromaddr = 'from2@gmail.com' 
toaddrs  = 'to2@gmail.com'
msg = "I was bored!"

# Credentials   
#password = '*******'

# The actual mail send  
#server = smtplib.SMTP('smtp.gmail.com:587')  
server = smtplib.SMTP('127.0.0.1', 2525)

server.ehlo()
#server.starttls()  
#server.login(fromaddr,password)

server.sendmail(fromaddr, toaddrs, msg)

server.quit()

print("done")
