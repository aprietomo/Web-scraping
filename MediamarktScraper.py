from sys import argv
import time
import requests
from bs4 import BeautifulSoup
import csv

arrNames = []
arrPrices = []

#Obtiene el numero de paginas que contienen productos de una clasificacion
def getnumberPages():
	i = 1
	while True:
		try:
			req2 = requests.get(Nexturl+str(i+1))
			BSoup2 = BeautifulSoup(req2.text, "html.parser")
			items2 = BSoup2.find_all('div',{'class':'product-wrapper'})
			if not items2:
				return i
			else:
				i += 1

		except requests.exceptions.RequestException as e:
			print "Esta url no existe"

#Obtiene los nombres y los precios de productos 
def getProduct(url):
	try:
		req = requests.get(url)
		BSoup = BeautifulSoup(req.text, "html.parser")
		items = BSoup.find_all('div',{'class':'product-wrapper'})
	
		for it in items:
			test = it.find_all('h2')
			for p in test:
				TextProduct = p.find_all(text=True)
				ProductName = ''.join(TextProduct).encode('utf-8').strip()
				arrNames.append(ProductName)			


		prices = BSoup.find_all('div',{'class':'price-box'})

		for pr in prices:
			test2 = pr.find_all('div',{'class':'price small'})
			for p2 in test2:
				TextPrice = p2.find_all(text=True)
				ProductPrice = ''.join(TextPrice).encode('utf-8').strip()
				arrPrices.append(ProductPrice.replace("-","00"))			

	except requests.exceptions.RequestException as e:
		print "Esta url no existe"

#Escribe en un fichero CSV los datos capturados
def EscrbirCSV():

	Fec_actualv1 = time.strftime("%d/%m/%y")
	Fec_actual = time.strftime("%d_%m_%y")

	with open(Nfichero+Fec_actual+".csv","w+") as fichero:
		writer = csv.writer(fichero)
		writer.writerow(('Producto','Precio(EUR)','Fecha dato'))
	
		i = 0
		while i < len(arrNames):
			writer.writerow((arrNames[i],arrPrices[i],Fec_actualv1))
			i += 1



script, Nfichero, Starturl = argv

Nexturl = Starturl+"?page="

Npag = getnumberPages()
actPage = 1

getProduct(Starturl)

while actPage < Npag:
	getProduct(Nexturl+str(actPage+1))
	actPage += 1

EscrbirCSV()
