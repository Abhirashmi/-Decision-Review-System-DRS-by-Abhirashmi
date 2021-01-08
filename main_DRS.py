import tkinter
import cv2 #pipinstall opencv-python
import PIL.Image, PIL.ImageTk  #pip install pillow
from functools import partial #to give an argument without showing
import threading #we use thread to be safe from the blocking nature of the program
import imutils # pip install imutils
import random
import time
import pygame
pygame.init()

# we can also use opencv video capture function and connect our pc through ip camera so we can get live videos and accordingly get our decisions conveyed by our drs system
SOUNDS=pygame.mixer.Sound('sound.mp3')

stream=cv2.VideoCapture("drs_video.mp4")
flag=True
def play_button(speed):
    global flag
    # play function helps us to give commands to the clip we have right now ,commands like slow preivious , fast previous , slow next , fast next

    print(f"you clicked on play.And speed is {speed}")

    # playing the video in reverse mode (previous button) when the value of speed is negative or playing the clip in forward mode when the speed is positive
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)#cap_prop sets the frame number you want to read
    stream.set(cv2.CAP_PROP_POS_FRAMES , frame1+speed)

    grabbed , frame=stream.read()
    if not grabbed:
        exit()
    frame=imutils.resize(frame, width=SET_WIDTH,  height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame))
    canvas.image= frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    if flag:
        canvas.create_text(290,60,fill="red",font="Times 30 bold",text="     DECISION PENDING !!!")
    flag =not flag







#setting width and height of the main screen
SET_WIDTH = 600
SET_HEIGHT = 368


def pending(decision):
    #1. firstly display decision pending image
    frame = cv2.cvtColor(cv2.imread("desicion pending.jpeg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height= SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    #2. wait for few moments or seconds
    r=random.randint(3,8)
    time.sleep(r)
    #3. display the sponser image

    frame = cv2.cvtColor(cv2.imread("sponsers1.jpeg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    time.sleep(r)

    frame = cv2.cvtColor(cv2.imread("sponsers2.jpeg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    time.sleep(r)


    frame = cv2.cvtColor(cv2.imread("sponsers3.jpeg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    time.sleep(r)

    frame = cv2.cvtColor(cv2.imread("decisionpending2.jpeg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    time.sleep(r)


    #4. wait for few moments again for building suspense!!
    time.sleep(r)

    #5. display out when out or display the not out image when not out
    if decision == "out":
        frame = cv2.cvtColor(cv2.imread("out.jpg"), cv2.COLOR_BGR2RGB)

    else:
        frame = cv2.cvtColor(cv2.imread("not out.jpeg"), cv2.COLOR_BGR2RGB)

    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)


def out():
    # this function runs when the 3rd umpire clicks on out button ; when the player is out
    thread= threading.Thread(target=pending,args=("out",))
    thread.daemon = 1
    thread.start()
    print("player is out!!")

def not_out():
    # this function runs when the 3rd umpire clicks on  not out button ; when the player is not out
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("player is not out !!")

#tkinter gui starts here
'''
A GUI (graphical user interface) is a system of interactive visual components for computer software.
 A GUI displays objects that convey information, and represent actions that can be taken by the user.
The objects change color, size, or visibility when the user interacts with them.
'''
window = tkinter.Tk()
window.title("Abhirashmi_3rd_umpire_ Decision Review System (DRS)_kit")

cv_img=cv2.cvtColor(cv2.imread("welcome.png"),cv2.COLOR_BGR2RGB)

canvas = tkinter.Canvas(window,width=SET_WIDTH , height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0 , 0 , ancho= tkinter.NW ,image = photo)
canvas.pack()
SOUNDS.play()
SOUNDS.play()


#buttons to control playback
btn=tkinter.Button(window,text="<<<< Previous (fast)", width=60 ,command =partial(play_button,-30))
btn.pack()

btn=tkinter.Button(window,text="<< Previous (slow)", width=60 ,command =partial(play_button,-5))
btn.pack()

btn=tkinter.Button(window,text=" Next (fast) >>>>", width=60 ,command = partial(play_button,30))
btn.pack()

btn=tkinter.Button(window,text=" Next (slow) >>", width=60 ,command =partial(play_button,5))
btn.pack()


btn=tkinter.Button(window,text=" GIVE OUT !!", width=60 ,command = out)
btn.pack()

btn=tkinter.Button(window,text=" GIVE NOT OUT !!", width=60 ,command =not_out)
btn.pack()

window.mainloop()


