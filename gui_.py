from tkinter import *
import tkinter as tk
import time
from random import randrange


class Application(Frame):
    
    def __init__(self,master):

        Frame.__init__(self,master)
        self.launch()
        self.master = master
        self.even_or_odd = randrange(0,2)
        self.difficulty = "Easy"
        self.shiplist = []
        self.ai_shiplist = []
        self.player_shots = [1000]
        self.ai_shots = [1000]
        self.board = [
        ["A",1],["B",1],["C",1],["D",1],["E",1],["F",1],["G",1],["H",1],["I",1],["J",1],
        ["A",2],["B",2],["C",2],["D",2],["E",2],["F",2],["G",2],["H",2],["I",2],["J",2],
        ["A",3],["B",3],["C",3],["D",3],["E",3],["F",3],["G",3],["H",3],["I",3],["J",3],
        ["A",4],["B",4],["C",4],["D",4],["E",4],["F",4],["G",4],["H",4],["I",4],["J",4],
        ["A",5],["B",5],["C",5],["D",5],["E",5],["F",5],["G",5],["H",5],["I",5],["J",5],
        ["A",6],["B",6],["C",6],["D",6],["E",6],["F",6],["G",6],["H",6],["I",6],["J",6],
        ["A",7],["B",7],["C",7],["D",7],["E",7],["F",7],["G",7],["H",7],["I",7],["J",7],
        ["A",8],["B",8],["C",8],["D",8],["E",8],["F",8],["G",8],["H",8],["I",8],["J",8],
        ["A",9],["B",9],["C",9],["D",9],["E",9],["F",9],["G",9],["H",9],["I",9],["J",9],
        ["A",10],["B",10],["C",10],["D",10],["E",10],["F",10],["G",10],["H",10],["I",10],["J",10],
        ]
        self.letters = [["A",1],["B",2],["C",3],["D",4],["E",5],["F",6],["G",7],["H",8],["I",9],["J",10]]
    def launch(self):
        self.pack(fill=BOTH, expand=1)

        #podpisy plansz
        Label(self, text="Twoja plansza\nA        B      C      D      E       F      G     H      I       J").grid(sticky=W,row = 0, column = 2,columnspan = 3)
        Label(self, text="Plansza przeciwnika\nA        B      C      D      E       F      G     H      I       J").grid(sticky=W, row = 0,column = 5)
        Label(self, text="1").grid(sticky=NE, row = 1,column = 1,pady=3)
        Label(self, text="2").grid(sticky=NE, row = 1,column = 1, pady=28)
        Label(self, text="3").grid(sticky=NE, row = 1,column = 1, pady=53)
        Label(self, text="4").grid(sticky=NE, row = 1,column = 1, pady=78)
        Label(self, text="5").grid(sticky=NE, row = 1,column = 1, pady=103)
        Label(self, text="10").grid(sticky=SE, row = 1,column = 1, pady=18)
        Label(self, text="9").grid(sticky=SE, row = 1,column = 1, pady=43)
        Label(self, text="8").grid(sticky=SE, row = 1,column = 1, pady=68)
        Label(self, text="7").grid(sticky=SE, row = 1,column = 1,pady=93)
        Label(self, text="6").grid(sticky=SE, row = 1,column = 1,pady=118)


        self.canvas1 = Canvas(self) #plansza gracza
        for num1 in range(10):
            for num2 in range(10):
                self.canvas = Canvas(self)
                self.canvas1.create_rectangle(2 + (num2) * 25,2+ (num1) * 25,250,250,outline= "black",fill = "white")
                self.canvas1.grid(row=1, column=2,sticky = N,columnspan = 3)

        
        self.canvas2 = Canvas(self) #plansza przeciwnika
        for num1 in range(10):
            for num2 in range(10):
                self.canvas = Canvas(self)
                self.canvas2.create_rectangle(2 + (num2) * 25,2+ (num1) * 25,250,250,outline= "black",fill = "white")
                self.canvas2.grid(row=1, column=5,columnspan = 2,sticky = N)

        #wprowadzanie statków
        Label(self,text = "Twoje Statki:").grid(row = 3,column= 1,sticky = W)
        self.label2 = Label(self,text = "Pierwszy punkt:")
        self.label2.grid(row = 3,column= 3,sticky = W)
        self.label1 = Label(self,text = "              Kierunek:")
        self.label1.grid(row = 3,column= 2,sticky = W)
        Label(self,text ="Pięciomasztowiec (5)").grid(row = 4,column = 1,sticky  = W)       
        Label(self,text = "Czteromasztowiec (4)").grid(row=5,column=1,sticky  = W)
        Label(self,text = "Trójmasztowiec 1 (3)").grid(row=6,column=1,sticky  = W)
        Label(self,text = "Trójmasztowiec 2 (3)").grid(row=7,column=1,sticky  = W)
        Label(self,text = "Dwumasztowiec (2)").grid(row=8,column=1,sticky  = W)
        Label(self,text = "").grid(row = 10,column = 1)
        #Label(self,text = "AI Difficulty:").grid(row = 5,column = 5)

        self.difficulty = StringVar(value = "Easy")
        #Radiobutton(self,text = "Easy",variable = self.difficulty,value = "Easy").grid(row = 5,column = 5,sticky = E)
        #Radiobutton(self,text = "Normal",variable = self.difficulty,value = "Normal").grid(row = 6,column = 5,sticky = E)
        
        
        self.error_label2 = Label(self,text = "")
        self.error_label2.grid(column = 5, row = 9)
        Label(self,text = "").grid(column = 5, row = 12)
        self.shoot_entry = Entry(self,)       
        self.shoot_button = Button(self,text = "Strzelaj",command = self.shoot)
        
        self.ac_direct = Entry(self,)
        self.ac_direct.grid(row=4,column=2,sticky  = E)
        
        self.ba_direct = Entry(self,)
        self.ba_direct.grid(row=5,column=2,sticky  = E)
        
        self.de_direct = Entry(self,)
        self.de_direct.grid(row=6,column=2,sticky  = E)
        
        self.su_direct = Entry(self,)
        self.su_direct.grid(row=7,column=2,sticky  = E)
        
        self.pa_direct = Entry(self,)
        self.pa_direct.grid(row=8,column=2,sticky  = E)
                
        self.ac_coord = Entry(self,)
        self.ac_coord.grid(row=4,column=3,sticky  = N)
        
        self.ba_coord = Entry(self,)
        self.ba_coord.grid(row=5,column=3,sticky  = N)
        
        self.de_coord = Entry(self,)
        self.de_coord.grid(row=6,column=3,sticky  = N)
        
        self.su_coord = Entry(self,)
        self.su_coord.grid(row=7,column=3,sticky  = N)
        
        self.pa_coord = Entry(self,)
        self.pa_coord.grid(row=8,column=3,sticky  = N)
        


        
        self.actionbutton = Button(self,text = "Potwierdź") #,command = self.ships
        self.actionbutton.grid(row = 4,column = 5,sticky = E)
        Button(self,text = "Instrukcja gry",command = self.help_button).grid(row = 0,column =0 ,sticky = E +N) #instrukcja gry

        #miejsce na errory
        self.errorlabel = Label(self,text = "")
        self.errorlabel.grid(row=9,column=0)  

    def update_grid(self):
        number = 0
        for num1 in range(10):
            for num2 in range(10):
                color = "white"
                for ship in self.shiplist:                 
                    for coord in ship[4]:
                        if number == coord[0] and coord[1] == "Pływa":
                            if ship[1] == "Pięciomasztowiec":
                                color = "orange"
                            elif ship[1] == "Czteromasztowiec":
                                color = "yellow"
                            elif ship[1] == "Trójmasztowiec 1":
                                color = "green"
                            elif ship[1] == "Trójmasztowiec 2":
                                color = "blue"
                            elif ship[1] == "Dwumasztowiec":
                                color = "purple"
                
                        elif number == coord[0] and coord[1] == "Trafiony":
                              color = "red"
                
                for cell in self.ai_shots:
                    if cell == number and color != "red":
                        color = "grey"
                self.canvas = Canvas(self)
                self.canvas1.create_rectangle(2 + (num2) * 25,2+ (num1) * 25,250,250,outline= "black",fill = color)
                self.canvas1.grid(row=1, column=2,sticky = W,columnspan = 3)
                number+=1
        winning = 0       
        for ships in self.shiplist:
            for coords in ship[4]:
                if coords[1] == "Trafiony":
                    winning += 1
        if winning == 17:
            self.game_end("AI")
        winning = 0
        for ships in self.ai_shiplist:
            for coords in ships[4]:
                if coords[1] == "Trafiony":
                    winning += 1
        if winning == 17:
            self.game_end("Gracz")
        number = 0
        for num1 in range(10):
           for num2 in range(10):
                color = "white"
                for ship in self.ai_shiplist:
                    for coord1 in ship[4]:
                        if number == coord1[0] and coord1[1] == "Trafiony":
                           color = "red"
                for cell in self.player_shots:
                    if cell == number and color != "red":
                        color = "grey"
                self.canvas = Canvas(self)
                self.canvas2.create_rectangle(2 + (num2) * 25,2+ (num1) * 25,250,250,outline= "black",fill = color)
                self.canvas2.grid(row=1, column=5,sticky = E)
                number+=1
                
    def shoot(self):
        coord = self.shoot_entry.get()
        try:
            coord = coord[0].upper() + str(coord[1:])
        except(IndexError):
            True
        if len(coord) != 2 and len(coord)!= 3:
            self.error_label2.configure(text = "Złe koordynaty strzału!")
        
        elif (coord[0] == "A" or coord[0] == "B" or coord[0] == "C" or coord[0] == "D" or coord[0] == "E" or coord[0] == "F" or coord[0] == "G" or coord[0] == "H" or coord[0] == "I" or coord[0] == "J") and ( coord[1] == "1" or coord[1] == "2" or coord[1] == "3" or coord[1] == "4" or coord[1] == "5" or coord[1] == "6" or coord[1] == "7" or coord[1] == "8" or coord[1] == "9" or coord[1] == "10"):
            
            
            for cell in range(len(self.board)):
                try:
                    if coord[0] == self.board[cell][0] and coord[1:] == str(self.board[cell][1]):
                        coord = cell
                except(TypeError):
                    True
            num = 0
            for i in self.player_shots:
                if str(i) == str(coord):
                    num += 1
                    self.error_label2.configure(text = "Nie możesz tutaj strzelać! Już tu wcześniej strzeliłeś!")
                else:
                    True
            if num  == 0:
                self.player_shots.append(coord)
                #if self.difficulty == "Easy":
                while num == 0:
                    ai_coord = randrange(0,100)
                    for number in self.ai_shots:
                        if number == ai_coord:       
                            num +=1
                        else:
                            True
                    if num > 0:
                        num = 0
                    elif num == 0:
                        num = 1
                        
                    
                if num == 1:
                    self.ai_shots.append(ai_coord)
                    strzal=ai_coord
                    
                    self.error_label2.configure(text = "Przeciwnik strzelił w "+ str(ai_coord + 11))
            
            for ai_ship in self.ai_shiplist:
                num = 0
                for coordinate in ai_ship[4]:
                    if coordinate[0] == coord:
                        coordinate[1] = "Trafiony"
                    if coordinate[1] == "Trafiony":
                        num +=1
                if num == ai_ship[2]:
                    if ai_ship[1] == "Pięciomasztowiec Wrogi":
                        self.aiac_label.configure(text = "ZATOPIONY!")
                    elif ai_ship[1] == "Czteromasztowiec Wrogi":
                        self.aiba_label.configure(text = "ZATOPIONY!")
                    elif ai_ship[1] == "Trójmasztowiec 1 Wrogi":
                        self.aide_label.configure(text = "ZATOPIONY!")
                    elif ai_ship[1] == "Trójmasztowiec 2 Wrogi":
                        self.aisu_label.configure(text = "ZATOPIONY!")
                    elif ai_ship[1] == "Dwumasztowiec Wrogi":
                        self.aipa_label.configure(text = "ZATOPIONY!")

                
            for ship in self.shiplist:
                num = 0
                for coordinate2 in ship[4]:
                    try:
                        if coordinate2[0] == ai_coord:
                            coordinate2[1] = "Trafiony"
                        if coordinate[1] == "Trafiony":
                            num +=1
                    except(UnboundLocalError):
                        True
                if num == ship[2]:
                    if ship[1] == "Pięciomasztowiec":
                        self.pac_label.configure(text = "ZATOPIONY!")
                    elif ship[1] == "Czteromasztowiec":
                        self.pba_label.configure(text = "ZATOPIONY!")
                    elif ship[1] == "Trójmasztowiec 1":
                        self.pde_label.configure(text = "ZATOPIONY!")
                    elif ship[1] == "Trój masztowiec 2":
                        self.psu_label.configure(text = "ZATOPIONY!")
                    elif ship[1] == "Dwumasztowiec":
                        self.ppa_label.configure(text = "ZATOPIONY!")
                    
            self.update_grid() ##
        else:
            self.error_label2.configure(text = "Złe koordynaty strzału!")
    def help_button(self):
        window = tk.Toplevel(self)   
        message = "Zagrajmy w statki!"
        label = tk.Label(window, text=message)
        label.pack(side="top", fill="both", padx=10, pady=10)
        
    def game_end(self,winner):
        self.shoot_button.grid_forget()
        self.shoot_entry.grid_forget()
        
        if winner == "Gracz":
            message = "Gratulacje! Wygrałeś!"
        else:
            message = "O nie! Przeciwnik zatopił wszystkie Twoje statki!"
        window = tk.Toplevel(self)
        label = tk.Label(window, text=message)
        label.pack(side="top", fill="both", padx=10, pady=10)
            
                            
def main():

    root = tk.Tk()
    app = Application(root)
    root.geometry = ("1000x1000")
    root.title("Gra w statki")
    root.mainloop()
    


main()
