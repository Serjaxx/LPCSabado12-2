from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://mexico.as.com/resultados/futbol/mexico_clausura/clasificacion/?omnil=src-sab"
pagina = requests.get(url)
soup = BeautifulSoup(pagina.content, "html.parser")

#Los equipos
eq = soup.find_all("span", class_="nombre-equipo")

equipos = list()

count = 0
for i in eq:
    if count < 18:
        equipos.append(i.text)
    else:
        break
    count += 1

#Puntos
pts = soup.find_all("td", class_="destacado")

puntos = list()

count = 0
for i in pts:
    if count < 18:
        puntos.append(i.text)
    else:
        break
    count += 1

df = pd.DataFrame({"Equipo":equipos, "Puntos":  puntos}, index = list(range(1,19)))
print(df)
df.to_csv("Tabla de la Liga.csv", index=False)
