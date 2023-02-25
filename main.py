from tkinter import *
import requests
from PIL import Image,ImageTk
import time

class MyWeather:
    def __init__(self,root):
        self.root=root
        self.root.title("Weather Detector")
        self.root.geometry("350x600+350+100")
        self.root.resizable(False, False)
        self.root.config(bg = "White")
        self.root.wm_iconbitmap("1.ico")

        frame1 = Frame(self.root,bd = 2 , relief = GROOVE,bg = "white")
        frame1.place(x= 5,y=5,width = 340, height = 145)

        city_title = Label(frame1,text = "Weather", font=("goudy old style",10,"bold"),bg = "#033958",fg = "white").place(x = 0,y=3, relwidth = 1)
        self.var_search = StringVar()
        self.txt_city = Entry(frame1,textvariable = self.var_search, font=("goudy old style",15),bg = "white",fg = "#262626",bd = 2 , relief = RIDGE)
        self.txt_city.place(x =3,y=27, width = 330, height = 40)
        self.txt_city.config(fg = "light grey")
        self.txt_city.insert(0,"\t        City Name")
        self.txt_city.bind("<Button-1>", lambda event: self.clear_entry(event,self.txt_city))
        self.btn_search = Button(frame1,text = "Search",command = self.weather, font=("goudy old style",15),cursor = "hand2",bg = "lightgreen",fg = "#262626")
        self.btn_search.place(x =3,y=70, width = 330, height = 25)
        self.btn_search.bind_all('<Return>', self.fun)

        self.warning = Label(frame1,text = "", bg = "white", fg = "dark red",padx = 5)
        self.warning.place(x = 120, y =110,width = 100)

        lbl_foot = Label(self.root,text = "RG Techs || Koustav Dey", font=("goudy old style",10),bg = "#033958",fg = "white",padx = 5).place(x = 0,y=580, relwidth = 1)

        frame2 = Frame(self.root,bd = 2 , relief = GROOVE,bg = "white")
        frame2.place(x= 5,y=149,width = 340, height = 410)
        
        frame3 = Frame(self.root,bd = 2 , relief = GROOVE,bg = "white")
        frame3.place(x= 12,y=152,width = 325, height = 75)



        self.img = Label(frame3,bg = "white")
        self.img.place(x = 127,y=0,height=70,width =70)



        self.temp_highlight = Label(frame3,text = "27"+u"\N{DEGREE SIGN}"+"c",bg = "white",fg = "black",font=("goudy old style",30,"bold"))
        self.temp_highlight.place(x = 10 , y = 5,height = 60,width = 80 )
        self.weather_highlight = Label(frame3,text = "Clear",bg = "white",fg = "black",font=("goudy old style",22,"bold"))
        self.weather_highlight.place(x = 220 , y = 5,height = 60,width = 80 )

        banner_start = Label (frame2,text = "Requests",font=("goudy old style",10),bg = "dark red",anchor ="w",fg = "white").place(x =5,y=77,width = 160)
        banner_end = Label (frame2,text = "Results",font=("goudy old style",10),bg = "dark red",anchor ="w",fg = "white").place(x =165,y=77,width = 164)

        city_info = Label(frame2,text = "City :",font=("goudy old style",15), bg = "white", fg = "black",padx = 5).place(x = 10, y =100)
        self.city_info_data = Label(frame2,text = "",font=("goudy old style",15), bg = "white", fg = "black",padx = 5)
        self.city_info_data.place(x = 160, y =100)
        
        country_info = Label(frame2,text = "Country :",font=("goudy old style",15), bg = "white", fg = "black",padx = 5).place(x = 10, y =130)
        self.country_info_data = Label(frame2,text = "",font=("goudy old style",15), bg = "white", fg = "black",padx = 5)
        self.country_info_data.place(x = 160, y =130)
        
        temp_c_info = Label(frame2,text = "Temp C "+u"\N{DEGREE SIGN}"+":",font=("goudy old style",15), bg = "white", fg = "black",padx = 5).place(x = 10, y =160)
        self.temp_c_info_data = Label(frame2,text = "",font=("goudy old style",15), bg = "white", fg = "black",padx = 5)
        self.temp_c_info_data.place(x = 160, y =160)
        
        temp_f_info = Label(frame2,text = "Temp F "+u"\N{DEGREE SIGN}"+":",font=("goudy old style",15), bg = "white", fg = "black",padx = 5).place(x = 10, y =190)
        self.temp_f_info_data = Label(frame2,text = "",font=("goudy old style",15), bg = "white", fg = "black",padx = 5)
        self.temp_f_info_data.place(x = 160, y =190)
        
        descrip_info = Label(frame2,text = "Weather :",font=("goudy old style",15), bg = "white", fg = "black",padx = 5).place(x = 10, y =220)
        self.descrip_info_data = Label(frame2,text = "",font=("goudy old style",15), bg = "white", fg = "black",padx = 5)
        self.descrip_info_data.place(x = 160, y =220)
        
        lat_info = Label(frame2,text = "Latitude :",font=("goudy old style",15), bg = "white", fg = "black",padx = 5).place(x = 10, y =250)
        self.lat_info_data = Label(frame2,text = "",font=("goudy old style",15), bg = "white", fg = "black",padx = 5)
        self.lat_info_data.place(x = 160, y =250)
        
        lon_info = Label(frame2,text = "Longititude :",font=("goudy old style",15), bg = "white", fg = "black",padx = 5).place(x = 10, y =280)
        self.lon_info_data = Label(frame2,text = "",font=("goudy old style",15), bg = "white", fg = "black",padx = 5)
        self.lon_info_data.place(x = 160, y =280)
        
        pressure_info = Label(frame2,text = "Pressure :",font=("goudy old style",15), bg = "white", fg = "black",padx = 5).place(x = 10, y =310)
        self.pressure_info_data = Label(frame2,text = "",font=("goudy old style",15), bg = "white", fg = "black",padx = 5)
        self.pressure_info_data.place(x = 160, y =310)
        
        humidity_info = Label(frame2,text = "Humidity :",font=("goudy old style",15), bg = "white", fg = "black",padx = 5).place(x = 10, y =340)
        self.humidity_info_data = Label(frame2,text = "",font=("goudy old style",15), bg = "white", fg = "black",padx = 5)
        self.humidity_info_data.place(x = 160, y =340)
        
        wind_speed_info = Label(frame2,text = "Speed :",font=("goudy old style",15), bg = "white", fg = "black",padx = 5).place(x = 10, y =370)
        self.wind_speed_info_data = Label(frame2,text = "",font=("goudy old style",15), bg = "white", fg = "black",padx = 5)
        self.wind_speed_info_data.place(x = 160, y =370)




    def weather(self):
        try:
            if self.txt_city.get()=="":
                self.warning.config(text = "City Not Found!",fg ="dark red")
            else:
          
                city = self.var_search.get()
                api_key = "f8320bb3ad790a736afead4ff5615bc1"
                complete_url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
                result = requests.get(complete_url)
                if result:
                    json=result.json()
                    city_name = json["name"]
                    country = json["sys"]["country"]
                    temp_c = json["main"]["temp"]- 273.15
                    temp_f = (json["main"]["temp"]- 273.15) *9/5 +32
                    wind = json["weather"][0]["main"]
                    ico = json["weather"][0]["icon"]
                    descrip=json["weather"][0]["description"]
                    lat = json["coord"]["lat"]
                    lon =json["coord"]["lon"]
                    pressure =json["main"]["pressure"]
                    humidity =json["main"]["humidity"]
                    wind_speed =json["wind"]["speed"]#mph

                    self.get_img =Image.open(f"icons/{ico}.png")
                    self.get_img=self.get_img.resize((80,80),Image.ANTIALIAS)
                    self.get_img=ImageTk.PhotoImage(self.get_img)

                    self.img.config(image = self.get_img)
                    
                    self.city_info_data.config(text=city_name)
                    self.country_info_data.config(text=country)
                    self.temp_highlight.config(text = str(int(temp_c))+u"\N{DEGREE SIGN}"+"c")
                    self.temp_c_info_data.config(text = str(int(temp_c))+u"\N{DEGREE SIGN}"+"C")
                    self.temp_f_info_data.config(text = str(int(temp_f))+u"\N{DEGREE SIGN}"+"F")
                    self.weather_highlight.config(text = wind)
                    self.descrip_info_data.config(text = descrip.upper())
                    self.lat_info_data.config(text = lat)
                    self.lon_info_data.config(text = lon)
                    self.pressure_info_data.config(text=str(pressure)+" Atm")
                    self.warning.config(text="Data Found",fg="dark green")
                    self.humidity_info_data.config(text=humidity)
                    self.wind_speed_info_data.config(text = str(wind_speed)+" Mph")


                    self.txt_city.delete(0, END)
                    self.txt_city.config(fg = "light grey")
                    self.txt_city.insert(0,"\t        City Name")
                    self.btn_search.focus_set()
                
                else:
                    self.warning.config(text="Invalid City!")
        except Exception as e:
            self.warning.config(text="Network Error!")
            time.sleep(5)
            self.weather()
            pass
    
    def fun(self,event) :
        self.weather()           
    
    def clear_entry(self,event, entry):
        flag = 0
        self.txt_city.delete(0, END)
        self.txt_city.config({"foreground": "black"})
        self.txt_city.unbind("<Key>", flag)



root = Tk()
obj=MyWeather(root)
root.mainloop()