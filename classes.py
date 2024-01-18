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


    def winCondition(self):                                                 # Méthode qui vérifie si un joueur a gagné
        boardSize = self.__boardSize                                        # Taille du plateau 
        rows, cols = boardSize, boardSize                                   # Nombre de lignes et de colonnes du plateau               
        currentPlayer = self.pion.getPlayer()                               # Joueur du pion

        # Vérification de la victoire horizontale
        for row in range(rows):                                             # Boucle qui parcourt les lignes du plateau
            for col in range(cols - alignement + 1):                        # Boucle qui parcourt les colonnes du plateau
                victoire = True                                             # assignation de la variable victoire à True pour chaque case
                for i in range(alignement):                                 # Boucle qui parcourt les cases alignées                    
                    if self.__Board[row][col + i] != currentPlayer + 1:     # Si la case d'apès n'est pas égale au joueur + 1 car pour la machine joueur = 0 ou 1 et pour l'humain joueur = 1 ou 2
                        victoire = False                                    # assignation de la variable victoire à False car il n'y a pas de victoire
                        break                                               # Sort de la boucle
                if victoire:                                                # Si victoire = True
                    print(f"Victoire horizontale détectée en ligne {row}, colonne {col} à {col + alignement - 1}") # Affiche la victoire horizontale
                    return True                                             # Retourne True pour la suite du programme

        # Vérification de la victoire verticale
        for row in range(rows - alignement + 1):                            # Boucle qui parcourt les lignes du plateau
            for col in range(cols):                                         # Boucle qui parcourt les colonnes du plateau    
                victoire = True                                             # assignation de la variable victoire à True pour chaque case    
                for i in range(alignement):                                 # Boucle qui parcourt les cases alignées
                    if self.__Board[row + i][col] != currentPlayer + 1:     # Si la case d'en dessous n'est pas égale au joueur + 1 car pour la machine joueur = 0 ou 1 et pour l'humain joueur = 1 ou 2
                        victoire = False                                    # assignation de la variable victoire à False car il n'y a pas de victoire
                        break                                               # Sort de la boucle
                if victoire:                                                # Si victoire = True
                    print(f"Victoire verticale détectée en ligne {row}, à {row + alignement - 1}, colonne {col}") # Affiche la victoire verticale
                    return True                                             # Retourne True pour la suite du programme

        # Vérification de la victoire diagonale (\\)
        for row in range(rows - alignement + 1):                            # Boucle qui parcourt les lignes du plateau
            for col in range(cols - alignement + 1):                        # Boucle qui parcourt les colonnes du plateau   
                victoire = True                                             # assignation de la variable victoire à True pour chaque case
                for i in range(alignement):                                 # Boucle qui parcourt les cases alignées
                    if self.__Board[row + i][col + i] != currentPlayer + 1: # Si la case d'apres, en dessous est pas égale au joueur + 1 car pour la machine joueur = 0 ou 1 et pour l'humain joueur = 1 ou 2
                        victoire = False                                    # assignation de la variable victoire à False car il n'y a pas de victoire  
                        break                                               # Sort de la boucle
                if victoire:                                                # Si victoire = True
                    print(f"Victoire diagonale (\\) détectée de ({row}, {col}) à ({row + alignement - 1}, {col + alignement - 1})") # Affiche la victoire diagonale (\\)
                    return True                                             # Retourne True pour la suite du programme

        # Vérification de la victoire diagonale (//)
        for row in range(alignement - 1, rows):                             # Boucle qui parcourt les lignes du plateau
            for col in range(cols - alignement + 1):                        # Boucle qui parcourt les colonnes du plateau
                victoire = True                                             # assignation de la variable victoire à True pour chaque case
                for i in range(alignement):                                 # Boucle qui parcourt les cases alignées
                    if self.__Board[row - i][col + i] != currentPlayer + 1: # Si la case d'après, au dessus est pas égale au joueur + 1 car pour la machine joueur = 0 ou 1 et pour l'humain joueur = 1 ou 2
                        victoire = False                                    # assignation de la variable victoire à False car il n'y a pas de victoire
                        break                                               # Sort de la boucle
                if victoire:                                                # Si victoire = True
                    print(f"Victoire diagonale (//) détectée de ({row}, {col}) à ({row - alignement + 1}, {col + alignement - 1})") # Affiche la victoire diagonale (//)
                    return True                                             # Retourne True pour la suite du programme

        return False                                                        # Retourne False si il n'y a pas de victoire
    
    
    def updateBoard(self, x, y, nbCoups):                                   # Méthode qui met à jour le plateau
        currentPlayer = self.pion.getPlayer()                               # Joueur du pion
        if nbCoups > 1 and (x, y) not in self.possibleMoves[currentPlayer]: # Si le nombre de coups est supérieur à 1 et que les coordonnées ne sont pas dans les mouvements possibles
            return False                                                    # Retourne False

        if (x, y) in self.moveCondition() or nbCoups <= 1:                  # Si les coordonnées sont dans les mouvements possibles ou si le nombre de coups est inférieur ou égal à 1
            self.__Board[x][y] = currentPlayer + 1                          # Met à jour le plateau
            self.pion.setX(x)                                               # Met à jour l'abscisse du pion
            self.pion.setY(y)                                               # Met à jour l'ordonnée du pion    
            nbCoups += 1                                                    # Incrémente le nombre de coups                     
            return True                                                     # Retourne True      
        return False                                                        # Retourne False si il n'y a pas de victoire
    

