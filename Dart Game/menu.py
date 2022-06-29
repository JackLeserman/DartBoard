from glob import glob
import re
from tkinter import *
from tkinter.font import BOLD, Font
from turtle import clear
import  cv2 as cv
import os

window = Tk()
ready = IntVar()
window.attributes('-fullscreen', True)
window.resizable(5,10)
camera = cv.VideoCapture(0)

player_name_list = []
counter_player_tracker = 0

def num_players_entry(num_players):
    clearFrame(window)
    for i in range(int(num_players)):
        player_name_photo(int(num_players))
        clearFrame(window)
        print("E")
        
    print("DONE")
    confirm_players()

def convert_player_list_to_text(list):
    names = ""
    for name in list:
        names = names + name + ","
    return names


def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def get_name_and_add(name,num_players):
    player_name_list.append(name)
    print(name)
    ready.set(ready.get())
    
def confirm_players():
    clearFrame(window)
    players_title = Label(window, text="Confirm Players", font=Font(family='Helvetica', size=30, weight='bold'))
    players_title.grid(column=2, row =1)

    players = Label(window, text=convert_player_list_to_text(player_name_list), font=Font(family='Helvetica', size=20))
    players.grid(column=2, row =2)

    yes_button = Button(window,text="Yes",command = lambda: clearFrame(window), font=Font(family='Helvetica', size=15, weight='bold'))
    yes_button.grid(column=2,row=5)
    no_button = Button(window,text="No",command = lambda: main_menu(), font=Font(family='Helvetica', size=15, weight='bold'))
    no_button.grid(column=2,row=6)





def player_name_photo(num_players):
    players_title = Label(window, text="Name Each Player", font=Font(family='Helvetica', size=30))
    players_title.grid(column=2, row =1)
    
    player_name = StringVar()
    name_entry= Entry(window, textvariable = player_name,font=Font(family='Helvetica', size=30))
    name_entry.grid(column=2, row =2)

    #enter_button = Button(window,text="Take Photo",command = takePhoto, font=Font(family='Helvetica', size=30, weight='bold'))
    #enter_button.grid(column=2,row=5)

    players_title = Label(window, text="Players So Far...", font=Font(family='Helvetica', size=20, weight='bold'))
    players_title.grid(column=2, row =7)
    player_names = Label(window, text=convert_player_list_to_text(player_name_list), font=Font(family='Helvetica', size=12))
    player_names.grid(column=2, row =8)

    enter_button = Button(window,text="Continue",command = lambda: get_name_and_add(name_entry.get(),num_players), font=Font(family='Helvetica', size=30, weight='bold'))
    enter_button.grid(column=2,row=5)
    enter_button.wait_variable(ready)
    
    
    




########### HOME SCREEN -- SELECT NUMBER PLAYERS ##################
def main_menu():    
    clearFrame(window)
    window.title("Menu")
    welcome_title = Label(window, text="Dart Time", font=Font(family='Helvetica', size=40, weight='bold'))
    players_title = Label(window, text="Select Number of Players", font=Font(family='Helvetica', size=30))
    welcome_title.grid(column=2, row =1)
    players_title.grid(column=2, row=2)

    spin = Spinbox(window, from_=0, to=99, width=3, font=Font(family='Helvetica', size=36, weight='bold'))
    spin.grid(column=2,row=3)

    enter_button = Button(window,text="Continue",command = lambda: num_players_entry(spin.get()), font=Font(family='Helvetica', size=30, weight='bold'))
    enter_button.grid(column=2,row=5)

main_menu()
window.mainloop()