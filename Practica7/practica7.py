import ftplib
import os.path
path = "/debian/"
conn = "ftp.fi.debian.org"
fileName = "RETR README.html"
fileName2 = "RETR README"
fileName3 = "RETR README.mirrors.html"
fileName4 = "RETR README.mirrors.txt"

ftp = ftplib.FTP(conn)
ftp.login()
ftp.cwd(path)
ftp.retrlines("LIST")
with open('archivo.txt', 'wb') as fp:
    ftp.retrbinary(fileName, fp.write)
    ftp.retrbinary(fileName2, fp.write)
    ftp.retrbinary(fileName3, fp.write)
    ftp.retrbinary(fileName4, fp.write)
ftp.quit()

save = "C:/Users/javie/Desktop/TAREAS/3ER SEMESTRE/LAB CIBERSEGURIDAD/Practica7/txt"
