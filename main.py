from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x700+300+100")
root.resizable(False, False)
root.configure(bg="#3d5a80")

def getWeather():
    city = textfield.get()

    geoloactor = Nominatim(user_agent="weather_app_modern", timeout=10)
    location = geoloactor.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng = location.longitude, lat = location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    time_label.config(text = current_time)

    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c82d3f9340585f5049cbb4075c74c4e3"
    json_data = requests.get(api).json()

    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp'] - 273.15)
    feels_like = int(json_data['main']['feels_like'] - 273.15)
    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]
    wind = json_data["wind"]["speed"]
    visibility = json_data.get("visibility", "N/A")
    if visibility != "N/A":
        visibility = f"{int(visibility/1000)} km"
    
    # Update UI
    temp_label.config(text=f"{temp}°")
    condition_label.config(text=condition)
    feels_label.config(text=f"FEELS LIKE {feels_like}°")
    
    wind_value.config(text=f"{wind} km/h")
    humidity_value.config(text=f"{humidity}%")
    pressure_value.config(text=f"{pressure} hpa")
    visibility_value.config(text=visibility if visibility != "N/A" else "fog")
    

main_frame = Frame(root, bg="#5d7a9e", bd=0)
main_frame.place(x=150,y=80,width=600,height = 540)

content_frame = Frame(main_frame, bg="#6e8aa8", bd=0)
content_frame.place(x=20, y=20, width=560, height=500)

search_frame = Frame(content_frame, bg="#8c9fb3", bd=0, highlightthickness=1, highlightbackground="#a8b8c9")
search_frame.place(x=40,y=30,width=480,height=50)

textfield = Entry(search_frame, justify='left', font=("Helvetica", 16), bg="#8c9fb3", border=0, fg="white", insertbackground="white")
textfield.place(x=20,y=10,width=400,height=30)
textfield.insert(0,"delhi")
textfield.focus()

search_btn = Button(search_frame, text = "🔍", font=('Arial',16),bg = "#8c9fb3", border=0, fg="white", cursor="hand2", command=getWeather)
search_btn.place(x=430,y=8,width=35,height=35)

try:
    from PIL import Image, ImageTk
    logo_img = Image.open("assets/logo.png")
    logo_img = logo_img.resize((150, 150), Image.Resampling.LANCZOS)
    logo_image = ImageTk.PhotoImage(logo_img)
    icon_label = Label(content_frame, image=logo_image, bg="#6e8aa8")
    icon_label.place(x=80, y=120)
except:
    icon_label = Label(content_frame, text="🌫️", font=("Arial", 80), bg="#6e8aa8")
    icon_label.place(x=80, y=120)


temp_label = Label(content_frame, text = "12°", font=("Helvetica", 100, 'bold'), bg="#6e8aa8", fg = "white")
temp_label.place(x=280,y=120)

condition_label = Label(content_frame, text="Foggy", font=("Helvetica", 28), bg="#6e8aa8", fg="white")
condition_label.place(x=280,y=260)

feels_label = Label(content_frame, text = "FEELS LIKE 12°", font=("Helvetica", 12), bg="#6e8aa8", fg="#d0dae6")
feels_label.place(x=280,y=310)

time_label = Label(content_frame, text = "10:00 AM", font=("Helvetica", 10), bg="#6e8aa8", fg="#d0dae6")
time_label.place(x=40,y=350)

card_y = 380
card_width = 110
card_height = 100
spacing = 15

wind_card = Frame(content_frame, bg="#7d92a8", bd=0)
wind_card.place(x=40, y=card_y, width=card_width, height=card_height)
Label(wind_card, text="💨", font=("Arial", 20), bg="#7d92a8", fg="white").pack(pady=(5,0))
Label(wind_card, text="WIND", font=("Helvetica", 8), bg="#7d92a8", fg="#c0ccd9").pack()
wind_value = Label(wind_card, text="1.03 km/h", font=("Helvetica", 10, "bold"), bg="#7d92a8", fg="white")
wind_value.pack()

humidity_card = Frame(content_frame, bg="#7d92a8", bd=0)
humidity_card.place(x=40+card_width+spacing, y=card_y, width=card_width, height=card_height)
Label(humidity_card, text="💧", font=("Arial", 20), bg="#7d92a8", fg="white").pack(pady=(5,0))
Label(humidity_card, text="HUMIDITY", font=("Helvetica", 8), bg="#7d92a8", fg="#c0ccd9").pack()
humidity_value = Label(humidity_card, text="94%", font=("Helvetica", 10, "bold"), bg="#7d92a8", fg="white")
humidity_value.pack()

pressure_card = Frame(content_frame, bg="#7d92a8", bd=0)
pressure_card.place(x=40+(card_width+spacing)*2, y=card_y, width=card_width, height=card_height)
Label(pressure_card, text="⏱️", font=("Arial", 20), bg="#7d92a8", fg="white").pack(pady=(5,0))
Label(pressure_card, text="PRESSURE", font=("Helvetica", 8), bg="#7d92a8", fg="#c0ccd9").pack()
pressure_value = Label(pressure_card, text="1017 hpa", font=("Helvetica", 10, "bold"), bg="#7d92a8", fg="white")
pressure_value.pack()

visibility_card = Frame(content_frame, bg="#7d92a8", bd=0)
visibility_card.place(x=40+(card_width+spacing)*3, y=card_y, width=card_width, height=card_height)
Label(visibility_card, text="☁️", font=("Arial", 20), bg="#7d92a8", fg="white").pack(pady=(5,0))
Label(visibility_card, text="VISIBILITY", font=("Helvetica", 8), bg="#7d92a8", fg="#c0ccd9").pack()
visibility_value = Label(visibility_card, text="fog", font=("Helvetica", 10, "bold"), bg="#7d92a8", fg="white")
visibility_value.pack()


root.mainloop()