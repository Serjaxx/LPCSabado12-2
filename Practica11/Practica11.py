import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64

print("ENVIAR CORREO GMAIL")
user = input("Correo de Gmail: ")
password = getpass.getpass("Contraseña de Gmail: ")

remitente = input("De: ")
destinatario = input("Para: ")
asunto = input("Asunto del correo: ")
mensaje = input("Mensaje: ")

gmail = smtplib.SMTP("smtp.gmail.com", 587)
gmail.starttls()
gmail.login(user, password)
gmail.set_debuglevel(1)

header = MIMEMultipart()
header["Subject"] = asunto
header["From"] = remitente
header["To"] = destinatario

mensaje = MIMEText(mensaje, "html")
header.attach(mensaje)

gmail.sendmail(remitente, destinatario, header.as_string())

gmail.quit()






