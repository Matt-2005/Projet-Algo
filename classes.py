from tkinter import *

class Pion:
    def __init__(self, abscisse = -1, ordonnee = -1, player = 0):
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
        self.__player = (self.__player + 1) % 2


class Jeu:
    def __init__(self, boardSize, pion):
        self.__boardSize = boardSize
        self.pion = pion
        self.__Board = self.plateau(boardSize)
        self.coords = {0: [], 1: []} 
        self.possibleMoves = {0: [], 1: []}


    def plateau(self, boardSize):
        board = []
        for i in range(boardSize):
            line = []
            for j in range(boardSize):
                line.append(0)
            board.append(line)
        return board


    def moveCondition(self):
        currentPlayer = self.pion.getPlayer()
        if currentPlayer in self.coords:
            coords_player = self.coords[currentPlayer]
            x = coords_player[0][0]
            y = coords_player[0][1]
        else:
            x, y = -1, -1

        possibleCoords = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for possibleCoordsX, possibleCoordsY in possibleCoords:
            newX, newY = x + possibleCoordsX, y + possibleCoordsY
            if 0 <= newX < self.__boardSize and 0 <= newY < self.__boardSize and self.__Board[newX][newY] == 0:
                self.possibleMoves[currentPlayer].append((newX, newY))
        print(self.possibleMoves[currentPlayer])
        print(currentPlayer)
        print(x, y)
        return self.possibleMoves[currentPlayer]


    def winCondition(self):
        boardSize = self.__boardSize
        rows, cols = boardSize, boardSize
        currentPlayer = self.pion.getPlayer()

        # Vérification horizontale
        for row in range(rows):
            for col in range(cols - alignement + 1):
                if all(self.__Board[row][col + i] == currentPlayer + 1 for i in range(alignement)):
                    print(f"Victoire horizontale détectée en ligne {row}, colonne {col} à {col + alignement - 1}")
                    return True

        # Vérification verticale
        for row in range(rows - alignement + 1):
            for col in range(cols):
                if all(self.__Board[row + i][col] == currentPlayer + 1 for i in range(alignement)):
                    print(f"Victoire verticale détectée en ligne {row} à {row + alignement - 1}, colonne {col}")
                    return True

        # Vérification diagonale (\)
        for row in range(rows - alignement + 1):
            for col in range(cols - alignement + 1):
                if all(self.__Board[row + i][col + i] == currentPlayer + 1 for i in range(alignement)):
                    print(f"Victoire diagonale (\\) détectée de ({row}, {col}) à ({row + alignement - 1}, {col + alignement - 1})")
                    return True

        # Vérification diagonale (/)
        for row in range(alignement - 1, rows):
            for col in range(cols - alignement + 1):
                if all(self.__Board[row - i][col + i] == currentPlayer + 1 for i in range(alignement)):
                    print(f"Victoire diagonale (/) détectée de ({row}, {col}) à ({row - alignement + 1}, {col + alignement - 1})")
                    return True

        return False



    
    
    def updateBoard(self, x, y, nbCoups):
        currentPlayer = self.pion.getPlayer()
        if nbCoups > 1 and (x, y) not in self.possibleMoves[currentPlayer]:
            return False

        if (x, y) in self.moveCondition() or nbCoups <= 1: 
            self.__Board[x][y] = currentPlayer + 1
            self.pion.setX(x)
            self.pion.setY(y)
            nbCoups += 1
            return True
        return False
    

class GameInterface:
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.pion = Pion()
        self.jeu = Jeu(boardSize, self.pion)
        self.nbCoups = 0
        self.lastButton1 = None
        self.lastButton2 = None

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
        self.__nbText.set("Player " + str(self.pion.getPlayer() + 1))
        self.__text1 = Label(self.__frame2, textvariable=self.__nbText, width=10, height=2, bg='black', fg='white')
        self.__text1.pack()
        self.buttons = [
            [Button(self.__frame1, width=6, height=3, bg='black', command=lambda i=i, j=j: self.placePion(i, j)) for j
             in range(boardSize)] for i in range(boardSize)]
        for i in range(boardSize):
            for j in range(boardSize):
                self.buttons[i][j].grid(row=i, column=j)
        self.debutJeu()

        self.window.mainloop()

    def debutJeu(self):
        print("Début du jeu. Les joueurs peuvent placer leur premier pion où ils veulent.")

    def finJeu(self):
        if self.jeu.winCondition() == True:  # Jarrive pas à ramener la fonction winCondition ici :/
            print("Player " + str(self.pion.getPlayer() + 1) + " wins !")

    def restoreColor(self, x, y):
        self.buttons[x][y].config(bg='black')

    def changeColorPlayer1(self):
        self.lastButton1.config(bg='green')

    def changeColorPlayer2(self):
        self.lastButton2.config(bg='blue')

    def placePion(self, x, y):
        currentPlayer = self.pion.getPlayer()
        coupValide = False

        if self.nbCoups < 2:
            self.pion.setX(x)
            self.pion.setY(y)
            if currentPlayer == 0:
                self.buttons[x][y].config(bg='#3FEE3C')
                self.lastButton1 = self.buttons[x][y]
            else:
                self.buttons[x][y].config(bg='#31B3F0')
                self.lastButton2 = self.buttons[x][y]
            self.jeu.coords[currentPlayer] = [(x, y)]
            self.jeu.possibleMoves[currentPlayer] = []
            self.jeu.possibleMoves[currentPlayer] = self.jeu.moveCondition()
            coupValide = True
        else:
            if self.jeu.updateBoard(x, y, self.nbCoups):
                if currentPlayer == 0:
                    self.buttons[x][y].config(bg='#3FEE3C')
                    self.changeColorPlayer1()
                    self.lastButton1 = self.buttons[x][y]
                else:
                    self.buttons[x][y].config(bg='#31B3F0')
                    self.changeColorPlayer2()
                    self.lastButton2 = self.buttons[x][y]
                self.jeu.coords[currentPlayer] = [(x, y)]
                self.jeu.possibleMoves[currentPlayer] = []
                self.jeu.possibleMoves[currentPlayer] = self.jeu.moveCondition()
                coupValide = True
            else:
                self.buttons[x][y].after(500, self.restoreColor(x, y))
                print("Mouvement invalide, veuillez réessayer.")

        if coupValide == True:
            currentPlayer = self.pion.getPlayer()
            self.pion.updatePlayer()
            self.nbCoups += 1
            self.__nbText.set(f"Player {currentPlayer + 1}")
            self.finJeu()
            
                
tailleJeu = int(input("Taille du plateau (entre 8 et 12) : "))
while tailleJeu < 8 or tailleJeu > 12:
    print("Erreur : La taille doit être entre 8 et 12.")
    tailleJeu = int(input("Taille du plateau (entre 8 et 12) : "))

alignement = int(input("Nombre d'alignement pour gagner (entre 4 et 6) : "))
while alignement < 4 or alignement > 6:
    print("Erreur : Le nombre d'alignement doit être entre 4 et 6.")
    alignement = int(input("Nombre d'alignement pour gagner (entre 4 et 6) : "))

game = GameInterface(tailleJeu)