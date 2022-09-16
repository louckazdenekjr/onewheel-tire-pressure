import tkinter
import sys
import os
from tkinter import ttk


def kgToLbs(weight_kg):
    return weight_kg * 2.2046226218
    
def lbsToKg(weight_lbs):
    return weight_kg / 2.2046226218

def psiToBar(pressure_psi):
    return pressure_psi / 14.503773773
    
def barToPsi(pressure_bar):
    return pressure_bar * 14.503773773

def deciRound(input):
    return round(input, 2)

def recommendPressure(weight_kg, style_factor):
    weight_lbs = kgToLbs(weight_kg)
    pressure_psi = weight_lbs / 10
    pressure_bar = psiToBar(pressure_psi)
    
    style_factor = (style_factor/2) / 10
    pressure_bar = pressure_bar + (style_factor * pressure_bar)
    
    pressure_reading_psi = deciRound(barToPsi(pressure_bar))
    pressure_reading_bar = deciRound(pressure_bar)
    
    return pressure_reading_bar, pressure_reading_psi

class mainWindow(tkinter.Tk):
    def __init__(self):
        # inherit super
        super().__init__()
        
        # Initialize style
        ttk_style = ttk.Style()
        # Create style used by default for all Frames
        ttk_style.configure('TScale', background='#2d2d2d')

        # get path to set icon file
        if getattr(sys, 'frozen', False):
            application_path = sys._MEIPASS
        elif __file__:
            application_path = os.path.dirname(__file__)
        icon_file = str ( os.path.join ( application_path, "icon.ico" ) )

        # create tk root and set window flags
        self.geometry ("300x300")
        self.title('Onewheel Tire Pressure')
        self.attributes ('-topmost', True)
        self.configure ( background = '#2d2d2d' )
        self.resizable (False, False) 
        
        # set initial values
        self.font_family = "Tahoma"
        self.font_size = 9
        self.font_color = "#1e1e1e"
        self.style_factor = 0
 
        # create widgets
        self.button_calculate = tkinter.Button(
            self,
            text = "Calculate",
            font = ( self.font_family, self.font_size ),
            background = "#2d2d2d",
            activebackground = "#1e1e1e",
            foreground = "#c8c8c8",
            activeforeground = "#c8c8c8",
            justify = tkinter.CENTER,
            command = self.calculatePressure,
            width = 10,
            height = 1
        )
        
        self.button_calculate.place(
            relx        = 0.5, 
            rely        = 0.8, 
            anchor      = tkinter.CENTER
        )
        
        self.label_weight = tkinter.Label(
            self,
            text = "Enter rider weight (kg)",
            font = ( self.font_family, self.font_size ),
            justify = tkinter.CENTER,
            #width = 15,
            background = "#2d2d2d",
            foreground = "#c8c8c8"
        )
        
        self.label_weight.place(
            relx        = 0.5, 
            rely        = 0.1, 
            anchor      = tkinter.CENTER
        )    
        
        self.entry_weight = tkinter.Entry(
            self,
            font = ( self.font_family, self.font_size ),
            justify = tkinter.CENTER,
            width = 15,
            background = "#969696"
        )
        
        self.entry_weight.place(
            relx        = 0.5, 
            rely        = 0.2, 
            anchor      = tkinter.CENTER
        )
        
        
        self.label_style = tkinter.Label(
            self,
            text = "Select riding preference",
            font = ( self.font_family, self.font_size ),
            justify = tkinter.CENTER,
            #width = 15,
            background = "#2d2d2d",
            foreground = "#c8c8c8"
        )
        
        self.label_style.place(
            relx        = 0.5, 
            rely        = 0.35, 
            anchor      = tkinter.CENTER
        )    
        
        self.label_style_2 = tkinter.Label(
            self,
            text = "-10 = tricks and extreme off-road \n0 = standard pressure \n10 = maximum range and acceleration",
            font = ( self.font_family, self.font_size ),
            justify = tkinter.CENTER,
            #width = 15,
            background = "#2d2d2d",
            foreground = "#c8c8c8"
        )
        
        self.label_style_2.place(
            relx        = 0.5, 
            rely        = 0.65, 
            anchor      = tkinter.CENTER
        )

        self.label_style_3 = tkinter.Label(
            self,
            text = "-> 0 <-",
            font = ( self.font_family, self.font_size ),
            justify = tkinter.CENTER,
            #width = 15,
            background = "#2d2d2d",
            foreground = "#c8c8c8"
        )
        
        self.label_style_3.place(
            relx        = 0.5, 
            rely        = 0.55, 
            anchor      = tkinter.CENTER
        )  
        
        self.label_result = tkinter.Label(
            self,
            text = "",
            font = ( self.font_family, self.font_size ),
            justify = tkinter.CENTER,
            #width = 15,
            background = "#2d2d2d",
            foreground = "#c8c8c8"
        )
        
        self.label_result.place(
            relx        = 0.5, 
            rely        = 0.9, 
            anchor      = tkinter.CENTER
        )    
        
        self.slider_style = ttk.Scale(
            self,
            from_ = -10,
            to = 10,
            command = self.showStyle
        )
        
        self.slider_style.place(
            relx        = 0.5, 
            rely        = 0.45, 
            anchor      = tkinter.CENTER
        )

        
        # bind events to actions
        self.bind("<<exit>>", self.stopApplication)
        
        # start event loop
        self.mainloop()

    # define calculate pressure method to calculate optimal pressure
    def calculatePressure(self):
        try:
            weight_kg = self.entry_weight.get() 
            weight_kg = int(weight_kg)
            
            pressure_bar, pressure_psi = recommendPressure(weight_kg, self.style_factor)
            
            result_string = "Optimal tire pressure: " + str(pressure_bar) + " bar (" + str(pressure_psi) + " PSI)"
            self.label_result.config(text = result_string)
        except:
            result_string = "Incorrect rider weight entered."
            self.label_result.config(text = result_string)

    # define show style method to update label and variable
    def showStyle(self, value):
        value = int(float(value))
        value_string = "-> " + str(value) + " <-"
        
        self.label_style_3.config(text = value_string)
        self.style_factor = value

    # define callable main application exit method
    def stopApplication(self, event):
        sys.exit(0)


if __name__ == "__main__":
    appWindow = mainWindow()