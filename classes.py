from tkinter import *

class Pion:
    def __init__(self, abscisse, ordonnee, player):
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
        for dx, dy in possibleCoords:
            newX, newY = x + dx, y + dy
            if 0 <= newX < self.__boardSize and 0 <= newY < self.__boardSize and self.__Board[newX][newY] == 0:
                possibleMove.append((newX, newY))
        print(possibleMove)
        print(self.pion.getPlayer())
        return possibleMove

    def updateBoard(self, x, y):
        if (x, y) in self.moveCondition():
            self.__Board[x][y] = self.pion.getPlayer()
            self.pion.setX(x)
            self.pion.setY(y)
            return True
        return False

class GameInterface:
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.pion = Pion(0, 0, 1)
        self.jeu = Jeu(boardSize, self.pion)

        self.window = Tk()
        self.window.title("Jeu de Puissance 5")

        self.buttons = [[Button(self.window, width=4, height=2, command=lambda i=i, j=j: self.place_pion(i, j)) for j in range(boardSize)] for i in range(boardSize)]
        for i in range(boardSize):
            for j in range(boardSize):
                self.buttons[i][j].grid(row=i, column=j)

        self.window.mainloop()

    def place_pion(self, x, y):
        if self.jeu.updateBoard(x, y):
            player = self.pion.getPlayer()
            if player == 1:
                self.buttons[x][y].config(bg='green')
            else:
                self.buttons[x][y].config(bg='blue')
            self.pion.updatePlayer()
        else:
            self.buttons[x][y].config(bg='red')

game = GameInterface(10)
