import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup


import os

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import requests
import xlrd
import weasyprint

#VARIABLES DE ENTORNO

TOKEN = os.environ['TOKENOS']

# Enable logging
logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)



logger = logging.getLogger(__name__)
bot = telegram.Bot(token= TOKEN)


PORT = int(os.environ.get('PORT', 5000))

def rio2(update, context):

	url = 'http://www.saihduero.es/ficha-risr?r=EA073'

	respuesta = urllib.request.urlopen(url)
	contenidoWeb = respuesta.read()



	soup = BeautifulSoup(contenidoWeb, 'html.parser')


	soup.find("p", class_=False, id=False)


	f = open('rio.txt', 'wb')
	f.write(contenidoWeb)

	fecha = open('rio.txt', encoding="utf8")
	data0 = fecha.readlines()[544]


	data0 = data0.replace('								                                <h6 class="card-subtitle">', '')
	data0 = data0.replace('</h6>', '')



	h = open('rio.txt', encoding="utf8")
	data3 = h.readlines()[559]


	data3 = data3.replace('<td class="variable">', '↕️ Nivel: ')
	data3 = data3.replace('<span class="text-muted">m', 'm')
	data3 = data3.replace('</span></td>', '')
	data3 = data3.replace('													','')

	



	j = open('rio.txt', encoding="utf8")
	data5 = j.readlines()[566]


	data5 = data5.replace('<td class="variable">', '🌊 Caudal: ')
	data5 = data5.replace('<span class="text-muted">m3/s', 'm3/s')
	data5 = data5.replace('</span></td>', '')
	data5 = data5.replace('													','')

	




	f = open('rio.txt', encoding="utf8")
	data = f.readlines()[573]


	data = data.replace('<td class="variable">', 'Temperatura: ')
	data = data.replace('<span class="text-muted">ºC', 'ºC')
	data = data.replace('</span></td>', '')
	data = data.replace('													','')

	






	g = open('rio.txt', encoding="utf8")
	data2 = g.readlines()[580]


	data2 = data2.replace('<td class="variable">', '🌧️ Pluviometría: ')
	data2 = data2.replace('<span class="text-muted">l/m2', 'l/m2')
	data2 = data2.replace('</span></td>', '')
	data2 = data2.replace('													','')

	




	user = update.message.from_user
	
	bot.sendPhoto(chat_id=user.id, photo="https://farm66.static.flickr.com/65535/50217207348_7a876968d9_b.jpg")	
	update.message.reply_text("Imagen de archivo\nEste es el estado del Rio Cea a su paso por Sahagún:\n\n🕑 " + data0 + "🏞️ Rio: CEA\n📍 Estación de Aforo: SAHAGÚN\n🌡️ " + (data) + (data2) + (data3) + (data5)+ "\n🌐 Fuente: SAIHDUERO")

def comandos(update, context):

	url = 'https://pastebin.com/raw/NSExyCbd'

	myfile = requests.get(url)

	open('ej.txt', 'wb').write(myfile.content)

	with open('ej.txt') as f:
		mensaje = f.read()
		
	
	update.message.reply_text('🤖 Estos comandos son los únicos que entiendo. Para ejecutarlos, haz click sobre la palabra en azul. (Soy un poco lento, no me metas prisa)')
	update.message.reply_text(mensaje)

def start(update, context):

	update.message.reply_text('🤖 ¡Hola!, soy un BOT creado por Adrián Paniagua y te diré todo lo que sé de Sahagún. Soy un poco lento, no me metas prisa. Aquí te dejo una lista de comandos para que podamos entendenos:')
	
	url = 'https://pastebin.com/raw/NSExyCbd'

	myfile = requests.get(url)

	open('ej.txt', 'wb').write(myfile.content)

	with open('ej.txt') as f:
		mensaje = f.read()
		
	
	update.message.reply_text(mensaje)


def horario(update, context):

	user = update.message.from_user
	
	bot.sendPhoto(chat_id=user.id, photo="https://i.imgur.com/kfaDi9X.png")	
	
def echo(update, context):
	url = 'https://pastebin.com/raw/NSExyCbd'

	myfile = requests.get(url)

	open('ej.txt', 'wb').write(myfile.content)

	with open('ej.txt') as f:
		mensaje = f.read()

		
	
	update.message.reply_text('🤖 Lo siento pero no te entiendo. Actualmente solo entiendo estos comandos. Para ejecutarlos, simplemente haz click sobre la palabra en azul para relizar la acción')
	update.message.reply_text(mensaje)