class GameInterface:                                                        # Classe GameInterface  
    def __init__(self, boardSize):                                          # Constructeur de la classe GameInterface                         
        self.boardSize = boardSize                                          # Taille du plateau               
        self.pion = Pion()                                                  # Pion du jeu
        self.jeu = Jeu(boardSize, self.pion)                                # Jeu                               
        self.nbCoups = 0                                                    # Nombre de coups                               
        self.lastButton1 = None                                             # Dernier bouton du joueur 1    
        self.lastButton2 = None                                             # Dernier bouton du joueur 2

        self.window = Tk()                                                  # Fenêtre du jeu                              
        self.window.title("Jeu de Puissance 5")                             # Titre de la fenêtre                                
        self.window.config(padx=20, pady=20, highlightthickness=0, bd=0, bg="black") # Configuration de la fenêtre

        self.__frame1 = Frame(self.window)                                  # Frame du plateau                            
        self.__frame1.grid(row=0, column=0, rowspan=2)                      # Configuration du frame du plateau                    
        self.__frame1.config(pady=20, bg="black")                           # Configuration du frame du plateau                        

        self.__frame2 = Frame(self.window)                                  # Frame du joueur                 
        self.__frame2.grid(row=boardSize, column=0)                         # Configuration du frame du joueur               
        self.__frame2.config(padx=2, pady=2)                                # Configuration du frame du joueur              

        self.__nbText = StringVar()                                         # Texte du joueur   
        self.__nbText.set("Player " + str(self.pion.getPlayer() + 3))       # Texte du joueur
        self.__text1 = Label(self.__frame2, textvariable=self.__nbText, width=10, height=2, bg='black', fg='white') # Configuration du texte du joueur
        self.__text1.pack()                                                 # Configuration du texte du joueur                           
        self.buttons = [[Button(self.__frame1, width=6, height=3, bg='black', command=lambda i=i, j=j: self.placePion(i, j)) for j  in range(boardSize)] for i in range(boardSize)] # Configuration des boutons du plateau
        for i in range(boardSize):                                          # Boucle qui parcourt les lignes du plateau
            for j in range(boardSize):                                      # Boucle qui parcourt les colonnes du plateau
                self.buttons[i][j].grid(row=i, column=j)                    # Configuration des boutons du plateau
        self.debutJeu()                                                     # Début du jeu  

        self.window.mainloop()                                              # Boucle principale de la fenêtre

    def debutJeu(self):                                                     # Méthode qui démarre le jeu
        print("Début du jeu. Les joueurs peuvent placer leur premier pion où ils veulent.") # Affiche le début du jeu
        
    def disableButtons(self):                                               # Méthode qui désactive les boutons
        for row in self.buttons:                                            # Boucle qui parcourt les lignes du plateau              
            for button in row:                                              # Boucle qui parcourt les boutons du plateau
                button.config(state=DISABLED)                               # Désactive les boutons du plateau

    def finJeu(self):                                                       # Méthode qui vérifie si un joueur a gagné
        if self.jeu.winCondition() == True:                                 # Si un joueur a gagné
            print("Player " + str(self.pion.getPlayer() + 1) + " wins !")   # Affiche le joueur qui a gagné
            self.disableButtons()                                           # Désactive les boutons

    def restoreColor(self, x, y):                                           # Méthode qui restaure la couleur des boutons
        self.buttons[x][y].config(bg='black')                               # Restaure la couleur des boutons

    def changeColorPlayer1(self):                                           # Méthode qui change la couleur du bouton du joueur 1
        self.lastButton1.config(bg='green')                                 # Change la couleur du bouton du joueur 1

    def changeColorPlayer2(self):                                           # Méthode qui change la couleur du bouton du joueur 2
        self.lastButton2.config(bg='blue')                                  # Change la couleur du bouton du joueur 2
    
    
    def placePion(self, x, y):                                              # Méthode qui place le pion
        currentPlayer = self.pion.getPlayer()                               # Joueur du pion
        coupValide = False                                                  # Variable qui vérifie si le coup est valide

        if self.nbCoups < 2:                                                # Si le nombre de coups est inférieur à 2 (pour le premier et deuxième coup)
            self.pion.setX(x)                                               # Met à jour l'abscisse du pion
            self.pion.setY(y)                                               # Met à jour l'ordonnée du pion
            if currentPlayer == 0:                                          # Si le joueur est le joueur 1
                self.buttons[x][y].config(bg='#3FEE3C')                     # Change la couleur du bouton du joueur 1
                self.lastButton1 = self.buttons[x][y]                       # Dernier bouton du joueur 1
            else:                                                           # Sinon
                self.buttons[x][y].config(bg='#2ddff3')                     # Change la couleur du bouton du joueur 2
                self.lastButton2 = self.buttons[x][y]                       # Dernier bouton du joueur 2
            self.jeu.coords[currentPlayer] = [(x, y)]                       # Met à jour les coordonnées du joueur
            self.jeu.possibleMoves[currentPlayer] = []                      # Met à jour les mouvements possibles du joueur
            self.jeu.possibleMoves[currentPlayer] = self.jeu.moveCondition()# Met à jour les mouvements possibles du joueur   
            coupValide = True                                               # Le coup est valide
        else:                                                               # Sinon
            if self.jeu.updateBoard(x, y, self.nbCoups):                    # Si le plateau est mis à jour
                if currentPlayer == 0:                                      # Si le joueur est le joueur 1
                    self.buttons[x][y].config(bg='#3FEE3C')                 # Change la couleur du bouton du joueur 1
                    self.changeColorPlayer1()                               # Change la couleur du bouton du joueur 1
                    self.lastButton1 = self.buttons[x][y]                   # Dernier bouton du joueur 1
                else:                                                       # Sinon
                    self.buttons[x][y].config(bg='#2ddff3')                 # Change la couleur du bouton du joueur 2
                    self.changeColorPlayer2()                               # Change la couleur du bouton du joueur 2
                    self.lastButton2 = self.buttons[x][y]                   # Dernier bouton du joueur 2
                self.jeu.coords[currentPlayer] = [(x, y)]                   # Met à jour les coordonnées du joueur
                self.jeu.possibleMoves[currentPlayer] = []                  # Met à jour les mouvements possibles du joueur
                self.jeu.possibleMoves[currentPlayer] = self.jeu.moveCondition() # Met à jour les mouvements possibles du joueur
                coupValide = True                                           # Le coup est valide
            else:                                                           # Sinon
                self.buttons[x][y].config(bg='red')
                self.buttons[x][y].after(600, lambda: self.restoreColor(x, y)) # Restaure la couleur du bouton
                print("Mouvement invalide, veuillez réessayer.")            # Affiche un message d'erreur

        if coupValide == True:                                              # Si le coup est valide
            currentPlayer = self.pion.getPlayer()                           # Joueur du pion
            self.pion.updatePlayer()                                        # Met à jour le joueur du pion
            self.nbCoups += 1                                               # Incrémente le nombre de coups
            self.__nbText.set(f"Player {currentPlayer + 1}")                # Met à jour le texte du joueur
            self.finJeu()                                                   # Vérifie si un joueur a gagné 
            
        
        
            
                
tailleJeu = int(input("Taille du plateau (entre 8 et 12) : "))              # Taille du plateau
while tailleJeu < 8 or tailleJeu > 12:                                      # Boucle qui vérifie si la taille du plateau est entre 8 et 12
    print("Erreur : La taille doit être entre 8 et 12.")                    # Affiche une erreur
    tailleJeu = int(input("Taille du plateau (entre 8 et 12) : "))          # Taille du plateau

alignement = int(input("Nombre d'alignement pour gagner (entre 4 et 6) : "))    # Nombre d'alignement pour gagner
while alignement < 4 or alignement > 6:                                         # Boucle qui vérifie si le nombre d'alignement est entre 4 et 6
    print("Erreur : Le nombre d'alignement doit être entre 4 et 6.")            # Affiche une erreur
    alignement = int(input("Nombre d'alignement pour gagner (entre 4 et 6) : "))# Nombre d'alignement pour gagner

game = GameInterface(tailleJeu)                                                 # Démarre le jeu