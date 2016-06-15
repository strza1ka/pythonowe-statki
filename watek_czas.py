#wątek liczący sekundy

from threading import Thread
from time import sleep
sekundy=0
minuty=0
def Timer():
    while True:
        sleep(1)
        global sekundy
        sekundy=sekundy+1
        
  
if(__name__ == '__main__'):
    t = Thread(target=Timer,
    args=())
    t.start()
    print("Wątek uruchomiony !")
    data = input("napisz coś:")
    print(sekundy,"sekundy")