def telefonos(update, context):
	update.message.reply_text('☎️ Estos teléfonos te pueden ser de interés:\n\n🏢 Ayuntamiento de Sahagún: 987 780 001 \nℹ️ Información Turística: 987 781 015\n🏕️Camping Municipal: 987 780 415 \n📮 Oficina de Correos: 987 780 207 \n📚 Biblioteca Municipal: 987 782 169 \n🏥 Centro de Salud: 987 781 291\n🚑 Ambulancias: 987 780 444\n🚓 Guardia Civil: 987 780 845\n🚆 RENFE: 902 240 202\n🚌 Autobuses: 987 211 000\n✈️ Aeropuerto (León): 902 404 704\n🚗 Información de Tráfico: 900 123 505\n')
def webs(update, context):
	update.message.reply_text('Estas páginas webs te pueden ser útiles:\n\nℹ️ Turismo Sahagún: https://www.turismosahagun.com/\n📷 Adrián Paniagua: https://adrianpaniagua.es/\n📰 Sahagún Digital: http://sahagundigital.com/\n📷 Jose Luis Luna: https://www.joseluisluna.com/')
def help(update, context):
	update.message.reply_text('Esta es una lista de comandos para el bot, simplemente haz click sobre la palabra en azul para relizar la acción: \n ')

def farmacia(update, context):
	update.message.reply_text('⚕️ FARMACIAS DE GUARDIA EN LA PROVINCIA\n Puedes acceder al buscador desde el siguiente enlace: \n 🔗 http://bit.ly/cofleon ')
	

def tiempo(update, context):

	url = 'http://www.saihduero.es/ficha-risr?r=EA073'

	respuesta = urllib.request.urlopen(url)
	contenidoWeb = respuesta.read()
	soup = BeautifulSoup(contenidoWeb, 'html.parser')
	soup.find("p", class_=False, id=False)
	f = open('rio.txt', 'wb')
	f.write(contenidoWeb)

	f = open('rio.txt', encoding="utf8")
	data = f.readlines()[573]




	data = data.replace('<td class="variable">', ': ')
	data = data.replace('<span class="text-muted">ºC', 'ºC')
	data = data.replace('</span></td>', '')
	data = data.replace('													','')
	#AMANECER

	urlama = "https://salidaypuestadelsol.com/sun/sahagun"

	respuesta2 = urllib.request.urlopen(urlama)
	contenidoWeb2 = respuesta2.read()

	soup2 = BeautifulSoup(contenidoWeb2, 'html.parser')


	soup2.find("p", class_=False, id=False)


	g = open('amanecer.html', 'wb')
	g.write(contenidoWeb2)

	fecha2 = open('amanecer.html', encoding="utf8")
	data00 = fecha2.readlines()[376]

	fecha2 = open('amanecer.html', encoding="utf8")
	data01 = fecha2.readlines()[388]

	data00 = data00.replace('                <div class="time">', '')
	data00 = data00.replace('</div>', '')



	data01 = data01.replace('                <div class="time">', '')
	data01 = data01.replace('</div>', '')



	#PDF

	url2 = "https://www.eltiempo.es/pdf/sahagun.pdf"
	myfile = requests.get(url2)
	open('tiempo.pdf', 'wb').write(myfile.content)


	user = update.message.from_user

	update.message.reply_text("☀️ EL TIEMPO EN SAHAGÚN ☂️\n\n🌡️ TEMPERATURA ACTUAL" +data+"\n🌅 SALIDA  DEL SOL: "+data00+"\n🌆 PUESTA DEL SOL: "+data01+"\n🔮 PREVISIÓN PARA LOS PROXIMOS DIAS:")
	bot.sendDocument(chat_id=user.id, document=open('tiempo.pdf', 'rb'))

def contacto(update, context):
	update.message.reply_text('Puedes contactar con el creador del BOT en:\n👉 bot@adrianpaniagua.es\n👉 @APLEONI')

def agenda(update, context):
	url = 'https://pastebin.com/raw/tGLevJ1g'

	myfile = requests.get(url)

	open('ej.txt', 'wb').write(myfile.content)

	with open('ej.txt') as f:
		mensaje = f.read()
		
	
	update.message.reply_text(mensaje)


