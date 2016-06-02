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
        [0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],
        [0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1],[8,1],[9,1],
        [0,2],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2],[9,2],
        [0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,3],[9,3],
        [0,4],[1,4],[2,4],[3,4],[4,4],[5,4],[6,4],[7,4],[8,4],[9,4],
        [0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],
        [0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],[7,6],[8,6],[9,6],
        [0,7],[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],[8,7],[9,7],
        [0,8],[1,8],[2,8],[3,8],[4,8],[5,8],[6,8],[7,8],[8,8],[9,8],
        [0,9],[1,9],[2,9],[3,9],[4,9],[5,9],[6,9],[7,9],[8,9],[9,9],
        ]
        #self.letters = [["A",1],["B",2],["C",3],["D",4],["E",5],["F",6],["G",7],["H",8],["I",9],["J",10]]

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
        self.difficulty = StringVar(value = "Easy")
                
        self.error_label2 = Label(self,text = "")
        self.error_label2.grid(column = 5, row = 9)
        Label(self,text = "").grid(column = 5, row = 12)
        self.shoot_entry = Entry(self,)       
        self.shoot_button = Button(self,text = "Strzelaj")#,command = self.shoot
        
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
        


        
        self.actionbutton = Button(self,text = "Potwierdź")#,command = self.ships
        self.actionbutton.grid(row = 4,column = 5,sticky = E)
        Button(self,text = "Instrukcja gry",command = self.help_button).grid(row = 0,column =0 ,sticky = E +N) #instrukcja gry

        #miejsce na errory
        self.errorlabel = Label(self,text = "")
        self.errorlabel.grid(row=9,column=0)  
    def ships(self):
        invalid_cell = []
        invalid_ai = []
        error = "no"
        self.shiplist = []
        self.error_label2.configure(text = "")
        ac_player = ["gracz","Pięciomasztowiec",5,self.ac_direct.get().upper(),self.ac_coord.get()]
        ba_player = ["gracz","Czteromasztowiec",4,self.ba_direct.get().upper(),self.ba_coord.get()]
        de_player = ["gracz","Trójmasztowiec 1",3,self.de_direct.get().upper(),self.de_coord.get()]
        su_player = ["gracz","Trójmasztowiec 2",3,self.su_direct.get().upper(),self.su_coord.get()]
        pa_player = ["gracz","Dwumasztowiec",2,self.pa_direct.get().upper(),self.pa_coord.get()]
        print ("Oto lista")
        print (ac_player)
        print ("koniec listy")
        


            
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
