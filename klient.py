from pickle import loads, dumps
from socket import *
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
WINDOW_SIZE = [536, 400]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# tytuł
pygame.display.set_caption("Statki v.1")

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
statki2=tab[0]

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


# Multicast group parameters
group_addr = "localhost"
port = 2223
# Stworzenie socketa
sock = socket(AF_INET, SOCK_DGRAM)
# Opcje socketa
sock.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, 32)
sock.setsockopt(IPPROTO_IP, IP_MULTICAST_LOOP, 1)
# Gra
print("Wysyłam tablicę twoich statków na serwer...")
sock.sendto(Serializuj(statki), (group_addr, port))
print("Wysłano!")
mojaTura = sock.recv(4096).decode('utf-8')

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

while True:
    if mojaTura == '3':
        print("Wszystkie miejsca zajęte, niestety nie zagrasz")
        break
    elif mojaTura == '2':
        print("Gratulacje! Wygrałeś!")
        break
    elif mojaTura == '-2':
        przegrana = "Niestety, przegrałeś."
        print("Niestety, przegrałeś.")
        break
    elif mojaTura == '1':
        # inicjalizacja pygame
        #pygame.init()
##        font = pygame.font.SysFont("arial", 16)
##        text = font.render("%s" %(), True, (0, 128, 0))
# wielkość ekranu
##        WINDOW_SIZE = [536, 500]
##        screen = pygame.display.set_mode(WINDOW_SIZE)
## 
### tytuł
##        pygame.display.set_caption("Statki")
 
# pętla do momentu zamknięcia programu
        done = False
        while not done:
            for event in pygame.event.get():  # zdarzenie
                if event.type == pygame.QUIT:  #
                    pygame.quit()
                    done = True  #
                    ##poinformować drugiego gracza, że wygrał
                    sock.close()
                    exit()                   
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # odczytywanie pozycji po kliknięciu
                    pos = pygame.mouse.get_pos()
                    # zamiana współrzędnych na współrzędne plansz
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    #statki2[row][column-11] = 1
                    data = "%s%s" %(int(row), int(column-11))
        #wyslij wiadomość do serwera
                    sock.sendto(data.encode('utf-8'), (group_addr, port))
        #oczekuj na odp.
                    mojaTura = sock.recv(4096).decode('utf-8')
                    tab=loads(sock.recv(4096))
                    #print(tab_wy)
                    #cos = Wypisz(tab,1)
                    #print (cos)
                    #magazyn.append(Wypisz(tab,1))
                    #print(magazyn)
                    tablica=Wypisz(tab,3)
                    tablica = ConvertTable(tablica)
                    tablica2 = Wypisz(tab,1)
                    tablica2 = ConvertTable(tablica2)
##                    tablica2=Wypisz(tab,0)
##                    tablica2= ConvertTable(tablica2)
                    #print(tablica2)
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
                    
##                    elif Wypisz(tab,1)[row,column-11] == x:
##
##                    elif Wypisz(tab,1)[row,column-11] == X:

##                    else:
##                        print ("nico")
##                    #print(tab)
##                    pygame.display.flip()
##                    statki2[row][column-11] = 1
##                    if column >=10:
##                        print("Click ", pos, "Koordynaty: ", row, column-11)
##                    else:
##                        print("Click ", pos, "Koordynaty: ", row, column)
         
            if mojaTura == "1":
                font = pygame.font.SysFont("arial", 16)
                text = font.render("%s" %("Twój ruch"), True, (0, 255, 0))
            else:
                font = pygame.font.SysFont("arial", 16)
                text = font.render("%s" %("Ruch przeciwnika"), True, (0, 255, 0))
            screen.fill(BLACK)
            screen.blit(text,(10,300))        
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

##        data = (row, column-11)
##        #wyslij wiadomość do serwera
##        sock.sendto(data.encode('utf-8'), (group_addr, port))
##        #oczekuj na odp.
        mojaTura = sock.recv(4096).decode('utf-8')
        tab=loads(sock.recv(4096))
        #Wypisz(tab,1)
        #print(tab)
        pygame.display.flip()

    else:
        #czekaj
        print('Ruch przeciwnika, czekaj...')
        #oczekuj na odp.
        mojaTura = sock.recv(4096).decode('utf-8')
        tab=loads(sock.recv(4096))
        pygame.display.flip()
        #Wypisz(tab,1)
        #print(tab)
sock.close()
 
# zamknięcie pygame
pygame.quit()
