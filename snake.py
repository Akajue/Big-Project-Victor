import pygame
import random

# Initialisation de Pygame
pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VIOLET = (210, 130, 238)
GRIS = (128, 128, 128)

# Définition de la taille de la fenêtre
TAILLE_ECRAN = largeur, hauteur = 640, 480
ECRAN = pygame.display.set_mode(TAILLE_ECRAN)

# Définition de la taille de la grille
TAILLE_CASE = 10
LARGEUR_GRILLE = largeur // TAILLE_CASE
HAUTEUR_GRILLE = hauteur // TAILLE_CASE

# Initialisation de la tête du serpent et de sa direction
tete = [LARGEUR_GRILLE // 2, HAUTEUR_GRILLE // 2]
direction = [1, 0]

# Initialisation du corps du serpent
corps = [tete[:]]

# Initialisation de la nourriture
nourriture = [random.randint(0, LARGEUR_GRILLE - 1), random.randint(0, HAUTEUR_GRILLE - 1)]

# Définition de la police d'écriture
police = pygame.font.SysFont(None, 25)

# Définition de la fonction pour afficher le score
def afficher_score():
    score = len(corps) - 1
    texte_score = police.render("Score: " + str(score), True, NOIR)
    ECRAN.blit(texte_score, (10, 10))

# Boucle principale du jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != [0, 1]:
                direction = [0, -1]
            elif event.key == pygame.K_DOWN and direction != [0, -1]:
                direction = [0, 1]
            elif event.key == pygame.K_LEFT and direction != [1, 0]:
                direction = [-1, 0]
            elif event.key == pygame.K_RIGHT and direction != [-1, 0]:
                direction = [1, 0]

    # Déplacement de la tête du serpent
    tete[0] += direction[0]
    tete[1] += direction[1]

    # Vérification des collisions
    if tete[0] < 0 or tete[0] >= LARGEUR_GRILLE or tete[1] < 0 or tete[1] >= HAUTEUR_GRILLE or tete in corps:
        pygame.quit()
        sys.exit()

    # Ajout de la tête du serpent au corps
    corps.insert(0, tete[:])

    # Vérification si le serpent a mangé la nourriture
    if tete == nourriture:
        nourriture
        while nourriture in corps:
            nourriture = [random.randint(0, LARGEUR_GRILLE - 1), random.randint(0, HAUTEUR_GRILLE - 1)]

    else:
        corps.pop()

    # Effacement de l'écran
    ECRAN.fill(GRIS)

    # Affichage du serpent
    for partie in corps:
        pygame.draw.rect(ECRAN, VIOLET, (partie[0] * TAILLE_CASE, partie[1] * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

    # Affichage de la nourriture
    pygame.draw.rect(ECRAN, NOIR, (nourriture[0] * TAILLE_CASE, nourriture[1] * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

    # Affichage du score
    afficher_score()

    # Actualisation de l'écran
    pygame.display.flip()

    # Pause pour que le jeu ne soit pas trop rapide
    pygame.time.wait(50)
