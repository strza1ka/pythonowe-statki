from pickle import loads, dumps
from datetime import datetime
from socketserver import BaseRequestHandler, UDPServer
from random import randrange
from sys import exit
from random import randint
import pygame

#zaimplementowane tablice do losowania
maps = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 3, 3, 3, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 4, 4, 4, 4]],

        [[0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
         [0, 0, 0, 0, 2, 2, 0, 0, 4, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 3, 3, 3, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [3, 3, 3, 0, 0, 2, 2, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 4, 0, 0, 0]],

        [[0, 4, 4, 4, 4, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 3, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

        [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 4, 0, 3, 0, 0, 0, 0, 0],
         [0, 0, 4, 0, 3, 0, 0, 0, 0, 0],
         [0, 0, 4, 0, 3, 0, 0, 0, 0, 0]],

        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 4, 4, 4, 4, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [3, 3, 3, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 2, 2, 0, 0, 0, 0]],
        
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 3, 3, 3, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 4, 0, 0, 0, 0, 0, 1, 0]],

        [[0, 0, 0, 0, 4, 4, 4, 4, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [3, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 2, 0, 0, 0, 0, 0, 0, 0, 0]],

        [[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 4, 4, 4, 4, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
         [0, 0, 3, 3, 3, 0, 0, 0, 2, 0]]]

#tablica przechowująca informacje o rozgrywce
tab = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
       
       [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
       
       [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
       
       [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]

clients = []
licznik = [0,0]
liczbaStatkow = 4

  
def Time():
    time = datetime.now()
    if time.second < 10: return str(time.hour)+":"+str(time.minute)+":0"+str(time.second)+" "
    else: return str(time.hour)+":"+str(time.minute)+":"+str(time.second)+" "

class MyUDPHandler(BaseRequestHandler):
    def handle(self):
        global licznik
        global tab
        global liczbaStatkow
        global clients
        # -- dodaj clienta, jeśli nie jest w bazie i baza < 2 osoby --
        socket = self.request[1]
        if self.client_address not in clients and len(clients)<2:
            clients.append(self.client_address)
            # - prześlij akceptację - 
            socket.sendto(dumps("yes"), self.client_address)
            # - losuj i wyślij statki graczowi - 
            global statki
            print(Time(), self.request[0].decode("utf-8"))
            los = randint(0,8)
            print(Time(), "Wylosowano mapę: ", maps[los])
            statki = maps[los]
            socket.sendto(Serializuj(statki), self.client_address)

            # - gracz, który pierwszy się dołączył, drugi zaczyna -
            if len(clients) == 1:
                tab[0] = statki
                socket.sendto(str(-1).encode('utf-8'), clients[0])
            else:
                tab[2] = statki
                socket.sendto(str(1).encode('utf-8'), clients[1])

        # -- jeśli klient w bazie to go obsługujemy --
        elif self.client_address in clients: 
            # data - pole w które strzelił gracz, np. 12
            data = self.request[0].decode('utf-8')
            # - sprawdzamy czy trafił -
            print(Time(), self.client_address, " strzelił w: ", data)
            czyTrafiony = Strzal(tab, int(data[0]), int(data[1]), KtoryGracz(self.client_address[1]))

            # - wysyłanie informacji pozostałym -          
            for i in range(0, len(clients)):
                if i==0: tmp = tab
                else: tmp = [tab[2],tab[3],tab[0],tab[1]]
                if clients[i] != self.client_address:
                    # wiadomość do oczekującego (tego,który nie strzelał)
                    socket.sendto(str(-czyTrafiony).encode('utf-8'), clients[i])
                    socket.sendto(Serializuj(tmp), clients[i])
                else:
                    # wiadomość do strzelającego
                    socket.sendto(str(czyTrafiony).encode('utf-8'), clients[i])
                    socket.sendto(Serializuj(tmp), clients[i])
                    
            # - czyszczenie zmiennych w przypadku zakończenia gry -
            if czyTrafiony == 2:
                print(Time(),"Gra została zakończona - można zacząć kolejną")
                clients = []
                licznik = [0,0]
                liczbaStatkow = 4
                tab = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]
        # -- client nie został dodany i nie ma go w bazie --
        else:
            print(Time(),"Do gry chciał dołączyć ktoś nowy")
            # - wyślij graczowi odmowę dołączenia do gry [serwer pełny] -
            socket.sendto(dumps("no"), self.client_address)
        
def KtoryGracz(port):
    if port == clients[0][1]:
        return 1
    elif port == clients[1][1]:
        return 2
    else:
        return -1


def Serializuj(tb):
    return dumps(tb)

 
def ZliczStatek(tb, x, y, kier):
    licznik = 0
    #zlicza ile kfelków danego statku zostało zestrzelonych. 
    if kier == 0:
        while y < 9 and tb[x][y] != 0:
            licznik += 1
            y += 1
        if y == 9 and tb[x][y] != 0:
            licznik += 1
    elif kier == 1:
        while x > 0 and tb[x][y] != 0:
            licznik += 1
            x -= 1
        if x==0 and tb[x][y] != 0:
            licznik += 1
    elif kier == 2:
        while y > 0 and tb[x][y] != 0:
            licznik += 1
            y -= 1
        if y==0 and tb[x][y] != 0:
            licznik += 1
    elif kier == 3:
        while x < 9 and tb[x][y] != 0:
            licznik += 1
            x += 1
        if tb[x][y] != 0:
            licznik += 1
    return licznik


def ZatopStatek(tab, x1, y1, gracz, kier):
    #sprawia, że do okoła zatopionego statku pojawiają siepudla
    tb = tab[(gracz + 1) % 3 + 1]
    x = x1
    y = y1
    d = ZliczStatek(tab[(gracz + 1) % 3], x, y, kier)

    if kier == 0:
        for i in range(0, d):
            if x == x1 and y == y1:
                if y > 0:
                    tb[x][y - 1] = 3
                    if x > 0:
                        tb[x - 1][y - 1] = 3
                    if x < 9:
                        tb[x + 1][y - 1] = 3

            if x > 0:
                tb[x - 1][y] = 3
            if x < 9:
                tb[x + 1][y] = 3
            tab[(gracz + 1) % 3 + 1][x][y] = 2
            y += 1
        if y < 9:
            tb[x][y] = 3
            if x > 0:
                tb[x - 1][y] = 3
            if x < 9:
                tb[x + 1][y] = 3

    if kier == 1:
        for i in range(0, d):
            if x == x1 and y == y1:
                if x < 9:
                    tb[x + 1][y] = 3
                    if y > 0:
                        tb[x + 1][y - 1] = 3
                    if y < 9:
                        tb[x + 1][y + 1] = 3

            if y > 0:
                tb[x][y - 1] = 3
            if y < 9:
                tb[x][y + 1] = 3
            tab[(gracz + 1) % 3 + 1][x][y] = 2
            x -= 1
        if x >= 0:
            tb[x][y] = 3
            if y > 0:
                tb[x][y - 1] = 3
            if y < 9:
                tb[x][y + 1] = 3

    if kier == 2:
        for i in range(0, d):
            if x == x1 and y == y1:
                if y < 9:
                    tb[x][y + 1] = 3
                    if x > 0:
                        tb[x - 1][y + 1] = 3
                    if x < 9:
                        tb[x + 1][y + 1] = 3

            if x > 0:
                tb[x - 1][y] = 3
            if x < 9:
                tb[x + 1][y] = 3
            tab[(gracz + 1) % 3 + 1][x][y] = 2
            y -= 1
        if y >= 0:
            tb[x][y] = 3
            if x > 0:
                tb[x - 1][y] = 3
            if x < 9:
                tb[x + 1][y] = 3

    if kier == 3:
        for i in range(0, d):
            if x == x1 and y == y1:
                if x > 0:
                    tb[x - 1][y] = 3
                    if y > 0:
                        tb[x - 1][y - 1] = 3
                    if y < 9:
                        tb[x - 1][y + 1] = 3

            if y > 0:
                tb[x][y - 1] = 3
            if y < 9:
                tb[x][y + 1] = 3
            tab[(gracz + 1) % 3 + 1][x][y] = 2
            x += 1
        if x < 9:
            tb[x][y] = 3
            if y > 0:
                tb[x][y - 1] = 3
            if y < 9:
                tb[x][y + 1] = 3


def Strzal(tab, x, y, gracz):
    # x, y - współrzędne punktu w który został oddany strzał, x,y należą do [0,9]
    # gracz - nr gracza, który oddał strzał {1, 2}
    g = (gracz + 1) % 3
    # Wypisz(tab,g)
    #print(x, y)
    licz = [0, 0, 0, 0]
    kraniec = [x, y]
    #sprawdzamy w tablicy statków wartość pola - jak 0 mamy pudło
    if tab[g + 1][x][y] == 0:
        if tab[g][x][y] == 0:
            print(Time(),"pudło!")
            tab[g + 1][x][y] = 3
            return -1
        else:
            #w przeciwnym wypadku sprawdza, czy statek jest zatopiony szerzej niż tylko jedno pole i w którą stronę od właśnie wybranego statku
            tab[g + 1][x][y] = 1
            for kier in range(0, 4):
                if kier == 0:
                    yt = y
                    xt = x
                    while yt > 0 and tab[g + 1][xt][yt - 1] == 1:
                        yt -= 1
                        licz[0] += 1
                        kraniec[1] = yt
                elif kier == 1:
                    yt = y
                    xt = x
                    while xt < 9 and tab[g + 1][xt + 1][yt] == 1:
                        xt += 1
                        licz[1] += 1
                        kraniec[0] = xt
                elif kier == 2:
                    yt = y
                    xt = x
                    while yt < 9 and tab[g + 1][xt][yt + 1] == 1:
                        yt += 1
                        licz[2] += 1
                        kraniec[1] = yt
                else:
                    yt = y
                    xt = x
                    while xt > 0 and tab[g + 1][xt - 1][yt] == 1:
                        xt -= 1
                        licz[3] += 1
                        kraniec[0] = xt
            tr = 0
            for e in range(0, 4):
                if licz[e] != 0:
                    kier = e
            if licz == [0, 0, 0, 0] and tab[g][x][y] == 1:
                #jeżeli statek jest jednomasztowy, od razu zatpiamy
                tr = 1
                ZatopStatek(tab, kraniec[0], kraniec[1], gracz, kier)
                licznik[gracz-1] += 1
                if licznik[gracz-1] == liczbaStatkow:
                    return 2
                print(Time(),"Trafiony zatopiony")
                return 1
            elif ZliczStatek(tab[g + 1], kraniec[0], kraniec[1], kier) == tab[g][kraniec[0]][kraniec[1]]:
                #jeżeli zatopione kafelki są równe długości statku (zapisane w każdym polu), zatapiamy statek
                tr = 1
                ZatopStatek(tab, kraniec[0], kraniec[1], gracz, kier)
                licznik[gracz-1]+=1
                if licznik[gracz-1] == liczbaStatkow:
                    return 2
                print(Time(),"Trafiony zatopiony")
                return 1
            if tr == 0:
                print(Time(),"trafiony")
                tab[g + 1][x][y] = 1
                return 1
    else:
        print(Time(),"Już raz strzelałeś w to miejsce, wybierz inne.")
        return 1


if __name__ == "__main__":
    try:
        host, port = "10.55.5.82", 2223
        server = UDPServer((host, port), MyUDPHandler)
        print(Time(),"Serwer uruchomiony")
        server.serve_forever()
    except KeyboardInterrupt:      
        server.server_close()
        print(Time(),"Serwer wyłączony")
        exit()