def tren(update, context):

	url = 'https://pastebin.com/raw/d7WuyDfG'

	myfile = requests.get(url)

	open('ej.txt', 'wb').write(myfile.content)

	with open('ej.txt') as f:
		mensaje = f.read()
		
	
	update.message.reply_text(mensaje)


def leonsahagun(update, context):
	import datetime


	fecha= datetime.date.today()
	hoy= fecha.strftime("%d-%m-%Y")
	print (hoy)
	url = 'http://horariospdf.renfe.com/HIRRenfeWeb/trenesPdf.do?O=15100&D=15009&F='+hoy+'&ID=s'
	myfile = requests.get(url)
	open('horario.pdf', 'wb').write(myfile.content)

	print (hoy)

	user = update.message.from_user
	update.message.reply_text("🚉 Este es el horario:\n\n📅FECHA: "+hoy+"\n\n📄FORMATO: PDF\n\n🌐FUENTE: RENFE")
	bot.sendDocument(chat_id=user.id, document=open('horario.pdf', 'rb'))

def sahagunleon(update, context):
	import datetime
	fecha= datetime.date.today()
	hoy= fecha.strftime("%d-%m-%Y")
	print (hoy)
	url = 'http://horariospdf.renfe.com/HIRRenfeWeb/trenesPdf.do?O=15009&D=15100&F='+hoy+'&ID=s'
	myfile = requests.get(url)
	open('horario.pdf', 'wb').write(myfile.content)

	print (hoy)

	user = update.message.from_user
	update.message.reply_text("🚉 Este es el horario:\n\n📅FECHA: "+hoy+"\n\n📄FORMATO: PDF\n\n🌐FUENTE: RENFE")
	bot.sendDocument(chat_id=user.id, document=open('horario.pdf', 'rb'))

def palenciasahagun(update, context):
	import datetime
	fecha= datetime.date.today()
	hoy= fecha.strftime("%d-%m-%Y")
	print (hoy)
	url = 'http://horariospdf.renfe.com/HIRRenfeWeb/trenesPdf.do?O=14100&D=15009&F='+hoy+'&ID=s'
	myfile = requests.get(url)
	open('horario.pdf', 'wb').write(myfile.content)

	print (hoy)

	user = update.message.from_user
	update.message.reply_text("🚉 Este es el horario:\n\n📅FECHA: "+hoy+"\n\n📄FORMATO: PDF\n\n🌐FUENTE: RENFE")
	bot.sendDocument(chat_id=user.id, document=open('horario.pdf', 'rb'))

def sahagunpalencia(update, context):
	import datetime
	fecha= datetime.date.today()
	hoy= fecha.strftime("%d-%m-%Y")
	print (hoy)
	url = 'http://horariospdf.renfe.com/HIRRenfeWeb/trenesPdf.do?O=15009&D=14100&F='+hoy+'&ID=s'
	myfile = requests.get(url)
	open('horario.pdf', 'wb').write(myfile.content)

	print (hoy)

	user = update.message.from_user
	update.message.reply_text("🚉 Este es el horario:\n\n📅FECHA: "+hoy+"\n\n📄FORMATO: PDF\n\n🌐FUENTE: RENFE")
	bot.sendDocument(chat_id=user.id, document=open('horario.pdf', 'rb'))

def noticias(update, context):
	import feedparser
	NewsFeed = feedparser.parse("http://sahagundigital.com/coverrss")
	entr1 = NewsFeed.entries[1]
	entr2 = NewsFeed.entries[2]
	entr3 = NewsFeed.entries[3]
	entr4 = NewsFeed.entries[4]
	entr5 = NewsFeed.entries[5]



	update.message.reply_text("📰 Estas son las ultimas noticias de Sahagún:\n👉 " +(entr1.title)+"\n🔗 "+(entr1.link)+"\n\n👉 "+(entr2.title)+"\n🔗 "+(entr2.link)+"\n\n👉 "+(entr3.title)+"\n🔗 "+(entr3.link)+"\n\n👉 "+(entr4.title)+"\n🔗 "+(entr4.link)+"\n\n👉 "+(entr5.title)+"\n🔗 "+(entr5.link)+"\n\n🌐FUENTE: Sahagún Digital")
def covid(update, context):
	url = 'https://pastebin.com/raw/qudjN0mg'

	myfile = requests.get(url)

	open('ej.txt', 'wb').write(myfile.content)

	with open('ej.txt') as f:
		mensaje = f.read()
		
	
	update.message.reply_text(mensaje)
