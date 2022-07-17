from glob import glob
import re
from tkinter import *
from tkinter.font import BOLD, Font
from turtle import clear
import  cv2 as cv
import os
import random as random

window = Tk()
ready = IntVar()
window.attributes('-fullscreen', True)
window.resizable(5,10)
camera = cv.VideoCapture(0)

player_name_list = []
player_scores = []
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

    yes_button = Button(window,text="Yes",command = lambda: select_game(), font=Font(family='Helvetica', size=15, weight='bold'))
    yes_button.grid(column=2,row=5)
    no_button = Button(window,text="No",command = lambda: main_menu(), font=Font(family='Helvetica', size=15, weight='bold'))
    no_button.grid(column=2,row=6)

def select_game():
    clearFrame(window)
    players_title = Label(window, text="Select Game Mode", font=Font(family='Helvetica', size=30, weight='bold'))
    players_title.grid(column=2, row =1)
    dem_button = Button(window,text="Demolition",command = lambda: demolition(), font=Font(family='Helvetica', size=15, weight='bold'))
    dem_button.grid(column=1,row=2)
    quack_button = Button(window,text="Quack",command = lambda: main_menu(), font=Font(family='Helvetica', size=15, weight='bold'))
    quack_button.grid(column=2,row=2)
    killer_button = Button(window,text="Killer",command = lambda: main_menu(), font=Font(family='Helvetica', size=15, weight='bold'))
    killer_button.grid(column=3,row=2)





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

    enter_button = Button(window,text="Add Player",command = lambda: get_name_and_add(name_entry.get(),num_players), font=Font(family='Helvetica', size=30, weight='bold'))
    enter_button.grid(column=2,row=5)
    enter_button.wait_variable(ready)

def initalize_score(num):
    for i in range(len(player_name_list)):
        player_scores.append(num)

def getScore():
    text = ""
    bullet = " • "
    for i in range(len(player_name_list)):
        name = player_name_list[i]
        score = player_scores[i]
        text = text + name + ": " + str(score)
        if(i != (len(player_name_list)-1)):
            text = text + bullet
    return text


def scoreboard_dem(window, players):
    scoreboard = Label(window, text= getScore(), font=Font(family='Helvetica', size=14, weight='bold'))
    scoreboard.grid(column=2, row=3)

def game_navbar():
    MSA_button = Button(window,text="Manual Score Adjust",command = lambda: num_players_entry(spin.get()), font=Font(family='Helvetica', size=10))
    MSA_button.grid(column=1,row=9)
    home_button = Button(window,text="Quit Game",command = lambda: main_menu(), font=Font(family='Helvetica', size=10))
    home_button.grid(column=3,row=9)
    endturn_button = Button(window,text="-- END TURN --",command = lambda: main_menu(), font=Font(family='Helvetica', size=20, weight='bold'))
    endturn_button.configure(bg="red")
    endturn_button.grid(column=2,row=9)
    

def player_game_info(player, throw):
    infotext = player + "'s Turn. Throw: " + str(throw) + "/3"
    players_info = Label(window, text=infotext, font=Font(family='Helvetica', size=20, weight='bold'))
    players_info.grid(column=2, row =2)

def demolition():
    winner = False
    clearFrame(window)
    initalize_score(180)
    scoreboard_dem(window, len(player_name_list))
    game_navbar()
    player_game_info(player_name_list[1],1) #TODO REMOVE
    players_title = Label(window, text="Demolition", font=Font(family='Helvetica', size=20, weight='bold'))
    players_title.grid(column=2, row =1)


########### HOME SCREEN -- SELECT NUMBER PLAYERS ##################
def main_menu():    
    clearFrame(window)
    player_name_list.clear()
    player_scores.clear()
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

#TODO
#teams
#quitgame confirm?