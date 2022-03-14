#import tkinter, pygame for mixer, and PIL for image manipulation
import tkinter as tk
from tkinter import *
import pygame
import os
from PIL import Image, ImageTk

class MusicPlayer:
  #initialize music player class
  def __init__(self, root):
    self.root = root
    #set title and size of window
    self.root.title("Music Player")
    self.root.geometry("875x280+200+200") 

    #initialize mixer for music
    pygame.init()
    pygame.mixer.init()

    self.track = StringVar()
    self.status = StringVar()

    #frame for header and logo pictures
    header_frame = LabelFrame(self.root, bg = "black", borderwidth = 0, highlightthickness = 0)
    header_frame.place(x = 0, y = 0, width = 875, height = 100)

    #adds the logo image to the top left corner
    logo = Image.open("icons/logo.png")
    #alternate text for the image
    logo.title = ("This is the logo image")
    resize_logo = logo.resize((80, 80))
    logo_img = ImageTk.PhotoImage(resize_logo)
    header_label = Label(image = logo_img, bg = "black")
    header_label.place(x = 5, y = 10)
    header_label.image = logo_img

    #adds an album image to the top right corner
    album = Image.open("icons/album.png")
    #alternate text for the image
    album.title = ("This is the title image.")
    resize_album = album.resize((80, 80))
    album_img = ImageTk.PhotoImage(resize_album)
    header_label = Label(image = album_img, bg = "black")
    header_label.place(x =780, y = 10)
    header_label.image = album_img

    #frame for currently playing song and status
    track_frame = LabelFrame(self.root, text = "Song Track", font = ("Modern",  15,  "bold"), bg = "black", fg = "white")
    track_frame.place(x = 0, y = 100, width = 475, height = 100)
    song_track = Label(track_frame, textvariable = self.track, width = 20, anchor="w", font = ("Modern", 24, "bold"), bg = "black", fg = "pink").grid(row = 0, column = 0, padx = 0, pady = 0)
    track_status = Label(track_frame, textvariable = self.status, font = ("Modern", 24, "bold"), bg = "black", fg = "pink").grid(row = 0, column = 1, padx = 0, pady = 0)

    #frame for button controls
    button_frame = LabelFrame(self.root, text = "Controls", font = ("Modern", 15, "bold"), bg = "black", fg = "white")
    button_frame.place(x = 0, y = 200, width = 475, height = 75)
    
    play_button = Button(button_frame, text = "PLAY", command = self.play_song, width = 4, height = 1, font = ("Modern", 16, "bold"), fg = "black", bg = "gold").grid(row = 0, column = 0, padx = 2, pady = 5)
    pause_button = Button(button_frame, text = "PAUSE", command = self.pause_song, width = 4, height = 1, font = ("Modern", 16, "bold"), fg = "black", bg = "gold").grid(row = 0, column = 1, padx = 2, pady = 5)
    songs_button = Button(button_frame, text = "ABOUT", command = self.about_window, width = 4, height = 1, font = ("Modern", 16, "bold"), fg = "black", bg = "gold").grid(row = 0, column = 2, padx = 2, pady = 5)
    exit_button = Button(button_frame, text= "EXIT", command = root.destroy, width = 4, height = 1, font = ("Modern", 16, "bold"), fg = "black", bg = "gold").grid(row = 0, column = 3, padx = 2, pady = 5)
    
    #frame for listing playlist of songs that comes from folder
    songs_frame = LabelFrame(self.root, text = "Playlist", font = ("Modern", 15, "bold"), bg = "black", fg = "white")
    songs_frame.place(x = 475, y = 100, width = 400, height = 175)
    scroll_y = Scrollbar(songs_frame, orient = VERTICAL)
    self.playlist = Listbox(songs_frame, yscrollcommand = scroll_y.set, selectbackground = "black", selectmode = SINGLE, font = ("Modern", 16, "bold"), bg = "black", fg = "pink")
    scroll_y.pack(side = RIGHT, fill = Y)
    scroll_y.config(command = self.playlist.yview)
    self.playlist.pack(fill = BOTH)
    os.chdir("music/")
    songtracks = os.listdir()
    for track in songtracks:
      self.playlist.insert(END, track)

  #plays the selected song in the list
  def play_song(self):
    self.track.set(self.playlist.get(ACTIVE))
    self.status.set("- Playing")
    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    pygame.mixer.music.play()

  #pauses the currently playing song
  def pause_song(self):
    self.status.set("- Paused")
    pygame.mixer.music.pause()
  
  #the about page for the music player that opens in a new window
  def about_window(self):
    about_win = Toplevel()
    about_win.geometry("400x100")
    description1 = Label(about_win, text = "This is a music player with songs loaded from a folder.")
    description2 = Label(about_win, text = "Select a song from the list and press play.")
    description1.pack()
    description2.pack()

#runs the music player
root = tk.Tk()
MusicPlayer(root)
root.mainloop()