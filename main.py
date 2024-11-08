from tictactoe.tictactoe import *
from os import system
game = [
    #0  1  2
    [" "," "," "], #game[0]
    [" "," "," "], #game[1]
    [" "," "," "]  #game[2]
    ]

a1 = game[0][0]
a2 = game[0][1]
a3 = game[0][2]
b1 = game[1][0]
b2 = game[1][1]
b3 = game[1][2]
c1 = game[2][0]
c2 = game[2][1]
c3 = game[2][2]
def menu():

    while True:
        try:
            system("clear")
            menu = int(input("Start(1) || Kilépés(2)"))
            if menu == 1:
                start()
            elif menu == 2:
                exit()
            else:
                print("Írj be helyes adatot!")
        except ValueError:
            print("Írj be helyes adatot!")

def start():
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    while True:
        if a1 == "o" and a2 == "o" and a3 == "o": 
            print("Nyert: o") 
            return 
        elif b1 == "o" and b2 == "o" and b3 == "o":
            print("Nyert: o")
            return
        elif c1 == "o" and c2 == "o" and c3 == "o":
            print("Nyert: o")
            return
        elif a1 == "o" and b1 == "o" and c1 == "o":
            print("Nyert: o")
            return
        elif a2 == "o" and b2 == "o" and c2 == "o":
            print("Nyert: o")
            return
        elif a3 == "o" and b3 == "o" and c3 == "o":
            print("Nyert: o")
            return
        elif a1 == "o" and b2 == "o" and c3 == "o":
            print("Nyert: o")
            return
        elif a1 == "x" and a2 == "x" and a3 == "x":
            print("Nyert: x")
            return
        elif b1 == "x" and b2 == "x" and b3 == "x":
            print("Nyert: x")
            return
        elif c1 == "x" and c2 == "x" and c3 == "x":
            print("Nyert: x")
            return
        elif a1 == "x" and b1 == "x" and c1 == "x":
            print("Nyert: x")
            return
        elif a2 == "x" and b2 == "x" and c2 == "x":
            print("Nyert: x")
            return
        elif a3 == "x" and b3 == "x" and c3 == "x":
            print("Nyert: x")
            return
        elif a1 == "x" and b2 == "x" and c3 == "x":
            print("Nyert: x")
            return
        system("clear")
        print("   1   2   3")
        print("  ___________")
        print(f"a | {a1} | {a2} | {a3} |")
        print(f"  |---|---|---|")
        print(f"b | {b1} | {b2} | {b3} |")
        print(f"  |---|---|---|")
        print(f"c | {c1} | {c2} | {c3} |")
        print("  -----------")
        while True:
            player1 = input("Játékos1(x): Hova lépsz?")
            if player1 == "a1":
                a1 = "x"
                break
            elif player1 == "a2":
                a2 = "x"
                break
            elif player1 == "a3":
                a3 = "x"
                break
            elif player1 == "b1":
                b1 = "x"
                break
            elif player1 == "b2":
                b2 = "x"
                break
            elif player1 == "b3":
                b3 = "x"
                break
            elif player1 == "c1":
                c1 = "x"
                break
            elif player1 == "c2":
                c2 = "x"
                break
            elif player1 == "c3":
                c3 = "x"
                break
            
        system("clear")
        print("   1   2   3")
        print("  ___________")
        print(f"a | {a1} | {a2} | {a3} |")
        print(f"  |---|---|---|")
        print(f"b | {b1} | {b2} | {b3} |")
        print(f"  |---|---|---|")
        print(f"c | {c1} | {c2} | {c3} |")
        print("  -----------")
        while True:
            player2 = input("Játékos2(o): Hova lépsz?")
            if player2 == "a1": a1 = "o"
            elif player2 == "a2":
                a2 = "o"
                break
            elif player2 == "a3":
                a3 = "o"
                break
            elif player2 == "b1":
                b1 = "o"
                break
            elif player2 == "b2":
                b2 = "o"
                break
            elif player2 == "b3":
                b3 = "o"
                break
            elif player2 == "c1":
                c1 = "o"
                break
            elif player2 == "c2":
                c2 = "o"
                break
            elif player2 == "c3":
                c3 = "o"
                break
    
    
    


if __name__ == "__main__":
    menu()