def piscina(update, context):
	update.message.reply_text("¿Sobre que tipo de entrada desea Información?")
	update.message.reply_text("👉/diariapiscina : Entrada un único dia\n👉/bonotemporada : Bono para toda la temporada\n👉/bonoquincenal : Bono Quincenal\n👉/bonomensual : Bono mensual")

def bonotemporada(update, context):
	url = 'https://pastebin.com/raw/iPX7Gp3q'

	myfile = requests.get(url)

	open('ej.txt', 'wb').write(myfile.content)

	with open('ej.txt') as f:
		mensaje = f.read()
		
	url2 = "https://repo.listaadrian.tk/bot/deporte.pdf"
	myfile = requests.get(url2)
	open('deporte.pdf', 'wb').write(myfile.content)
	user = update.message.from_user
	
	update.message.reply_text(mensaje)
	bot.sendDocument(chat_id=user.id, document=open('deporte.pdf', 'rb'))


def bonoquincenal(update, context):
	url = 'https://pastebin.com/raw/TC6pnTmr'

	myfile = requests.get(url)

	open('ej.txt', 'wb').write(myfile.content)

	with open('ej.txt') as f:
		mensaje = f.read()
		
	url2 = "https://repo.listaadrian.tk/bot/deporte.pdf"
	myfile = requests.get(url2)
	open('deporte.pdf', 'wb').write(myfile.content)
	user = update.message.from_user
	
	update.message.reply_text(mensaje)
	bot.sendDocument(chat_id=user.id, document=open('deporte.pdf', 'rb'))

def bonomensual(update, context):
	url = "https://pastebin.com/raw/JHLKav2p"
	myfile = requests.get(url)

	open('ej.txt', 'wb').write(myfile.content)

	with open('ej.txt') as f:
		mensaje = f.read()
		
	url2 = "https://repo.listaadrian.tk/bot/deporte.pdf"
	myfile = requests.get(url2)
	open('deporte.pdf', 'wb').write(myfile.content)
	user = update.message.from_user
	
	update.message.reply_text(mensaje)
	bot.sendDocument(chat_id=user.id, document=open('deporte.pdf', 'rb'))

def diariapiscina(update, context):
	url = 'https://pastebin.com/raw/wievXCu0'

	myfile = requests.get(url)

	open('ej.txt', 'wb').write(myfile.content)

	with open('ej.txt') as f:
		mensaje = f.read()

	url2 = "https://repo.listaadrian.tk/bot/deporte.pdf"
	myfile = requests.get(url2)
	open('deporte.pdf', 'wb').write(myfile.content)
	user = update.message.from_user
	
	update.message.reply_text(mensaje)
	bot.sendDocument(chat_id=user.id, document=open('deporte.pdf', 'rb'))

def gimnasio(update, contexy):

	url2 = "https://repo.listaadrian.tk/bot/gimnasio.pdf"
	myfile = requests.get(url2)
	open('gimnasio.pdf', 'wb').write(myfile.content)

	url = 'https://pastebin.com/raw/WznSbJ1u'

	myfile = requests.get(url)

	open('ej.txt', 'wb').write(myfile.content)

	with open('ej.txt') as f:
		mensaje = f.read()
	
	user = update.message.from_user
	
	update.message.reply_text(mensaje)
	bot.sendDocument(chat_id=user.id, document=open('gimnasio.pdf', 'rb'))
def padel(update, context):
	url = 'https://pastebin.com/raw/NUYLANMi'

	myfile = requests.get(url)

	open('ej.txt', 'wb').write(myfile.content)

	with open('ej.txt') as f:
		mensaje = f.read()

	url2 = "https://repo.listaadrian.tk/bot/deporte.pdf"
	myfile = requests.get(url2)
	open('deporte.pdf', 'wb').write(myfile.content)
	user = update.message.from_user
	
	update.message.reply_text(mensaje)
	bot.sendDocument(chat_id=user.id, document=open('deporte.pdf', 'rb'))

def taxis(update, context):
	url = 'https://pastebin.com/raw/nkvUdD7Q'

	myfile = requests.get(url)

	open('ej.txt', 'wb').write(myfile.content)

	with open('ej.txt') as f:
		mensaje = f.read()
	update.message.reply_text(mensaje)

