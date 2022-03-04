from tkinter import *
import pygame
import os

class MusicPlayer:

  def __init__(self, root):
    self.root = root
    self.root.title("Music Player")
    self.root.geometry("875x175+200+200")
    pygame.init()
    pygame.mixer.init()
    self.track = StringVar()
    self.status = StringVar()

    trackframe = LabelFrame(self.root, text = "Song Track", font = ("Modern",  15,  "bold"), bg = "grey", fg = "white")
    trackframe.place(x = 0, y = 0, width = 475, height = 100)
    songtrack = Label(trackframe, textvariable = self.track, width = 20, font = ("Modern", 24, "bold"), bg = "grey", fg = "pink").grid(row = 0, column = 0, padx = 10, pady = 5)
    trackstatus = Label(trackframe, textvariable = self.status, font = ("Modern", 24, "bold"), bg = "grey", fg = "pink").grid(row = 0, column = 1, padx = 10, pady = 5)

    buttonframe = LabelFrame(self.root, text = "Controls", font = ("Modern", 15, "bold"), bg = "grey", fg = "white")
    buttonframe.place(x = 0, y = 100, width = 475, height = 75)
    playbtn = Button(buttonframe, text = "PLAY", command = self.playsong, width = 6, height = 1, font = ("Modern", 16, "bold"), fg = "navyblue", bg = "gold").grid(row = 0, column = 0, padx = 10, pady = 5)
    playbtn = Button(buttonframe, text = "PAUSE", command = self.pausesong, width = 8, height = 1, font = ("Modern", 16, "bold"), fg = "navyblue", bg = "gold").grid(row = 0, column = 1, padx = 10, pady = 5)

    songsframe = LabelFrame(self.root, text = "Playlist", font = ("Modern", 15, "bold"), bg = "grey", fg = "white")
    songsframe.place(x = 475, y = 0, width = 400, height = 175)
    scrol_y = Scrollbar(songsframe, orient = VERTICAL)
    self.playlist = Listbox(songsframe, yscrollcommand = scrol_y.set, selectbackground = "black", selectmode = SINGLE, font = ("Modern", 12, "bold"), bg = "silver", fg = "navyblue")
    scrol_y.pack(side = RIGHT, fill = Y)
    scrol_y.config(command = self.playlist.yview)
    self.playlist.pack(fill = BOTH)
    os.chdir("music/")
    songtracks = os.listdir()
    for track in songtracks:
      self.playlist.insert(END, track)

  def playsong(self):
    self.track.set(self.playlist.get(ACTIVE))
    self.status.set("- Playing")
    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    pygame.mixer.music.play()

  def pausesong(self):
    self.status.set("- Paused")
    pygame.mixer.music.pause()

root = Tk()
MusicPlayer(root)
root.mainloop()