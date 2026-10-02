# EXERCISE - 7  --> Healthy Programmer
# Fitness reminder program to Programmer

# 9am to 5pm

# Water - water.mp3  (3.5 litres)
"""  have to remind the programmer to drink water and this reminder will stop only when prog. type Drank and enter, also have to make a file to
 log the time stamp of the water drinked.  """

# Eyes - eyes.mp3
""" In every 30 minutes it will remind for eye exercise and will stop on writng EyDone  , log file. """

# Physical Activity - physical.mp3
""" Every 45 min.  ExDone , log file. """

""" Alarm will only stop when user will type exit option. """

# NOTE :
# Pygame module is used to play the audio


# starting the solution of exercise-7

import time
list_eye = ["9:30:00", "10:00:00", "10:30:00", "11:00:00", "11:30:00", "12:00:00", "12:30:00", "13:00:00", "13:30:00", "14:00:00", "14:30:00", "15:00:00", "15:30:00", "16:00:00", "16:30:00", "17:00:00"]
list_phy = ["9:45:00", "10:30:00", "11:15:00", "12:00:00", "12:45:00", "13:30:00", "14:15:00", "15:00:00", "15:45:00", "16:30:00"]
list_water = ["9:33:00", "10:06:00", "10:39:00", "11:12:00", "11:45:00", "12:18:00", "12:5`:00", "13:24:00", "13:57:00", "14:30:00", "15:03:00", "15:36:00", "16:09:00", "16:42:00"]
# f = open("healthy_programmer.txt", "rt")

import datetime
from pygame import mixer
mixer.init()
# mixer.music.load("physical.mp3")
# mixer.music.load("eyes.mp3")
# mixer.music.set_volume(0.7)
# mixer.music.play()

# while True:
#     print("Press 'p' to pause, 'r' to resume")
#     print("Press 'e' to exit the program")
#     query = input("  ")
#
#     if query == 'p':
#         # Pausing the music
#         mixer.music.pause()
#
#     elif query == 'r':
#         # Resuming the music
#         mixer.music.unpause()
#
#     elif query == 'e':
#         # Stop the mixer
#         mixer.music.stop()
#
#         break

try:
    def physical():
        mixer.music.load("physical.mp3")
        mixer.music.play(loops=-1)
        query = input("Write \'ExDone\' to exit the program")
        if query == "ExDone":
            mixer.music.stop()
        print("Log your progress: ")
        f = open("healthy_programmer.txt", "a")
        progress = input("Write your progress: \n")
        log_time = datetime.datetime.now()
        f.write(str(log_time) + "-->" + progress + "\n\n")
        f.close()

    def eyes():
        mixer.music.load("eyes.mp3")
        mixer.music.play(loops=-1)
        print("Press \'EyDone\' to exit the program")
        query = input()
        if query == "EyDone":
            mixer.music.stop()
        print("Log your progress: ")
        f = open("healthy_programmer.txt", "a")
        progress = input()
        log_time = datetime.datetime.now()
        f.write(str(log_time) + "-->" + progress + "\n\n")
        f.close()

    def water():
        mixer.music.load("drink_water.mp3")
        mixer.music.play(loops=-1)
        print("Write \'Drinked\' to exit the program")
        query = input()
        if query == "Drinked":
            mixer.music.stop()
        print("Log your progress: ")
        f = open("healthy_programmer.txt", "a")
        progress = input()
        log_time = datetime.datetime.now()
        f.write(str(log_time) + "-->" + progress + "\n\n")
        f.close()
        print("Your progress is logged into a file. \n")

except KeyboardInterrupt as ki:
    print(ki)
    print("You are out of your working Time")


# below is the logic that calls the particular function at the required time.
while True:
    if time.strftime("%H:%M:%S") in list_eye:
        eyes()
    if time.strftime("%H:%M:%S") in list_phy:
        physical()
    if time.strftime("%H:%M:%S") in list_water:
        water()
    if time.strftime("%H:%M:%S") == "17:00:01":
        print("Your Working time is Finished")
        break


# make the program by the time difference.