def sahagunpromesas(update, content):
	url = 'https://pastebin.com/raw/Uy41Fb2q'

	myfile = requests.get(url)

	open('ej.txt', 'wb').write(myfile.content)

	with open('ej.txt') as f:
		mensaje = f.read()
	update.message.reply_text(mensaje)
def gasolineras(update, context):

	gasoleoA = "https://geoportalgasolineras.es/reportEESSBusqueda?extension=XLS&filter=%7B%22tipoEstacion%22:%22EESS%22,%22idProvincia%22:%2224%22,%22idMunicipio%22:23462,%22idProducto%22:4,%22rotulo%22:%22%22,%22eessEconomicas%22:false,%22conPlanesDescuento%22:false,%22horarioInicial%22:null,%22horarioFinal%22:null,%22calle%22:%22%22,%22numero%22:%22%22,%22codPostal%22:%22%22,%22tipoVenta%22:%22P%22,%22tipoServicio%22:null,%22idOperador%22:null,%22nombrePlan%22:%22%22,%22idTipoDestinatario%22:null,%22report%22:true%7D"

	myfile = requests.get(gasoleoA)
	open('gasofa.xls', 'wb').write(myfile.content)

	workbook = xlrd.open_workbook('gasofa.xls')

	worksheet = workbook.sheet_by_index(0)

	name1 = worksheet.cell(4, 8).value
	name2 = worksheet.cell(5, 8).value
	name3 = worksheet.cell(6, 8).value

	direction1 = worksheet.cell(4, 4).value
	direction2 = worksheet.cell(5, 4).value
	direction3 = worksheet.cell(6, 4).value

	precioA1 = worksheet.cell(4, 7).value
	precioA2 = worksheet.cell(5, 7).value
	precioA3 = worksheet.cell(6, 7).value

	horario1 = worksheet.cell(4, 11).value
	horario2 = worksheet.cell(5, 11).value
	horario3 = worksheet.cell(6, 11).value


	gasoleoB= "https://geoportalgasolineras.es/reportEESSBusqueda?extension=XLS&filter=%7B%22tipoEstacion%22:%22EESS%22,%22idProvincia%22:%2224%22,%22idMunicipio%22:23462,%22idProducto%22:1,%22rotulo%22:%22%22,%22eessEconomicas%22:false,%22conPlanesDescuento%22:false,%22horarioInicial%22:null,%22horarioFinal%22:null,%22calle%22:%22%22,%22numero%22:%22%22,%22codPostal%22:%22%22,%22tipoVenta%22:%22P%22,%22tipoServicio%22:null,%22idOperador%22:null,%22nombrePlan%22:%22%22,%22idTipoDestinatario%22:null,%22report%22:true%7D"

	myfile2 = requests.get(gasoleoB)
	open('gasofa2.xls', 'wb').write(myfile2.content)

	workbook2 = xlrd.open_workbook('gasofa2.xls')

	worksheet2 = workbook2.sheet_by_index(0)

	nameY1 = worksheet2.cell(4, 8).value
	nameY2 = worksheet2.cell(5, 8).value
	nameY3 = worksheet2.cell(6, 8).value

	directionY1 = worksheet2.cell(4, 4).value
	directionY2 = worksheet2.cell(5, 4).value
	directionY3 = worksheet2.cell(6, 4).value

	precioYA1 = worksheet2.cell(4, 7).value
	precioYA2 = worksheet2.cell(5, 7).value
	precioYA3 = worksheet2.cell(6, 7).value

	horarioY1 = worksheet2.cell(4, 11).value
	horarioY2 = worksheet2.cell(5, 11).value
	horarioY3 = worksheet2.cell(6, 11).value

	actualizacion = worksheet.cell(4, 6).value
	actualizacion2 = worksheet2.cell(4, 6).value


	update.message.reply_text("Estos son los precios de la GASOLINA 95 y el GASOLEO A en Sahagún")
	update.message.reply_text("GASOLEO A\n 👉 "+(name1)+"\n💶: "+ (precioA1)+" €" +"\n📍: "+(direction1)+"\n⏰: "+(horario1)+ "\n\n👉 "+(name2)+"\n💶: "+ (precioA2)+" €"+"\n📍: "+(direction2)+"\n⏰: "+(horario2)+"\n\n👉 "+(name3)+"\n💶: "+ (precioA3)+" €"+"\n📍: "+(direction3)+"\n⏰: "+(horario3)+"\n\n📝 Última actualizacion de datos: "+(actualizacion)+"\n🌐 FUENTE: GEOPORTAL")
	update.message.reply_text("GASOLINA 98\n 👉 "+(nameY1)+"\n💶: "+ (precioYA1)+" €"+ "\n📍: "+(directionY1)+"\n⏰: "+(horarioY1)+ "\n\n👉 "+(nameY2)+"\n💶: "+ (precioYA2)+" €"+"\n📍: "+(directionY2)+"\n⏰: "+(horarioY2)+"\n\n👉 "+(nameY3)+"\n💶: "+ (precioYA3)+" €"+"\n📍: "+(directionY3)+"\n⏰: "+(horarioY3)+"\n\n📝 Última actualizacion de datos: "+(actualizacion)+"\n🌐 FUENTE: GEOPORTAL")

