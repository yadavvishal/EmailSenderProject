## Python project##
## First turn on Less secure app of google account ##


from email import message
import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("your email id", email password)
subject="Sending email using python"
body=" Hiii"
message="Subject:{}\n{}".format(subject, body)
listOfAddress=["receiver email id","receiver email id"]
ob.sendmail("your email id",listOfAddress,message)
print("Send successfully")
ob.quit()
