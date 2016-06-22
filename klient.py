from pickle import loads, dumps
from socket import *
import pygame
from pygame.locals import *
from sys import exit
from threading import Thread
from time import sleep


# kolory
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# wielkość komórki
WIDTH = 20
HEIGHT = 20
 
# oddzielenie komórek
MARGIN = 5

#wielkość okna
WINDOW_SIZE = [536, 400]


sekundy = 0
minuty = 0

tab = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
       [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
       [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
       [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]
statki = [[0, 0, 0, 1, 0, 0, 0, 4, 0, 0], [0, 0, 0, 0, 0, 0, 0, 4, 0, 0], [0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 2, 2, 0, 0, 0, 0, 4, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 3, 3, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]
statki2 = tab[0]

mojaTura = -15

def OdbierzSygnal():
    while True:
        global mojaTura
        global sock
        mojaTura = sock.recv(4096).decode('utf-8')
        print(GameTime() + "odebrano pierwszą wiad: ", mojaTura)
        tab=loads(sock.recv(4096))
        print("odebrano statki")
        global tablica
        tablica = Wypisz(tab,3)
        tablica = ConvertTable(tablica)
        print(tablica)
        global tablica2
        tablica2 = Wypisz(tab,1)
        tablica2 = ConvertTable(tablica2)
        print(tablica2)
        for row in range(10):
                       # magazyn.append([])
            for column in range(10):
               # magazyn[row].append(0)
                if tablica[row][column]== 'o':
                    statki2[row][column]=5
                    #color = Blue
                elif tablica[row][column]=='x':
                    statki2[row][column]=6
                    #color= Red
                elif tablica[row][column] == 'X':
                    statki2[row][column]=7
                    #color=Black
                elif tablica2[row][column]=='o':
                    statki[row][column]=5
                    #color= Red
                elif tablica2[row][column] == 'x':
                    statki[row][column]=6
                    #color=Black
                elif tablica2[row][column]=='X':
                    statki[row][column]=7
                    #color= Red
                else:
                    statki2[row][column]=8
                    #color=White
                pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN + 270,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            # wyświetlenie narysowanej planszy
            pygame.display.flip()
        
    


#odmierza czas
def Timer():
    global sekundy
    global minuty
    while True:
        sleep(1)
        sekundy = sekundy+1
        if sekundy == 60:
            sekundy = 0
            minuty = minuty+1

#zwraca string z czasem gry
def GameTime():
    global sekundy
    global minuty
    if sekundy < 10:sekundyString = "0" + str(sekundy)
    else: sekundyString = sekundy
    return  str(minuty) + ":" + str(sekundyString)

def Serializuj(tb):
    return dumps(tb)

def Wypisz(tb, n):
    if n%2==1:
        tablica = []
        for x in range(10):
            for y in range(10):
                if tb[n][x][y]==0:
                    tablica.append("?")
                elif tb[n][x][y]==1:
                    tablica.append("x")
                elif tb[n][x][y]==2:
                    tablica.append("X")
                elif tb[n][x][y]==3:
                    tablica.append("o")
    else:
        print(tablica)
    return tablica

def ConvertTable(tab):
    tmp=[]
    newTab=[]
    k=0
    for i in range(10):
        for j in range(10):
            tmp.append(tab[k])
            k+=1
        newTab.append(tmp)
        tmp=[]
    return newTab





## --- SOCKET ---
# Multicast group parameters
group_addr = "localhost"
port = 2223
# Stworzenie socketa
sock = socket(AF_INET, SOCK_DGRAM)
# Opcje socketa
sock.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, 32)
sock.setsockopt(IPPROTO_IP, IP_MULTICAST_LOOP, 1)


## --- GRA ----
stoper = Thread(target=Timer,args=())
stoper.start()

pygame.init()
pygame.display.set_caption("Statki v.1")
screen = pygame.display.set_mode(WINDOW_SIZE)

## -- dołącz do gry, wyślij wiadomość do serwera --
sock.sendto("poke".encode('utf-8'), (group_addr, port))
mojeStatki = loads(sock.recv(4096))
print("Otrzymałem tablicę twoim statków z serwera")
print(mojeStatki)
## zaimplementować - podmienić :D
## ....
mojaTura = sock.recv(4096).decode('utf-8')
if mojaTura == '3': print("Wszystkie miejsca zajęte, niestety nie zagrasz")
OdbierajSyngaly = Thread(target=OdbierzSygnal,args=())
OdbierajSyngaly.start()


for row in range(10):
    # dodanie rzędów
    statki.append([])
    for column in range(10):
        statki[row].append(0)  # dodanie kolumn (komórek)
        
for row in range(10):
    # dodanie rzędów
    statki2.append([])
    for column in range(10):
        statki2[row].append(0)  # dodanie kolumn (komórek)

font = pygame.font.SysFont("arial", 16)
# pętla programu
done = False
while not done:
    for event in pygame.event.get():  # zdarzenie
        if event.type == pygame.QUIT:  
            pygame.quit()
            done = True
            ## ---------------- poinformować drugiego gracza, że wygrał ----------------
            ## ...
            ## ...
            ## ...
            sock.close()
            exit()                   
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mojaTura=='1':
                # odczytywanie pozycji po kliknięciu
                pos = pygame.mouse.get_pos()
                # zamiana współrzędnych na współrzędne plansz
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                #statki2[row][column-11] = 1
                data = "%s%s" %(int(row), int(column-11))
                #wyslij wiadomość do serwera
                sock.sendto(data.encode('utf-8'), (group_addr, port))
                
    timeTextBox = font.render("czas gry: " + GameTime(), True, (0, 255, 0))
    if mojaTura=='-1':
        text = font.render("Ruch wykonuje przeciwnik", True, (0, 255, 0))
    elif mojaTura=='1': 
        text = font.render("Twoja kolej - strzelaj", True, (0, 255, 0))
    elif mojaTura == '2':
        text = font.render("WYGRAŁEŚ", True, (0, 255, 0))
        break
    elif mojaTura == '-2':
        text = font.render("PRZEGRAŁEŚ", True, (0, 255, 0))
        break    
        
    screen.fill(BLACK)
    screen.blit(text,(10,300))
    screen.blit(timeTextBox,(10,330))
    
    # plansza - rysowanie
    for row in range(10):
        for column in range(10):
            color = WHITE
            if statki[row][column] == 1:
                color = GREEN
            if statki[row][column] == 2:
                color = GREEN
            if statki[row][column] == 3:
                color = GREEN
            if statki[row][column] == 4:
                color = GREEN
            if statki[row][column] == 5:
                color = BLUE
            if statki[row][column] == 6:
                color = RED
            if statki[row][column] == 7:
                color = BLACK
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    for row in range(10):
        for column in range(10):
            color = WHITE
            if statki2[row][column] == 5:
                color = BLUE
            if statki2[row][column] == 6:
                color = RED
            if statki2[row][column] == 7:
                color = BLACK
            if statki2[row][column] == 8:
                color = WHITE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN + 270,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    # wyświetlenie narysowanej planszy
    pygame.display.flip()


sock.close()
pygame.quit()
