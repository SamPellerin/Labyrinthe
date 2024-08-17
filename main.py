# Auteurs: Samuel Pellerin
# Date: 26 octobre 2023
#
# Ce programme nous permet, en tant que programmeur travaillant pour
# une bibliothèque de code, de générer aléatoirement des labyrinthes de tailles
# prédéfinies. Ce programme permet également de démontrer la validité de
# l'algorithme de Pledge, en dessinant en rouge, dans le labyrinthe généré, le
# chemin emprunté par un robot qui utiliserait l'algorithme en question
# afin de sortir du labyrinthe.

###############################################################################


# La fonction xCord prend en paramètres le numéro de la case et la
# largeur du labyrinthe et renvoie la coordonée en x de la case.


def xCord(numCell, largeur):
    return numCell % largeur


# La fonction yCord prend en paramètres le numéro de la case et la
# largeur du labyrinthe et renvoie la coordonée en y de la case.


def yCord(numCell, largeur):
    return numCell // largeur


# La fonction murN prend en paramètres le numéro de la case et la largeur
# du labyrinthe et renvoie la coordonée du mur horizontal au nord de la case.


def murN(numCell):
    return numCell


# La fonction murE prend en paramètres le numéro de la case et la largeur
# du labyrinthe et renvoie la coordonée du mur vertical à l'est de la case.


def murE(numCell, largeur):
    return 1 + xCord(numCell, largeur) + yCord(numCell, largeur) *\
    (largeur + 1)


# La fonction murS prend en paramètres le numéro de la case et la largeur
# du labyrinthe et renvoie la coordonée du mur horizontal au sud de la case.


def murS(numCell, largeur):
    return xCord(numCell, largeur) + (yCord(numCell, largeur) + 1) * largeur


# La fonction murO prend en paramètres le numéro de la case et la largeur
# du labyrinthe et renvoie la coordonée du mur vertical à l'ouest de la case.


def murO(numCell, largeur):
    return xCord(numCell, largeur) + yCord(numCell, largeur) * (largeur + 1)


def testMurEtCord():
    assert xCord(21, 8) == 5
    assert yCord(21, 8) == 2
    assert murN(21) == 21
    assert murE(21, 8) == 24
    assert murS(21, 8) == 29
    assert murO(21, 8) == 23
    assert xCord(3, 2) == 1
    assert yCord(3, 2) == 1
    assert murN(3) == 3
    assert murE(3,2) == 5
    assert murS(3,2) == 5
    assert murO(3,2) == 4


###############################################################################


# La fonction séquence prend en paramètre un nombre n, et retourne un
# tableau ayant n entiers (de 0 à n-1).


def sequence(n):
    return list(range(n))


def testSequence():
    assert sequence(5) == [0, 1, 2, 3, 4]
    assert sequence(1) == [0]
    assert sequence(0) == []


###############################################################################


# La fonction prend en paramètre un tableau et une valeur numérique, et
# retourne un booléen 'True' si le tableau contient la valeur, et 'False'
# dans le cas contraire.


def contient(tab, val):
    if val in tab:
        return True
    else:
        return False


def testContient():
    assert contient([0, 1, 2, 3, 4], 3) == True
    assert contient([], 0) == False
    assert contient([0], 0) == True
    assert contient([5, 7, 9], 8) == False


###############################################################################


# La fonction ajouter prend en paramètre un tableau et une valeur numérique
# et renvoie le même tableau, mais avec la valeur numérique ajoutée (si elle
# n'était pas déjà présente).


def ajouter(tab, val):
    if val not in tab:
        tab.append(val)
    return tab


def testAjouter():
    assert ajouter([2, 5, 7], 5) == [2, 5, 7]
    assert ajouter([2, 5, 9, 3], 6) == [2, 5, 9, 3, 6]
    assert ajouter([], 0) == [0]


###############################################################################


# La fonction retirer prend en paramètre un tableau et une valeur numérique
# et renvoie le même tableau mais sans la valeur specifiée.


def retirer(tab, val):
    if val in tab:
        tab.remove(val)
    return tab


