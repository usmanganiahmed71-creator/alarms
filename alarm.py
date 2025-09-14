import time
import datetime
import pygame
import threading
def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    alarm="song.mp3"
    while True:
        tyme = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
        print(tyme)
        if tyme==alarm_time:
            print("TIME UPP")
            pygame.mixer.init()
            pygame.mixer.music.load(alarm)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
                if input("STOP to stop:")=="STOP":
                    break
                else:
                    print("RETRY")
            break

if __name__=="__main__":
    tyme=datetime.datetime.now()
    print(tyme)
    inp=input("in format HH:MM:SS")
    set_alarm(inp)