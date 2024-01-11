from tkinter import *

class Pion:
    def __init__(self, abscisse = -1, ordonnee = -1, player = 1):
        self.__x = abscisse
        self.__y = ordonnee
        self.__player = player

    def getX(self):
        return self.__x
    def getY(self):
        return self.__y

    def setX(self, newX):
        self.__x = newX
    def setY(self, newY):
        self.__y = newY

    def getPlayer(self):
        return self.__player

    def setPlayer(self, newPlayer):
        self.__player = newPlayer

    def updatePlayer(self):
        if self.__player == 1:
            self.setPlayer(2)
        else:
            self.setPlayer(1)

class Jeu:
    def __init__(self, boardSize, pion):
        self.__boardSize = boardSize
        self.pion = pion
        self.__Board = self.plateau(boardSize)

    def plateau(self, boardSize):
        board = []
        for i in range(boardSize):
            line = []
            for j in range(boardSize):
                line.append(0)
            board.append(line)
        return board


    def moveCondition(self):
        x = self.pion.getX()
        y = self.pion.getY()
        possibleMove = []
        possibleCoords = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for possibleCoordsX, possibleCoordsY in possibleCoords:
            newX, newY = x + possibleCoordsX, y + possibleCoordsY
            if 0 <= newX < self.__boardSize and 0 <= newY < self.__boardSize and self.__Board[newX][newY] == 0:
                possibleMove.append((newX, newY))
        print(possibleMove)
        print(self.pion.getPlayer())
        return possibleMove

    
    def updateBoard(self, x, y):
        if (x, y) in self.moveCondition():
            currentPlayer = self.pion.getPlayer()
            self.__Board[x][y] = currentPlayer
            self.pion.setX(x)
            self.pion.setY(y)

            # Mise à jour de l'état de jeu pour le prochain joueur
            self.pion.updatePlayer()  # Change le joueur actif
            nextPlayerMoves = self.moveCondition()  # Calcule les coups possibles pour le joueur suivant
            print(f"Possible moves for player {self.pion.getPlayer()}: {nextPlayerMoves}")
            
            return True
        return False

class GameInterface:
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.pion = Pion()
        self.jeu = Jeu(boardSize, self.pion)
        self.player = 1

        self.window = Tk()
        self.window.title("Jeu de Puissance 5")
        self.window.config(padx=20, pady=20, highlightthickness=0, bd=0, bg="black")

        self.__frame1 = Frame(self.window)
        self.__frame1.grid(row=0, column=0, rowspan=2)
        self.__frame1.config(pady=20, bg="black")

        self.__frame2 = Frame(self.window)
        self.__frame2.grid(row=boardSize, column=0)
        self.__frame2.config(padx=5, pady=5)

        self.__nbText = StringVar()
        self.__nbText.set("Player " + str(self.player))
        self.__text1 = Label(self.__frame2, textvariable=self.__nbText)
        self.__text1.pack()

        self.buttons = [[Button(self.__frame1, width=4, height=2, command=lambda i=i, j=j: self.place_pion(i, j)) for j in range(boardSize)] for i in range(boardSize)]
        for i in range(boardSize):
            for j in range(boardSize):
                self.buttons[i][j].grid(row=i, column=j)
        self.debutJeu()

        self.window.mainloop()

    def debutJeu(self):
        print("Début du jeu. Les joueurs peuvent placer leur premier pion où ils veulent.")

    def place_pion(self, x, y):
        if self.pion.getX() == -1 and self.pion.getY() == -1:
            self.pion.setX(x)
            self.pion.setY(y)
            player = self.pion.getPlayer()
            if player == 1:
                self.buttons[x][y].config(bg='green')
            else:
                self.buttons[x][y].config(bg='blue')
            self.pion.updatePlayer()
        else:
            if self.jeu.updateBoard(x, y):
                self.buttons[x][y].config(bg='green' if self.pion.getPlayer() == 1 else 'blue')
                self.pion.updatePlayer()
            else:
                self.buttons[x][y].config(bg='red')
game = GameInterface(10)
