import tkinter as tk
from tkinter import font

import requests


def weather_res(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']

        output = 'City: %s \nConditions: %s \nTemperature(°F): %s' % (
            name, description, temp)
    except:
        output = "It's not possible to receive the data from source"
    return output


def get_weather(city):
    key = 'a5a4c516dea9381dfa1e1e4b8ff6816d'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'appid': key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = weather_res(weather)


root = tk.Tk()

# background
canvas = tk.Canvas(root, height=250, width=750)
canvas.pack()


# frame
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


entry = tk.Entry(frame)
entry.place(relwidth=0.65, relheight=1)

# actions! create button
button = tk.Button(frame, text="Get Weather", font=40,
                   command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

loweFrame = tk.Frame(root, bg='#090c1c', bd=1)
loweFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(loweFrame, font=('Modern', 30))
label.place(relwidth=1, relheight=1)


root.mainloop()