def testRetirer():
    assert retirer([9, 2, 5], 2) == [9, 5]
    assert retirer([9, 2, 5], 4) == [9, 2, 5]
    assert retirer([], 69) == []
    assert retirer([0], 0) == []


###############################################################################


# La fonction voisins prend en paramètre la hauteur et largeur du labyrinthe
# et les coordonnées d'une case, et renvoies le numéro des cases voisines
# dans un tableau.


def voisins(xCordCell, yCordCell, largeur, hauteur):
    numCell = yCordCell * largeur + xCordCell
    numCellHaut = numCell - largeur
    numCellBas = numCell + largeur
    numCellGauche = numCell - 1
    numCellDroite = numCell + 1
    voisins = []
    if numCellHaut > -1: 
        voisins.append(numCellHaut)
    if yCordCell == yCord(numCellGauche,largeur):
        voisins.append(numCellGauche)
    if numCellBas < largeur * hauteur:
        voisins.append(numCellBas)
    if yCordCell == yCord(numCellDroite,largeur):
        voisins.append(numCellDroite)
    return voisins


def testvoisins():
    assert voisins(7, 2, 8, 4) == [15, 22, 31]
    assert voisins(4, 1, 5, 2) == [4, 8]
    assert voisins(0, 0, 1, 1) == []
    assert voisins(0, 3, 3, 6) == [6, 12, 10]


###############################################################################


# La fonction position intersectionAleatoire est inspiré de la
# solution de l'ex6 de la démonstration 6. La fonction prend en paramètre
# 2 tableaux et retourne un élément aleatoire de l'intersection.


def intersectionAleatoire(tab1, tab2):
    intersection = []                  # tableau résultant
    for i in range(len(tab1)):         # pour tous les éléments de tab1
        elem = tab1[i]
        if elem in tab2:
            ajouter(intersection,elem)  
    if len(intersection) == 0:
        return None
    else:
        indiceAleatoire = math.floor(random() * len(intersection))
        elemAleatoire = intersection[indiceAleatoire]
    return elemAleatoire


def testIntersectionAleatoire():
    assert intersectionAleatoire([3, 1, 4, 1, 5], [2, 4, 4, 3]) == 3 or 4
    assert intersectionAleatoire([-3, 1, 0, 1, 5], [2, 4, 4, -3]) == -3
    assert intersectionAleatoire([1, 2, 3], [4, 5, 6]) == None


###############################################################################


# La fonction retirerMurCommun prend en paramètres 2 numéro de case que
# nous savons voisines, la largeur du labyrinthe et les tableaux contenant
# les numéros des murs verticaux et horizontaux, et renvoie le tableau (soit
# horiz ou verti) qui contient le mur en commun aux 2 cases, mais en
# retirant ce mur.


def retirerMurCommun(numCase1, numCase2, largeur, horiz, verti):
    if murN(numCase1) == murS(numCase2, largeur):
        horiz = retirer(horiz, murN(numCase1))
        return horiz
    elif murS(numCase1, largeur) == murN(numCase2):
        horiz = retirer(horiz, murN(numCase2))
        return horiz
    elif murE(numCase1, largeur) == murO(numCase2, largeur):
        verti = retirer(verti, murE(numCase1, largeur))
        return verti
    else:
        verti = retirer(verti, murE(numCase2, largeur))
        return verti


def testMurCommun():
    assert retirerMurCommun(12, 20, 8, sequence(40), sequence(35)) == retirer(
        sequence(40), 20
    )
    assert retirerMurCommun(11, 12, 8, sequence(40), sequence(35)) == retirer(
        sequence(35), 13
    )
    assert retirerMurCommun(8, 7, 3, sequence(21), sequence(24)) == retirer(
        sequence(24), 10
    )


###############################################################################


# La fonction fondblanc prend en paramètres la largeur, hauteur et dimension
# du labyrinthe, et renvoie un écran avec le bon nombre de pixels blancs pour
# le labyrinthe désiré.


