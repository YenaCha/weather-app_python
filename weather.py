from tkinter import *
import tkinter.messagebox
import requests
tk = Tk()
tk.title('My weather app')
tk.geometry('500x300')
citytext = StringVar()
cityentry = Entry(tk, textvariable=citytext).place(x=190, y=130)
placelabel = Label(tk,text='',font=('bold', 15))
placelabel.place(x=190,y=220)
templabel = Label(tk,text='',font=('bold',15))
templabel.place(x=190,y=250)
def findweather():
    city = citytext.get()
    link = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
        city+'&units=metric&appid=22515dbe8047cf659da74a1cae281c2e'
    response = requests.get(link)
    data = response.json()
    placelabel['text']='{} , {}'.format(data['name'],data['sys']['country'])
    templabel['text']='{}°C'.format(data['main']['temp'])


header = Label(tk, text='Weather app', font=('bold', 15)).place(x=190, y=50)
citylabel = Label(tk, text='Enter your city name :',
                  font=('bold', 15)).place(x=190, y=100)

searchbutton = Button(tk, text='Go', width=12,
                      command=findweather).place(x=190, y=170)

tk.mainloop()