def datosclimaticos(update, context):
	user = update.message.from_user
	pdf = weasyprint.HTML('http://www.inforiego.org/opencms/opencms/info_meteo/semana/Proc_MuestraSemana2.jsp?ident=24+8&provincia=0&poblacion=0&zona=0').write_pdf()

	open('semana.pdf', 'wb').write(pdf)
	update.message.reply_text("☁️ Estos son los datos climáticos de esta semana en la estación de Sahagún\n🌐 FUENTE: INFORIEGO")
	bot.sendDocument(chat_id=user.id, document=open('semana.pdf', 'rb'))

def murales(update, context):
	update.message.reply_text("Puedes ver toda la Información sobre los murales en el siguiente enlace: \nhttps://telegra.ph/LOS-MURALES-DE-SAHAG%C3%9AN-10-27")

def autobuses(update, context):
	url = "https://pastebin.com/raw/uA48xvUz"
	myfile = requests.get(url)

	open('ej.txt', 'wb').write(myfile.content)

	with open('ej.txt') as f:
		mensaje = f.read()
	update.message.reply_text(mensaje)

def revistaies(update, context):
	import feedparser
	NewsFeed = feedparser.parse("https://revista.iesdesahagun.es/feed")
	entr1 = NewsFeed.entries[1]
	entr2 = NewsFeed.entries[2]
	entr3 = NewsFeed.entries[3]
	entr4 = NewsFeed.entries[4]
	entr5 = NewsFeed.entries[5]
	update.message.reply_text("📰 Estas son las ultimas publicaciones de la revista escolar:\n👉 " +(entr1.title)+"\n🔗 "+(entr1.link)+"\n\n👉 "+(entr2.title)+"\n🔗 "+(entr2.link)+"\n\n👉 "+(entr3.title)+"\n🔗 "+(entr3.link)+"\n\n👉 "+(entr4.title)+"\n🔗 "+(entr4.link)+"\n\n👉 "+(entr5.title)+"\n🔗 "+(entr5.link)+"\n\n🌐 FUENTE: IES DE SAHAGÚN")
def azud(update, context):
	url = 'http://www.saihduero.es/ficha-risr?r=EM141'

	respuesta = urllib.request.urlopen(url)
	contenidoWeb = respuesta.read()



	soup = BeautifulSoup(contenidoWeb, 'html.parser')


	soup.find("p", class_=False, id=False)


	f = open('rio.txt', 'wb')
	f.write(contenidoWeb)

	fecha = open('rio.txt', encoding="utf8")
	data0 = fecha.readlines()[593]


	data0 = data0.replace('													<td class="variable">', '↕️ Nivel: ')
	data0 = data0.replace('<span class="text-muted">m</span></td>', ' m')

	fecha2 = open('rio.txt', encoding="utf8")
	data1 = fecha2.readlines()[600]

	data1 = data1.replace('													<td class="variable">', '🌊 Caudal:  ')
	data1 = data1.replace('<span class="text-muted">m3/s</span></td>', 'm3/s')


	fecha3 = open('rio.txt', encoding="utf8")
	data2 = fecha3.readlines()[607]

	data2 = data2.replace('													<td class="variable">', '🌡️ Temperatura: ')
	data2 = data2.replace('</td>', ' ºC')


	fecha4 = open('rio.txt', encoding="utf8")
	data3 = fecha4.readlines()[614]

	data3 = data3.replace('													<td class="variable">', '🌧️ Pluviometría: ')
	data3 = data3.replace('<span class="text-muted">l/m2</span></td>', ' l/m2')


	fecha5 = open('rio.txt', encoding="utf8")
	data4 = fecha5.readlines()[578]

	data4 = data4.replace('								                                <h6 class="card-subtitle">', '🕑 : ')
	data4 = data4.replace('</h6>', '')




	update.message.reply_text("Este es el estado del Azud de Galleguillos:\n\n" + (data4) + "🏞️ Cauce: Canal Cea-Carrión\n📍 Estación de Aforo: GALLEGUILLOS\n" + (data0) + (data1) + (data2)+ (data3)+ "\nDatos tomados en el aliviadero de río Cea\n🌐 Fuente: SAIHDUERO")
