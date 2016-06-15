from pickle import loads, dumps
from socket import *
import pygame
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
statki = [[0, 0, 0, 0, 0, 0, 0, 3, 0, 0], [0, 0, 0, 0, 0, 0, 0, 3, 0, 0], [0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 2, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 4, 4, 4, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]
statki2=tab[2]

def Serializuj(tb):
    return dumps(tb)
    
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
        print("Niestety, przegrałeś.")
        break
    elif mojaTura == '1':
        #strzelaj
        # inicjalizacja pygame
        pygame.init()
 
# wielkość ekranu
        WINDOW_SIZE = [536, 255]
        screen = pygame.display.set_mode(WINDOW_SIZE)
 
# tytuł
        pygame.display.set_caption("Statki")
 
# pętla do momentu zamknięcia programu
        done = False
        while not done:
            for event in pygame.event.get():  # zdarzenie
                if event.type == pygame.QUIT:  # 
                    done = True  # 
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # odczytywanie pozycji po kliknięciu
                    pos = pygame.mouse.get_pos()
                    # zamiana współrzędnych na współrzędne plansz
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    statki2[row][column-11] = 1
                    data = "%s%s" %(int(row), int(column-11))
        #wyslij wiadomość do serwera
                    sock.sendto(data.encode('utf-8'), (group_addr, port))
        #oczekuj na odp.
                    mojaTura = sock.recv(4096).decode('utf-8')
                    tab=loads(sock.recv(4096))
                    print(tab)
                    pygame.display.flip()
         
            # kolor tła
            screen.fill(BLACK)
         
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
                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])
            for row in range(10):
                for column in range(10):
                    color = WHITE
                    if statki2[row][column] == 1:
                        color = BLUE
                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN + 270,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])
        # wyświetlenie narysowanej planszy
            pygame.display.flip()
        mojaTura = sock.recv(4096).decode('utf-8')
        tab=loads(sock.recv(4096))
        print(tab)
        pygame.display.flip()
    else:
        #czekaj
        print('Ruch przeciwnika, czekaj...')
        #oczekuj na odp.
        mojaTura = sock.recv(4096).decode('utf-8')
        tab=loads(sock.recv(4096))
        print(tab)
sock.close()
pygame.quit()

