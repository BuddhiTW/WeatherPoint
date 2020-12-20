# ----------------------------------------Author:Buddhi Thilakshana-----------------------------------------------------
import requests
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from time import sleep


gui = Tk()

gui.geometry("900x600")
gui.title("THE WEATHER POINT")
gui.resizable(False, False)
topframe = Frame(gui)
topframe.pack(side=TOP)

load = Image.open('weather123.jpg')
tkimage = ImageTk.PhotoImage(load)
gui.attributes('-alpha', 0.95)

Label(gui, image=tkimage).place(x=0, y=0, relwidth=1, relheight=1)


# ---------------------------------------------------------------------------------------------------------------------
def all():
    global search
    try:
        city = str(search.get())
        api = 'http://api.openweathermap.org/data/2.5/weather?appid=3da456d66277df508d4402b846b4532f&q='
        url = api+city
        jd = requests.get(url).json()

        print(jd)

        name = jd['name']

        # condition
        condition = jd['weather'][0]['main']

        # temperature
        temperature = jd['main']['temp']
        t = str(temperature-273)+ "celcius"

        # pressure
        pressure = jd['main']['pressure']
        p = str(pressure)+ "BAR"

        # humidity
        humidity = jd['main']['humidity']
        h = humidity

        # wind

        wind = jd['wind']['speed']
        w = str(wind)+ "kMph"

        try:
            winddir = jd['wind']['deg']
            wr = str(winddir)+ "degree"
        except:
            print("null_direction")
        # condition
        description = jd['weather'][0]['description']
        d = description

        # clouds
        clouds = jd['clouds']['all']
        c = str(clouds)+ "%"

    # ---------------------------------------------------------------------------------------------------------------------
        mainLabel.configure(text="THE WEATHER FOCAST OF "+name.upper())
        mainLabel.place(x=250, y=82)

        

        condition_label.configure(text=f"Condition      :{condition}")
        condition_label.place(x=82, y=180)

        temperature_label.configure(text=f"Temperature :{t}")
        temperature_label.place(x=82, y=200)

        pressure_label.configure(text=f"Pressure         :{p}")
        pressure_label.place(x=82, y=220)

        wind_label.configure(text=f"Wind              :{w}")
        wind_label.place(x=82, y=240)

        clouds_label.configure(text=f"Clouds          :{c}")
        clouds_label.place(x=82, y=260)

        humidity_label.configure(text=f"Humidity       :{h}%")
        humidity_label.place(x=82, y=280)

        description_label.configure(text=f"Description   :{d}")
        description_label.place(x=82, y=300)

        exceptLabel.configure(text="")
        exceptLabel.place(x=0, y=82)

        print("weather forcast of", name)



    # ---------------------------------------------------------------------------------------------------------------------

    except:

        mainLabel.configure(text="",)
        mainLabel.place(x=0, y=82)

        condition_label.configure(text="")
        condition_label.place(x=0, y=82)

        temperature_label.configure(text="")
        temperature_label.place(x=0, y=82)

        pressure_label.configure(text="")
        pressure_label.place(x=0, y=82)

        wind_label.configure(text="")
        wind_label.place(x=0, y=82)

        clouds_label.configure(text="")
        clouds_label.place(x=0, y=82)

        humidity_label.configure(text="")
        humidity_label.place(x=0, y=82)

        description_label.configure(text="")
        description_label.place(x=0, y=82)

        exceptLabel.configure(
            text="You might have a connection error or an error with the name you entered !")
        exceptLabel.place(x=250, y=250)


# ---------------------------------------------------------------------------------------------------------------------
# main label
mainLabel = Label(font="VERDANA", bg="skyblue", fg="red")
mainLabel.place(x=0, y=82)

# search bar
search = Entry(bg="yellow")
search.place(x=20, y=22)

# Search Button
ttk.Button(text="Search", command=all).place(x=140, y=19)
text = Text(wrap=WORD)

# all_lables
condition_label = Label(text="", bg="skyblue",font=('calibri', 12))
condition_label.place(x=0, y=82)


temperature_label = Label(text="", bg="skyblue",font=('calibri', 12))
temperature_label.place(x=0, y=82)

pressure_label = Label(text="", bg="skyblue",font=('calibri', 12))
pressure_label.place(x=0, y=82)

wind_label = Label(text="", bg="skyblue",font=('calibri', 12))
wind_label.place(x=0, y=82)

clouds_label = Label(text="", bg="skyblue",font=('calibri', 12))
clouds_label.place(x=0, y=82)

humidity_label = Label(text="", bg="skyblue",font=('calibri', 12))
humidity_label.place(x=0, y=82)

description_label = Label(text="", bg="skyblue",font=('calibri', 12))
description_label.place(x=0, y=82)

exceptLabel = Label(text="", bg="skyblue", fg="red",font=('calibri', 12))
exceptLabel.place(x=0, y=82)


# ---------------------------------------------------------------------------------------------------------------------

gui.mainloop()
