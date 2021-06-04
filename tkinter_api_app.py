#Realizar una aplicación utilizando Tkinter y conectando con una API.

#api PRUEBA : airnow https://docs.airnowapi.org/about

#Importar librerías y modulos
from tkinter import *
from PIL import ImageTk, Image

#Importar modulo para trabajar con APIs
import requests
import json





#Crear parametro de ventana
root = Tk()
root.title("Tkinter + API App")
root.iconbitmap("icon.ico")
root.geometry("400x40")
root.configure(background="green")


#Api - Generated URL
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=60A8D12A-44FA-422D-92B0-9F2C4196D550


#IMPORTAR API
try:
    #Crear una variable api_requests
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=60A8D12A-44FA-422D-92B0-9F2C4196D550")
    #Crear una nueva variable api
    api = json.loads(api_request.content)

    #cargar variables de acuerdo al contenido de la api que queremos ver
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']


except Exception as e:
    api = "Error de conexion con la API"


#Crear la etiqueta para visualizar el contenido de la api en la ventana
#Crear la etiqueta para visualizar el contenido de la api en la ventana
#myLabel = Label(root, text=api)
#myLabel.grid(row=0, column=0)
#probar conexion de api


#Definimos que campos de la API vamos a utilizar
myLabel = Label(root, text=city + "  " + "Air Quality" + " " + str(quality) + " " + category, font= ("Helvetica",22,"bold"), background = "green")
myLabel.grid(row=0, column=0)










#Loop infinito
root.mainloop()