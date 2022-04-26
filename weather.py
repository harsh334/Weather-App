from tkinter import *
from tkinter import messagebox
import time
from typing import final
import requests
from configparser import ConfigParser
# import json,base64

# api_key = "a1fb6c8ce5096de43e6a6e4ea4288a5b"
url ="http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

# --------------------------------------------

config_file= 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key= config['api_key']['key']

# ---------------------------------------------

def f(city):
    # strng.get()
    # print(strng.get())
    
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()         #convert the result in json for better undersatanding
        name = json['name']
        country = json['sys']['country']
        temp_k = json['main']['temp']
        temp_c = temp_k - 273.15
        pressure = json['main']['pressure']
        humidity = json['main']['humidity']
        # min_temp_k = json['main']['temp_min']
        # min_temp_c = min_temp_k - 273.15
        # max_temp_k= json['main']['temp_max']
        # max_temp_c = min_temp_k - 273.15
        wind_speed = json['wind']['speed']          #m/s
        visibility = json['visibility'] /1000      #meter
        condition = json['weather'][0]['main']
        final = (name,country,temp_c,pressure,humidity,visibility,wind_speed,condition)
        return final
    else:
        print(None)

# print(func('London'))
def func():
    city = strng.get()
    
    weather = f(city)
    if weather:
        # print('yes')
        roots = Tk()
        roots.geometry("700x500")
        

        name_lbl = Label(roots,text="",font=("Georgia" ,30 ,"bold"),fg="brown")
        name_lbl.pack(pady=30)

        temp_lbl = Label(roots,text="",font=("Georgia",15,"normal"))
        temp_lbl.pack(pady=10)

        pressure_lbl = Label(roots,text="",font=("Georgia",15,"normal"))
        pressure_lbl.pack(pady=10)

        humidity_lbl = Label(roots,text="",font=("Georgia",15,"normal"))
        humidity_lbl.pack(pady=10)

        windspeed_lbl = Label(roots,text="",font=("Georgia",15,"normal"))
        windspeed_lbl.pack(pady=10)

        visibility_lbl = Label(roots,text="",font=("Georgia",15,"normal"))
        visibility_lbl.pack(pady=10)

        condition_lbl = Label(roots,text="",font=("Georgia",15,"normal"))
        condition_lbl.pack(pady=10)


        name_lbl['text']="{}, {}".format(weather[0],weather[1])
        temp_lbl['text']="Temperature : {:.2f}°C".format(weather[2])
        pressure_lbl['text'] = "Pressure : {} hpa".format(weather[3])
        humidity_lbl['text']="Humidity : {} %".format(weather[4])
        # mintemp_lbl['text']="Minimum temp. : {:.2f}°C".format(weather[3])
        # maxtemp_lbl['text']="Maximum temp. : {:.2f}°C".format(weather[4])
        visibility_lbl['text']="Visibility : {} Km".format(weather[5])
        windspeed_lbl['text']="Wind Speed : {:.2f} m/s".format(weather[6])
        condition_lbl['text']="Condition : {}".format(weather[7])

        roots.mainloop()

    else:
        messagebox.showerror("Error","no city found")

root=Tk()
# root.geometry("600x400")
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

bg_pic = PhotoImage(file="—Pngtree—cloud creative texture horror weather_1175051.png")
bg = Label(root,image=bg_pic)
bg.place(x=0,y=0)

Label(root,text="Weather App",font=("Georgia" ,50 ,"bold")).pack(pady=60)
Label(root,text="Enter the city name",font=("Georgia",20,"normal"),fg="purple",bg="white").pack()

strng=StringVar()
cityname=Entry(root,textvariable=strng,width=40,font=("Calibri, 20")).pack(pady=20,ipady=10,ipadx=10)

Button(root,text="Find Weather",command=func,font=("Georgia",15,"normal"),fg="purple",relief=RAISED,padx=10,pady=6).pack(pady=20)

Button(root,text="Quit !",command=quit,font=("Georgia",15,"underline"),fg="red",relief=RAISED,padx=10,pady=6).pack(pady=10)

root.mainloop()









