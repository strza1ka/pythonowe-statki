# coding=utf-8
from pickle import loads, dumps
from time import sleep
from tkinter import *
from socketserver import BaseRequestHandler, UDPServer
from tkinter import *
import tkinter as tk
import time
from random import randrange
import pygame

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
clients = []
licznik = [0,0]
liczbaStatkow = 1

class MyUDPHandler(BaseRequestHandler):
    def handle(self):
        # dodaj clienta jeśli nie ma go w bazie klientów i jest mniej niż 2 osoby
        socket = self.request[1]
        if self.client_address not in clients and len(clients)<2:
            clients.append(self.client_address)
            print("Do gry dołączył gracz: ", self.client_address)

            #otrzymuję tablicę ze statkami gracza
            global statki
            statki = loads(self.request[0])

            #gracz, który pierwszy się dołączył, drugi zaczyna
            if len(clients) == 1:
                tab[0] = statki
                socket.sendto(str(-1).encode('utf-8'), clients[0])
            else:
                tab[2] = statki
                socket.sendto(str(1).encode('utf-8'), clients[1])
            # print(clients)
        #jeśli klient w bazie to go obsługujemy
        elif self.client_address in clients: 
            #data - pole w które strzelił gracz, np. 12
            data = self.request[0].decode('utf-8')

            #sprawdzamy czy trafił
            print(self.client_address, " strzelił w: ", data)
            czyTrafiony = Strzal(tab, int(data[0]), int(data[1]), KtoryGracz(self.client_address[1]))

            # wysyłanie informacji pozostałym:
            ##tutaj wysyłam wszystkim klientom ~~ client[i] = (ip, port)
            for i in range(0, len(clients)):
                if clients[i] != self.client_address:
                    # wiadomość do oczekującego (tego,który nie strzelał)
                    socket.sendto(str(-czyTrafiony).encode('utf-8'), clients[i])
                    socket.sendto(Serializuj(tab), clients[i])
                else:
                    # wiadomość do strzelającego
                    socket.sendto(str(czyTrafiony).encode('utf-8'), clients[i])
                    socket.sendto(Serializuj(tab), clients[i])
        else:
            print("Do gry chciał dołączyć ktoś nowy")
            socket.sendto(str(3).encode('utf-8'), self.client_address)


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
    if kier == 0:
        while y < 9 and tb[x][y + 1] != 0:
            if tb[x][y] != 0:
                licznik += 1
                y += 1
        if tb[x][y] != 0:
            licznik += 1
    elif kier == 1:
        while x > 0 and tb[x][y] != 0:
            licznik += 1
            x -= 1
    elif kier == 2:
        while y > 0 and tb[x][y] != 0:
            licznik += 1
            y -= 1
    elif kier == 3:
        while x < 9 and tb[x + 1][y] != 0:
            licznik += 1
            x += 1
        if tb[x][y] != 0:
            licznik += 1
    return licznik


def ZatopStatek(tab, x1, y1, gracz, kier):
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
    if tab[g + 1][x][y] == 0:
        if tab[g][x][y] == 0:
            print("pudło!")
            tab[g + 1][x][y] = 3
            return -1
        else:
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
                tr = 1
                ZatopStatek(tab, kraniec[0], kraniec[1], gracz, kier)
                licznik[gracz-1] += 1
                if licznik[gracz-1] == liczbaStatkow:
                    return 2
                print("Trafiony zatopiony")
                return 1
            elif ZliczStatek(tab[g + 1], kraniec[0], kraniec[1], kier) == tab[g][kraniec[0]][kraniec[1]]:
                tr = 1
                ZatopStatek(tab, kraniec[0], kraniec[1], gracz, kier)
                licznik[gracz-1]+=1
                if licznik[gracz-1] == liczbaStatkow:
                    return 2
                print("Trafiony zatopiony")
                return 1
            if tr == 0:
                print("trafiony")
                tab[g + 1][x][y] = 1
                return 1
    else:
        print("Już raz strzelałeś w to miejsce, wybierz inne.")
        return 1


if __name__ == "__main__":
    host, port = "localhost", 2223
    server = UDPServer((host, port), MyUDPHandler)
    server.serve_forever()