def fondblanc(largeur, hauteur, dimension):
    setScreenMode(
        (largeur * dimension) + largeur + 1, (hauteur * dimension) + hauteur 
        + 1)  # Nombre de pixels total.
    for i in range((largeur * dimension) + largeur + 1):
        for j in range((hauteur * dimension) + hauteur + 1):
            setPixel(i, j, "#FFF")

    return exportScreen()


def testFondBlanc():
    assert fondblanc(1, 1, 1) == "#fff#fff#fff\n#fff#fff#fff\n#fff#fff#fff"
    assert (
        fondblanc(1, 1, 2)
        == "#fff#fff#fff#fff\n#fff#fff#fff#fff\n" + 
        "#fff#fff#fff#fff\n#fff#fff#fff#fff"
    )
    assert (
        fondblanc(2, 1, 1)
        == "#fff#fff#fff#fff#fff\n#fff#fff#fff#fff#fff\n" + 
        "#fff#fff#fff#fff#fff"
    )


###############################################################################


# La fonction affichageHoriz prend en paramètre la dimension et largeur du
# labyrinthe, en plus du tableau avec tous les numéros de murs horizontaux
# qui doivent être affichés en noir, puis renvoie le fond blanc avec l'addition
# des murs horizontaux en noir.


def affichageHoriz(horiz, largeur, dimension):
    for i in range(1, len(horiz) - 1):
        # Chaque mur horizontal à une coordonnée en y fixe.
        yCordMur = (horiz[i] // largeur) * (dimension + 1)
        # On met en noir chaque point du mur.
        for j in range(dimension + 2):
            xCordPoint = (horiz[i] % largeur) * (dimension + 1) + j
            setPixel(xCordPoint, yCordMur, "#000")

    return exportScreen()


def testAffichageHoriz():
    fondblanc(2, 1, 1)
    assert (
        affichageHoriz(sequence(4), 2, 1)
        == "#fff#fff#000#000#000\n" 
        + "#fff#fff#fff#fff#fff\n#000#000#000#fff#fff"
    )
    fondblanc(2, 1, 2)
    assert (
        affichageHoriz(sequence(4), 2, 2)
        == "#fff#fff#fff#000#000#000#000\n"
        + "#fff#fff#fff#fff#fff#fff#fff\n#fff#fff#fff#fff#fff#fff#fff\n"
        + "#000#000"
        + "#000#000#fff#fff#fff"
    )


###############################################################################


# La fonction affichageVerti prend en paramètre la dimension et largeur du
# labyrinthe, en plus du tableau avec tous les numéros de murs verticaux
# qui doivent être affichés en noir, puis renvoie le fond blanc avec l'addition
# des murs verticaux en noir.


def affichageVerti(verti, largeur, dimension):
    for i in range(len(verti)):
        # Chaque mur vertical à une coordonnée en x fixe.
        xCordMur = (verti[i] % (largeur + 1)) * (dimension + 1)
        # On met en noir chaque point du mur.
        for j in range(dimension + 2):
            yCordPoint = (verti[i] // (largeur + 1)) * (dimension + 1) + j
            setPixel(xCordMur, yCordPoint, "#000")

    return exportScreen()


def testAffichageVerti():
    assert 2 == 2
    fondblanc(3, 1, 1)
    assert (
        affichageVerti(sequence(4), 3, 1)
        == "#000#fff#000#fff#000#fff#000\n"
        + "#000#fff#000#fff#000#fff#000\n#000#fff#000#fff#000#fff#000"
    )
    fondblanc(3, 1, 2)
    assert (
        affichageVerti(sequence(4), 3, 2)
        == "#000#fff#fff#000#fff#fff#000"
        + "#fff#fff#000\n#000#fff#fff#000#fff#fff#000#fff#fff#000\n#000#fff"
        + "#fff#000#fff#fff#000#fff#fff#000\n#000#fff#fff#000#fff#fff#000#fff" 
        + "#fff#000"
    )


###############################################################################


# La fonction laby prend en paramètre la largeur, hauteur et dimension désirés
# d'un labyrinthe,et imprime sur un écran le labyrinthe désiré.


def laby(largeur, hauteur, dimension):
    numOfCases = largeur * hauteur
    numOfVerti = (largeur + 1) * hauteur
    numOfHoriz = largeur * (hauteur + 1)
    cave = []                        # Tableau avec élem. de la cavité
    front = []                       # Tableau avec élem. de la frontière
    verti = sequence(numOfVerti)     # Tableau avec murs verticaux
    horiz = sequence(numOfHoriz)     # Tableau avec murs horizontaux
    caseDeBase = math.floor(random() * numOfCases)
    ajouter(cave,caseDeBase)         # Cavité de départ
    frontDeBase = voisins(
        xCord(caseDeBase, largeur), yCord(caseDeBase, largeur), largeur, 
        hauteur)
    front.extend(frontDeBase)        # Frontières de départ
    
    # Jusqu'à temps que toutes les cases soient dans la cavité.
    while len(cave) != numOfCases:   
        indexAleatoire = math.floor(random() * len(front))
        caseAleatoire = front[indexAleatoire]
        cave.append(caseAleatoire)   # Ajouter nouvelle case dans la cavité
        front.remove(caseAleatoire)  # Retirer nouvelle case de la frontière
        voisinsCaseAleatoire = voisins(
            xCord(caseAleatoire, largeur),
            yCord(caseAleatoire, largeur),
            largeur,
            hauteur)
        
        # On trouve la case de la cavité voisine à la nouvelle case.
        caseAdjacente = intersectionAleatoire(cave, voisinsCaseAleatoire)
        # Enlever les éléments de la cavité qui sont voisines de
        # la nouvelle Case.
        for j in range(len(cave)):
            voisinsCaseAleatoire = retirer(voisinsCaseAleatoire, cave[j])
        # Les cases voisines de la nouvelle case qui sont pas déjà dans front
        # y sont ajoutées.
        for k in range(len(voisinsCaseAleatoire)):
            front = ajouter(front, voisinsCaseAleatoire[k])
        retirerMurCommun(caseAleatoire, caseAdjacente, largeur, horiz, verti)
        
    # Il ne reste plus qu'à afficher le labyrinthe.
    fondblanc(largeur, hauteur, dimension)
    affichageHoriz(horiz, largeur, dimension)
    affichageVerti(verti, largeur, dimension)


###############################################################################

# La fonction pledge prend la largeur, la hauteur et la dimension du labyrinthe
# en paramètre et fait appel à la fonction laby pour tracer le labyrinthe. Un
# chemin en rouge est ensuite tracé selon le chemin que prendrait un robot 
# suivant l'algorithme de Pledge. La fonction pledge possède la limite suivante
# sur le paramètre dimension: dimension>5.

def pledge(largeur, hauteur, dimension):
    laby(largeur, hauteur, dimension) # Traçage du labyrinthe.
    
    # Texte contenant la couleur de chaque pixel du labyrinthe.
    labyrinthe = exportScreen()
    
    # Initialisation d'un tableau qui va contenir les caractères définissant la
    # couleur de tous les pixels du labyrinthe.
    tableauCaracteres = []
    
    # Définition du numéro de rangée maximal et du numéro de colonne maximal.
    rangeeMax = hauteur * dimension + hauteur
    colonneMax = largeur * dimension + largeur
    
    # On itère sur les caractères du texte et on les insère dans le tableau.
    for i in labyrinthe:
        tableauCaracteres.append(i)
    
    # Initialisation de la matrice qui va contenir les valeurs de couleur pour 
    # chaque pixel du labyrinthe.
    tableau = []
    for i in range(rangeeMax + 1):
        tableau.append([])
    
    # On isole chaque valeur de couleur (ex: "#000") dans tableauCaracteres et
    # on les rajoute à l'index du pixel correspondant dans tableau. À chaque 
    # occurence de "\n", on change de rangée dans la matrice.
    numeroRangee = 0
    for i in range(len(tableauCaracteres)):
        if tableauCaracteres[i] == "\n":
            numeroRangee += 1

        if tableauCaracteres[i] == "#":
            tableau[numeroRangee].append(
                tableauCaracteres[i]
                + tableauCaracteres[i + 1]
                + tableauCaracteres[i + 2]
                + tableauCaracteres[i + 3]
            )
    
    # Initialisation de la position du robot, de la direction du robot et du
    # compteur de l'algorithme de Pledge. 
    
    # Position actuelle du robot, le point (0,0) correspond au coin en haut à
    # gauche du labyrinthe.
    xRobot = 3
    yRobot = 0
    # Tableaux retraçant l'historique de la position du robot.
    positionX = [3]
    positionY = [0]
    # Direction actuelle du robot (N: nord, S: sud, O: ouest, E: est).
    direction = "S"
    
    # Compteur de l'algorithme de Pledge, si le robot tourne à gauche, on 
    # additionne 1 au compteur, s'il tourne à droite, on soustrait 1.
    compteur = 0

    # On associe la couleur noire ("#000") aux pixels de l'entrée du labyrinthe 
    # afin que le robot traite l'entrée comme un mur, une fois l'algorithme 
    # entamé.
    for i in range(0, dimension + 1):
        tableau[0][i] = "#000"

        
    # Boucle principale de l'algorithme de Pledge. On sort de la boucle si la
    # position du Robot correspond à la sortie du labyrinthe, soit y=rangeeMax.
    # La boucle possède 4 conditions principales qui correspondent aux 4 
    # directions possibles du robot. Initialement, le robot se dirige en ligne
    # droite et quand il frappe un mur, il tourne soit à gauche, soit à droite.
    # Le robot se tient toujours à 3 pixels de chaque mur et quand le robot 
    # tourne, on ajuste sa direction et le compteur en conséquence. On 
    # identifie les coins et les murs par la couleur des pixels à une certaine
    # position relative au robot. Si la valeur de couleur des pixels dans
    # tableau est "#000", cela signifie que le pixel est noir et qu'il y a un
    # mur à cet endroit. Si la valeur est "#fff", le pixel est blanc et il y 
    # a du vide à cet endroit. 
    while yRobot != rangeeMax:
        if direction == "N":
            # Les deux énoncés suivants correspondent aux deux types de coins 
            # rencontrés par le robot dans cette étape de l'algorithme de
            # Pledge, soit des coins intérieurs.
            if (
                tableau[yRobot - 3][xRobot] == "#000"
                and tableau[yRobot][xRobot - 3] == "#000"
            ):
                direction = "E"
                compteur -= 1

            elif (
                tableau[yRobot - 3][xRobot] == "#000"
                and tableau[yRobot][xRobot + 3] == "#000"
            ):
                direction = "O"
                compteur += 1
            # Si le robot ne se retrouve pas dans un coin et qu'il rencontre
            # un mur en face, il choisit la droite ou la gauche de façon 
            # aléatoire.
            elif tableau[yRobot - 3][xRobot] == "#000":
                r = random()
                if r <= 0.5:
                    direction = "O"
                    compteur += 1
                else:
                    direction = "E"
                    compteur -= 1
            # Si le robot ne rencontre pas de mur ou de coin, il continue son
            # chemin dans sa direction et on ajuste sa position actuelle et 
            # les tableaux de position afin de tracer son chemin à la fin.
            else:
                yRobot -= 1
                positionY.append(yRobot)
                positionX.append(xRobot)

        elif direction == "S":
            # L'énoncé suivant correspond à une condition unique à la direction
            # sud où le robot se retrouve en bas à droite du labyrinthe, soit 
            # proche de la sortie. Cette condition existe pour ne pas indexer 
            # des coordonnées inexistantes dans les conditions de coin, une 
            # fois rendu à la fin du labyrinthe.
            if (
                yRobot >= rangeeMax - 3
                and xRobot <= colonneMax
                and xRobot >= colonneMax - dimension
            ):
                yRobot += 1
                positionY.append(yRobot)
                positionX.append(xRobot)
            
            # On utilise les mêmes conditions que pour la direction nord, mais
            # la valeur de l'indexation dans tableau, de la direction 
            # résultante du robot et celle du compteur sont ajustées.
            elif (
                tableau[yRobot + 3][xRobot] == "#000"
                and tableau[yRobot][xRobot - 3] == "#000"
            ):
                direction = "E"
                compteur += 1

            elif (
                tableau[yRobot + 3][xRobot] == "#000"
                and tableau[yRobot][xRobot + 3] == "#000"
            ):
                direction = "O"
                compteur -= 1

            elif tableau[yRobot + 3][xRobot] == "#000":
                r = random()
                if r <= 0.5:
                    direction = "O"
                    compteur -= 1
                else:
                    direction = "E"
                    compteur += 1

            else:
                yRobot += 1
                positionY.append(yRobot)
                positionX.append(xRobot)

        elif direction == "O":
            if (
                tableau[yRobot + 3][xRobot] == "#000"
                and tableau[yRobot][xRobot - 3] == "#000"
            ):
                direction = "N"
                compteur -= 1

            elif (
                tableau[yRobot - 3][xRobot] == "#000"
                and tableau[yRobot][xRobot - 3] == "#000"
            ):
                direction = "S"
                compteur += 1

            elif tableau[yRobot][xRobot - 3] == "#000":
                r = random()
                if r <= 0.5:
                    direction = "N"
                    compteur -= 1
                else:
                    direction = "S"
                    compteur += 1

            else:
                xRobot -= 1
                positionX.append(xRobot)
                positionY.append(yRobot)

        else:
            # Les conditions se retrouvant dans l´énoncé else ci-dessus 
            # correspondent au cas où la direction du robot est l'est.
            if (
                tableau[yRobot + 3][xRobot] == "#000"
                and tableau[yRobot][xRobot + 3] == "#000"
            ):
                direction = "N"
                compteur += 1

            elif (
                tableau[yRobot - 3][xRobot] == "#000"
                and tableau[yRobot][xRobot + 3] == "#000"
            ):
                direction = "S"
                compteur -= 1

            elif tableau[yRobot][xRobot + 3] == "#000":
                r = random()
                if r <= 0.5:
                    direction = "N"
                    compteur += 1
                else:
                    direction = "S"
                    compteur -= 1

            else:
                xRobot += 1
                positionX.append(xRobot)
                positionY.append(yRobot)
        
        # Si le compteur n'égale pas 0, on fait appel à la fonction 
        # pledgeIterationCompteur qui déterminera le chemin emprunté par le
        # robot lorsque le compteur n'est pas à 0 (deuxième étape de
        # l'algorithme de Pledge).
        if compteur != 0:
            (
                xRobot,
                yRobot,
                positionX,
                positionY,
                direction,
                compteur,
            ) = pledgeIterationCompteur(
                xRobot,
                yRobot,
                positionX,
                positionY,
                direction,
                compteur,
                tableau,
                rangeeMax,
                colonneMax,
                dimension,
            )
    
    # Quand le robot est sorti du labyrinthe, on trace son chemin en itérant
    # sur les index des tableaux de la position et on trace chaque pixel en 
    # rouge sur le labyrinthe. La valeur "#f00" correspond à la couleur rouge.
    for i in range(len(positionX)):
        setPixel(positionX[i], positionY[i], "#f00")

###############################################################################

# La fonction pledgeIterationCompteur prend tous les paramètres faisant 
# référence à la position et la direction du robot ainsi que les 
# caractéristiques du labyrinthe, soit le tableau des couleurs de chaque pixel
# les valeurs maximales de rangée et de colonnes et la dimension du tableau.
# Cette fonction va itérer jusqu'à ce que le compteur soit 0 où la position du
# robot soit équivalente à la sortie du labyrinthe. Dans la boucle figurent
# plusieurs conditions (selon la direction du robot) qui identifient les 4 
# types de coin rencontrés par le robot. Dans cette étape, le robot suit le mur
# de sa main droite ou sa main gauche selon sa direction. Il tourne quand il 
# rencontre un coin et si le compteur est à 0, on retourne les valeurs de
# position et de direction du robot, ainsi que la valeur du compteur. On 
# revient ensuite dans la boucle principale de l'algorithme de Pledge.
def pledgeIterationCompteur(
    xRobot,
    yRobot,
    positionX,
    positionY,
    direction,
    compteur,
    tableau,
    rangeeMax,
    colonneMax,
    dimension,
):
    while compteur != 0 and yRobot != rangeeMax:
        if direction == "N":
            # Les deux énoncés suivants correspondent à des coins 
            # extérieurs. On ajoute également une condition sur la position du
            # robot afin que le robot n'identifie pas le mur extérieur du 
            # labyrinthe comme un coin.
            if (
                yRobot != rangeeMax - 3
                and tableau[yRobot][xRobot - 3] == "#fff"
                and tableau[yRobot + 1][xRobot - 3] == "#fff"
                and tableau[yRobot + 2][xRobot - 3] == "#fff"
                and tableau[yRobot + 3][xRobot - 3] == "#000"
                and tableau[yRobot + 3][xRobot - 2] == "#fff"
            ):
                direction = "O"
                compteur += 1

            elif (
                yRobot != rangeeMax - 3
                and tableau[yRobot][xRobot + 3] == "#fff"
                and tableau[yRobot + 1][xRobot + 3] == "#fff"
                and tableau[yRobot + 2][xRobot + 3] == "#fff"
                and tableau[yRobot + 3][xRobot + 3] == "#000"
                and tableau[yRobot + 3][xRobot + 2] == "#fff"
            ):
                direction = "E"
                compteur -= 1
            
            # Les deux énoncés suivants correspondent à des coins intérieurs.
            # Ces coins sont du même type que ceux rencontrés dans la boucle
            # principale de l'algorithme de Pledge.
            elif (
                tableau[yRobot - 3][xRobot] == "#000"
                and tableau[yRobot][xRobot - 3] == "#000"
            ):
                direction = "E"
                compteur -= 1

            elif (
                tableau[yRobot - 3][xRobot] == "#000"
                and tableau[yRobot][xRobot + 3] == "#000"
            ):
                direction = "O"
                compteur += 1
            # Si le robot ne rencontre pas de coins, on ajuste sa position
            # selon sa direction et on ajoute la valeur de sa position aux 
            # tableaux de position.
            else:
                yRobot -= 1
                positionY.append(yRobot)
                positionX.append(xRobot)

        elif direction == "S":
            # On utilise les mêmes conditions que pour la direction nord, mais
            # la valeur de l'indexation dans tableau, de la direction 
            # résultante du robot et celle du compteur sont ajustées. On ajoute
            # également la condition unique à la direction sud (la même que 
            # dans la boucle principale) afin que le robot n'indexe pas de 
            # coordonnées inexistantes quand il est rendu à la fin du 
            # labyrinthe.
            if (
                yRobot >= rangeeMax - 3
                and xRobot <= colonneMax
                and xRobot >= colonneMax - dimension
            ):
                yRobot += 1
                positionY.append(yRobot)
                positionX.append(xRobot)
                
            elif (
                yRobot != 3
                and tableau[yRobot][xRobot - 3] == "#fff"
                and tableau[yRobot - 1][xRobot - 3] == "#fff"
                and tableau[yRobot - 2][xRobot - 3] == "#fff"
                and tableau[yRobot - 3][xRobot - 3] == "#000"
                and tableau[yRobot - 3][xRobot - 2] == "#fff"
            ):
                direction = "O"
                compteur -= 1

            elif (
                yRobot != 3
                and tableau[yRobot][xRobot + 3] == "#fff"
                and tableau[yRobot - 1][xRobot + 3] == "#fff"
                and tableau[yRobot - 2][xRobot + 3] == "#fff"
                and tableau[yRobot - 3][xRobot + 3] == "#000"
                and tableau[yRobot - 3][xRobot + 2] == "#fff"
            ):
                direction = "E"
                compteur += 1

            elif (
                tableau[yRobot + 3][xRobot] == "#000"
                and tableau[yRobot][xRobot - 3] == "#000"
            ):
                direction = "E"
                compteur += 1

            elif (
                tableau[yRobot + 3][xRobot] == "#000"
                and tableau[yRobot][xRobot + 3] == "#000"
            ):
                direction = "O"
                compteur -= 1

            else:
                yRobot += 1
                positionY.append(yRobot)
                positionX.append(xRobot)
                
        elif direction == "O":
            if (
                xRobot != colonneMax - 3
                and tableau[yRobot - 3][xRobot] == "#fff"
                and tableau[yRobot - 3][xRobot + 1] == "#fff"
                and tableau[yRobot - 3][xRobot + 2] == "#fff"
                and tableau[yRobot - 3][xRobot + 3] == "#000"
                and tableau[yRobot - 2][xRobot + 3] == "#fff"
            ):
                direction = "N"
                compteur -= 1

            elif (
                xRobot != colonneMax - 3
                and tableau[yRobot + 3][xRobot] == "#fff"
                and tableau[yRobot + 3][xRobot + 1] == "#fff"
                and tableau[yRobot + 3][xRobot + 2] == "#fff"
                and tableau[yRobot + 3][xRobot + 3] == "#000"
                and tableau[yRobot + 2][xRobot + 3] == "#fff"
            ):
                direction = "S"
                compteur += 1

            elif (
                tableau[yRobot + 3][xRobot] == "#000"
                and tableau[yRobot][xRobot - 3] == "#000"
            ):
                direction = "N"
                compteur -= 1

            elif (
                tableau[yRobot - 3][xRobot] == "#000"
                and tableau[yRobot][xRobot - 3] == "#000"
            ):
                direction = "S"
                compteur += 1

            else:
                xRobot -= 1
                positionX.append(xRobot)
                positionY.append(yRobot)

        else:
            # Les conditions se retrouvant dans l´énoncé else ci-dessus 
            # correspondent au cas où la direction du robot est l'est.
            if (
                xRobot != 3
                and tableau[yRobot - 3][xRobot] == "#fff"
                and tableau[yRobot - 3][xRobot - 1] == "#fff"
                and tableau[yRobot - 3][xRobot - 2] == "#fff"
                and tableau[yRobot - 3][xRobot - 3] == "#000"
                and tableau[yRobot - 2][xRobot - 3] == "#fff"
            ):
                direction = "N"
                compteur += 1

            elif (
                xRobot != 3
                and tableau[yRobot + 3][xRobot] == "#fff"
                and tableau[yRobot + 3][xRobot - 1] == "#fff"
                and tableau[yRobot + 3][xRobot - 2] == "#fff"
                and tableau[yRobot + 3][xRobot - 3] == "#000"
                and tableau[yRobot + 2][xRobot - 3] == "#fff"
            ):
                direction = "S"
                compteur -= 1

            elif (
                tableau[yRobot + 3][xRobot] == "#000"
                and tableau[yRobot][xRobot + 3] == "#000"
            ):
                direction = "N"
                compteur += 1

            elif (
                tableau[yRobot - 3][xRobot] == "#000"
                and tableau[yRobot][xRobot + 3] == "#000"
            ):
                direction = "S"
                compteur -= 1

            else:
                xRobot += 1
                positionX.append(xRobot)
                positionY.append(yRobot)
    
    # On retourne les valeurs reliées à la position du robot, sa direction et
    # la valeur du compteur quand on sort de la boucle.
    return xRobot, yRobot, positionX, positionY, direction, compteur

###############################################################################

# On effectue les tests unitaires sur les différentes fonctions utilisées pour
# créer le labyrinthe.
testAffichageVerti()
testAffichageHoriz()
testFondBlanc()
testMurCommun()
testMurEtCord()
testIntersectionAleatoire()
testvoisins()
testRetirer()
testAjouter()
testContient()
testSequence()

# On choisit de faire appel à la fonction laby pour afficher le labyrinthe ou
# la fonction pledge pour afficher le labyrinthe et le chemin emprunté par un
# robot utilisant l'algorithme de Pledge. On peut mettre une ligne ou l'autre
# en commentaire pour afficher seulement le résultat de la fonction voulue.

laby(10,9,20)
#pledge(10, 9, 20)