def mapa(update, context):
	url = 'https://repo.listaadrian.tk/bot/MAPA.pdf'

	myfile = requests.get(url)

	open('mapa.pdf', 'wb').write(myfile.content)


	user = update.message.from_user
	update.message.reply_text("Este es el mapa turístico de Sahagún")
	bot.sendDocument(chat_id=user.id, document=open('mapa.pdf', 'rb'))
def grupo(update, context):
	user = update.message.from_user
	bot.sendPhoto(chat_id=user.id, photo="https://i.imgur.com/5Fw5fcy.png")	
	update.message.reply_text("Puedes unirte al grupo de TELEGRAM de Sahagún en el siguiente enlace: https://t.me/infosahagun ")

def cronicasanonimas(update, context):
	url = 'https://repo.listaadrian.tk/bot/cronicas.pdf'
	myfile = requests.get(url)
	open('CronicasAnonimasDeSahagún.pdf', 'wb').write(myfile.content)

	

	user = update.message.from_user
	
	bot.sendDocument(chat_id=user.id, document=open('CronicasAnonimasDeSahagún.pdf', 'rb'))


def main():




	updater = Updater(TOKEN, use_context=True)

	dp = updater.dispatcher

	dp.add_handler(CommandHandler("cronicasanonimas", cronicasanonimas))
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("rio", rio2))
	dp.add_handler(CommandHandler("horario", horario))
	dp.add_handler(CommandHandler("telefonos", telefonos))
	dp.add_handler(CommandHandler("webs", webs))
	dp.add_handler(CommandHandler("comandos", comandos))
	dp.add_handler(CommandHandler("help", help))
	# dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
	dp.add_handler(CommandHandler("tiempo", tiempo))
	dp.add_handler(CommandHandler("agenda", agenda))
	dp.add_handler(CommandHandler("contacto", contacto))
	dp.add_handler(CommandHandler("tren", tren))
	dp.add_handler(CommandHandler("leonsahagun", leonsahagun))
	dp.add_handler(CommandHandler("palenciasahagun", palenciasahagun))
	dp.add_handler(CommandHandler("sahagunleon", sahagunleon))
	dp.add_handler(CommandHandler("sahagunpalencia", sahagunpalencia))
	dp.add_handler(CommandHandler("noticias", noticias))
	dp.add_handler(CommandHandler("covid", covid))
	dp.add_handler(CommandHandler("bonomensual", bonomensual))
	dp.add_handler(CommandHandler("piscina", piscina))
	dp.add_handler(CommandHandler("diariapiscina", diariapiscina))
	dp.add_handler(CommandHandler("bonoquincenal", bonoquincenal))
	dp.add_handler(CommandHandler("bonotemporada", bonotemporada))
	dp.add_handler(CommandHandler("gimnasio", gimnasio))
	dp.add_handler(CommandHandler("padel", padel))
	dp.add_handler(CommandHandler("taxis", taxis))
	dp.add_handler(CommandHandler("sahagunpromesas", sahagunpromesas))
	dp.add_handler(CommandHandler("gasolineras", gasolineras))
	dp.add_handler(CommandHandler("datosclimaticos", datosclimaticos))
	dp.add_handler(CommandHandler("murales", murales))
	dp.add_handler(CommandHandler("autobuses", autobuses))
	dp.add_handler(CommandHandler("revistaies", revistaies))
	dp.add_handler(CommandHandler("azud", azud))
	dp.add_handler(CommandHandler("mapa", mapa))
	dp.add_handler(CommandHandler("grupo", grupo))
	dp.add_handler(CommandHandler("farmacia", farmacia))

	updater.start_webhook(listen="0.0.0.0",
						  port=int(PORT),
						  url_path=TOKEN)
	updater.bot.setWebhook('https://sahaguninfo.herokuapp.com/' + TOKEN)


	updater.idle()


if __name__ == '__main__':
	main()
