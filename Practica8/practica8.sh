#!/bin/python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import argparse
parser= argparse.ArgumentParser()

parser.add_argument("-arch", help="Archivo txt", required= True)
parser.add_argument("-mensaje", help="Mensaje", required= True)
params= parser.parse_args()
archivo=params.arch
frase=params.mensaje

msg = MIMEMultipart()
message = frase

msg['From'] = "sjlb@gmail"

archivo=open(archivo, "r")
lista=archivo.readlines()
numln = 0
for linea in lista:
	numln+=1
	print(numln, linea)
	msg['To']=linea
	msg['Subject']="Salu2"

	msg.attach(MIMEText(message, 'plain'))

	server = smtplib.SMTP('smtp.office365.com:587')

	server.starttls()

	server.login('sjlb@gmail' ,'****')

	server.sendmail(msg['From'], msg['To'], msg.as_string())

	server.quit()
	print("Fue exitoso! enviado a: " % (msg['To']))
	#numln+=1
archivo.close()
