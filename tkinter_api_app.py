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
root.geometry("400x80")

#definir funciones de botones
def zipLookup():
    #zip.get()
    #zipLabel = Label(root, text= zip.get())
    #zipLabel.grid(row = 1, column= 0, columnspan = 2 )

    #IMPORTAR API
    try:
        #Crear una variable api_requests
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() +"&distance=25&API_KEY=60A8D12A-44FA-422D-92B0-9F2C4196D550")
        #Crear una nueva variable api
        api = json.loads(api_request.content)

        #cargar variables de acuerdo al contenido de la api que queremos ver
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']


    #Crear condicional para que dependiendo del valor de la calidad del aire se puede escoger un color para el background.

        if category == "Good":
            wheater_color = "green"
        elif category == "Moderate":
            wheater_color = "yellow" 
        elif category == "Unhealthy for Sensitive Groups":
            wheater_color = "orange"
        elif category == "Unhealthy":
            wheater_color = "red"
        elif category == "Very Unhealthy":
            wheater_color = "#990066"
        elif category == "Hazardous":
            wheater_color = "#660000"
        

        root.configure(background=wheater_color)

        #Definimos que campos de la API vamos a utilizar
        myLabel = Label(root, text=city + "  " + "Air Quality" + " " + str(quality) + " " + category, font= ("Helvetica",22,"bold"), background = wheater_color)
        myLabel.grid(row=1 , column=0, columnspan = 2 )

    except Exception as e:
        api = "Error de conexion con la API"

#Api - Generated URL
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=60A8D12A-44FA-422D-92B0-9F2C4196D550





#Crear la etiqueta para visualizar el contenido de la api en la ventana
#Crear la etiqueta para visualizar el contenido de la api en la ventana
#myLabel = Label(root, text=api)
#myLabel.grid(row=0, column=0)
#probar conexion de api




#Crear Input
zip = Entry(root)
zip.grid(row= 0 , column= 0, stick = W+E+N+S)

#Crear boton de envio
zipButton  = Button(root, text = "Lookup Zipcode", command = zipLookup)
zipButton.grid(row= 0, column=1, stick = W+E+N+S )




#Loop infinito
root.mainloop()