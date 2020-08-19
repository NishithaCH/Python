import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("manishakatiyar1111@gmail.com","02march2000")
msg="HI, pineapple is love"
s.sendmail("manishakatiyar1111@gmail.com","shwetakumari152000@gmail.com",msg)
print("your email was sent")
s.quit()
