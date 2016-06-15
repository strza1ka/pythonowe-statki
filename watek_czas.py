#wątek liczący sekundy

from threading import Thread
from time import sleep
sekundy=0
minuty=0
def Timer():
    while True:
        sleep(1)
        global sekundy
        global minuty
        sekundy=sekundy+1
        if sekundy ==60:
            sekundy =0
            minuty=minusty+1

def PrintTime():
    if sekundy<10:
        sekundyString = "0" + str(sekundy)
    print("[",minuty,":",sekundyString,"] ",sep="",end="")
  
if(__name__ == '__main__'):
    t = Thread(target=Timer,
    args=())
    t.start()
    PrintTime()
    print("Wątek uruchomiony !")
    PrintTime()
    data = input("napisz coś:")
    PrintTime()


