from tkinter import *

class Pion:
    def __init__(self, abscisse, ordonnee, player):
        self.__x = abscisse
        self.__y = ordonnee
        self.player = player

    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getPlayer(self):
        return self.player

    def setX(self, newX):
        self.__x = newX
    def setY(self, newY):
        self.__y = newY
    def setPlayer(self, newPlayer):
        self.player = newPlayer


    def updatePlayer(self):
        player = self.getPlayer()
        if player == 1:
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
        boardSize = self.__boardSize
        x = self.pion.getX()
        y = self.pion.getY()
        possibleMove = []
        possibleCoords = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for possibleCoordsX, possibleCoordsY in possibleCoords:
            newX, newY = x +possibleCoordsX, y + possibleCoordsY
            if 0 <= newX < boardSize and 0 <= newY < boardSize and self.__Board[newX][newY] == 0:
                possibleMove.append((newX, newY))
        print(possibleMove)
        return possibleMove
    
    def updateBoard(self, x, y):
        possibleMove = self.moveCondition()
        for coords in possibleMove:
            if (x, y) == coords:
                self.__Board[x][y] = self.pion.getPlayer()
                self.pion.setX(x)
                self.pion.setY(y)
                return True
            else:
                return False
                
        


class GameInterface:
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.pion = Pion(0, 0, 1)
        self.jeu = Jeu(boardSize, pion)
        self.player = 1

        self.window = Tk()
        self.window.title("Jeu de Puissance 5")


        self.buttons = []
        for i in range(boardSize):
            row = []
            for j in range(boardSize):
                button = Button(self.window, width=4, height=2, command=lambda i=i, j=j: self.place_pion(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.window.mainloop()
        

    def place_pion(self, x, y):
        self.pion.setX(x)
        self.pion.setY(y)
        if self.jeu.updateBoard(x, y) == True:
            self.buttons[x][y].config(bg='green')
        else:
            self.buttons[x][y].config(bg='red')
            
            
pion = Pion(0,0,1)    
game = Jeu(10, pion)
game = GameInterface(10)