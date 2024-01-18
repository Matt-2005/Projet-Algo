from tkinter import *                                                       # Importation de la bibliothèque tkinter

class Pion:                                                                 # Classe Pion                                        
    def __init__(self, abscisse = -1, ordonnee = -1, player = 0):           # Constructeur de la classe Pion
        self.__x = abscisse                                                 # Abscisse du pion
        self.__y = ordonnee                                                 # Ordonnée du pion
        self.__player = player                                              # Joueur du pion                          

    def getX(self):                                                         # Getter de l'abscisse du pion                               
        return self.__x                                                     # Retourne l'abscisse du pion
    def getY(self):                                                         # Getter de l'ordonnée du pion
        return self.__y                                                     # Retourne l'ordonnée du pion                 

    def setX(self, newX):                                                   # Setter de l'abscisse du pion                                  
        self.__x = newX                                                     # Modifie l'abscisse du pion
    def setY(self, newY):                                                   # Setter de l'ordonnée du pion                     
        self.__y = newY                                                     # Modifie l'ordonnée du pion

    def getPlayer(self):                                                    # Getter du joueur du pion
        return self.__player                                                # Retourne le joueur du pion

    def setPlayer(self, newPlayer):                                         # Setter du joueur du pion
        self.__player = newPlayer                                           # Modifie le joueur du pion

    def updatePlayer(self):                                                 # Méthode qui change le joueur du pion
        self.__player = (self.__player + 1) % 2                             # Modifie le joueur du pion


class Jeu:                                                                  # Classe Jeu
    def __init__(self, boardSize, pion):                                    # Constructeur de la classe Jeu
        self.__boardSize = boardSize                                        # Taille du plateau             
        self.pion = pion                                                    # Pion du jeu                       
        self.__Board = self.plateau(boardSize)                              # Plateau du jeu       
        self.coords = {0: [], 1: []}                                        # Coordonnées des pions des joueurs                      
        self.possibleMoves = {0: [], 1: []}                                 # Mouvements possibles des joueurs                      


    def plateau(self, boardSize):                                           # Méthode qui crée le plateau du jeu
        board = []                                                          # Liste qui contiendra le plateau                         
        for i in range(boardSize):                                          # Boucle qui parcourt les lignes du plateau               
            line = []                                                       # Liste qui contiendra les lignes du plateau
            for j in range(boardSize):                                      # Boucle qui parcourt les colonnes du plateau                 
                line.append(0)                                              # Ajoute un 0 à la ligne  
            board.append(line)                                              # Ajoute la ligne au plateau
        return board                                                        # Retourne le plateau


    def moveCondition(self):                                                # Méthode qui vérifie les mouvements possibles
        currentPlayer = self.pion.getPlayer()                               # Joueur du pion
        if currentPlayer in self.coords:                                    # Si le joueur a déjà placé un pion
            coords_player = self.coords[currentPlayer]                      # coord = coordonnées du pion du joueur
            x = coords_player[0][0]                                         # Abscisse du pion du joueur    
            y = coords_player[0][1]                                         # Ordonnée du pion du joueur
        else:                                                               # Sinon                                
            x, y = -1, -1                                                   # Abscisse et ordonnée du pion du joueur = -1 = Erreur

        possibleCoords = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]               # Liste des mouvements possibles
        for possibleCoordsX, possibleCoordsY in possibleCoords:                                                 # Boucle qui parcourt les mouvements possibles   
            newX, newY = x + possibleCoordsX, y + possibleCoordsY                                               # Nouvelles coordonnées du pion du joueur
            if 0 <= newX < self.__boardSize and 0 <= newY < self.__boardSize and self.__Board[newX][newY] == 0: # Si les coordonnées sont dans le plateau et que la case est vide
                self.possibleMoves[currentPlayer].append((newX, newY))                                          # Ajoute les coordonnées à la liste des mouvements possibles
        return self.possibleMoves[currentPlayer]                                                                # Retourne la liste des mouvements possibles


    def winCondition(self):
        boardSize = self.__boardSize
        rows, cols = boardSize, boardSize
        currentPlayer = self.pion.getPlayer()

        # Vérification horizontale
        for row in range(rows):
            for col in range(cols - alignement + 1):
                victoire = True
                for i in range(alignement):
                    if self.__Board[row][col + i] != currentPlayer + 1:
                        victoire = False
                        break
                if victoire:
                    print(f"Victoire horizontale détectée en ligne {row}, colonne {col} à {col + alignement - 1}")
                    return True

        # Vérification verticale
        for row in range(rows - alignement + 1):
            for col in range(cols):
                victoire = True
                for i in range(alignement):
                    if self.__Board[row + i][col] != currentPlayer + 1:
                        victoire = False
                        break
                if victoire:
                    print(f"Victoire verticale détectée en ligne {row} à {row + alignement - 1}, colonne {col}")
                    return True

        # Vérification diagonale (\)
        for row in range(rows - alignement + 1):
            for col in range(cols - alignement + 1):
                victoire = True
                for i in range(alignement):
                    if self.__Board[row + i][col + i] != currentPlayer + 1:
                        victoire = False
                        break
                if victoire:
                    print(f"Victoire diagonale (\\) détectée de ({row}, {col}) à ({row + alignement - 1}, {col + alignement - 1})")
                    return True

        # Vérification diagonale (/)
        for row in range(alignement - 1, rows):
            for col in range(cols - alignement + 1):
                victoire = True
                for i in range(alignement):
                    if self.__Board[row - i][col + i] != currentPlayer + 1:
                        victoire = False
                        break
                if victoire:
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
        self.__nbText.set("Player " + str(self.pion.getPlayer() + 3))
        self.__text1 = Label(self.__frame2, textvariable=self.__nbText, width=10, height=2, bg='black', fg='white')
        self.__text1.pack()
        self.buttons = [[Button(self.__frame1, width=6, height=3, bg='black', command=lambda i=i, j=j: self.placePion(i, j)) for j  in range(boardSize)] for i in range(boardSize)]
        for i in range(boardSize):
            for j in range(boardSize):
                self.buttons[i][j].grid(row=i, column=j)
        self.debutJeu()

        self.window.mainloop()

    def debutJeu(self):
        print("Début du jeu. Les joueurs peuvent placer leur premier pion où ils veulent.")
        
    def disableButtons(self):
        for row in self.buttons:
            for button in row:
                button.config(state=DISABLED)

    def finJeu(self):
        if self.jeu.winCondition() == True:
            print("Player " + str(self.pion.getPlayer() + 1) + " wins !")
            self.disableButtons()

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
                self.buttons[x][y].config(bg='#2ddff3')
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
                    self.buttons[x][y].config(bg='#2ddff3')
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