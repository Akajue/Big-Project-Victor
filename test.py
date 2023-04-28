import pygame
import random
import sys



BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
VIOLET = (210, 130, 238)
VIOLETF = (200, 130, 238)
GRIS = (128, 128, 128)


pygame.init()


LARGEUR_GRILLE = 20
HAUTEUR_GRILLE = 20


TAILLE_CASE = 20


largeur_ecran = LARGEUR_GRILLE * TAILLE_CASE
hauteur_ecran = HAUTEUR_GRILLE * TAILLE_CASE + 50
ECRAN = pygame.display.set_mode((largeur_ecran, hauteur_ecran))


police_score = pygame.font.Font(None, 30)


position_score = (10, hauteur_ecran - 40)


jeu_actif = False
direction = [0, 0]
tete = [LARGEUR_GRILLE // 2, HAUTEUR_GRILLE // 2]
corps = [tete[:]]
nourriture = [random.randint(0, LARGEUR_GRILLE - 1), random.randint(0, HAUTEUR_GRILLE - 1)]
score = 0


taille_bouton = (200, 50)
position_bouton = ((largeur_ecran - taille_bouton[0]) // 2, (hauteur_ecran - taille_bouton[1]) // 2)
bouton_start = pygame.Rect(position_bouton, taille_bouton)


def afficher_score():
    texte_score = police_score.render(f"Score: {score}", True, VIOLET)
    ECRAN.blit(texte_score, position_score)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not jeu_actif and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if bouton_start.collidepoint(event.pos):
                jeu_actif = True
                direction = [0, -1]
                tete = [LARGEUR_GRILLE // 2, HAUTEUR_GRILLE // 2]
                corps = [tete[:]]
                nourriture = [random.randint(0, LARGEUR_GRILLE - 1), random.randint(0, HAUTEUR_GRILLE - 1)]
                score = 0
        elif jeu_actif and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != [0, 1]:
                direction = [0, -1]
            elif event.key == pygame.K_DOWN and direction != [0, -1]:
                direction = [0, 1]
            elif event.key == pygame.K_LEFT and direction != [1, 0]:
                direction = [-1, 0]
            elif event.key == pygame.K_RIGHT and direction != [-1, 0]:
                direction = [-1, 0]



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not jeu_actif and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if bouton_start.collidepoint(event.pos):
                    jeu_actif = True
                    direction = [0, -1]
                    tete = [LARGEUR_GRILLE // 2, HAUTEUR_GRILLE // 2]
                    corps = [tete[:]]
                    nourriture = [random.randint(0, LARGEUR_GRILLE - 1), random.randint(0, HAUTEUR_GRILLE - 1)]
                    score = 0
            elif jeu_actif and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != [0, 1]:
                    direction = [0, -1]
                elif event.key == pygame.K_DOWN and direction != [0, -1]:
                    direction = [0, 1]
                elif event.key == pygame.K_LEFT and direction != [1, 0]:
                    direction = [-1, 0]
                elif event.key == pygame.K_RIGHT and direction != [-1, 0]:
                    direction = [1, 0]

        ECRAN.fill(GRIS)

        if not jeu_actif:
            pygame.draw.rect(ECRAN, VIOLET, bouton_start)
            police_bouton = pygame.font.Font(None, 30)
            texte_bouton = police_bouton.render("Start", True, NOIR)
            position_texte_bouton = (bouton_start.centerx - texte_bouton.get_width() // 2,
                                    bouton_start.centery - texte_bouton.get_height() // 2)
            ECRAN.blit(texte_bouton, position_texte_bouton)
        else:
            tete = [tete[0] + direction[0], tete[1] + direction[1]]
            if tete[0] < 0 or tete[0] >= LARGEUR_GRILLE or tete[1] < 0 or tete[1] >= HAUTEUR_GRILLE:
                jeu_actif = False
            elif tete in corps:
                jeu_actif = False
            else:
                corps.insert(0, tete[:])
                if tete == nourriture:
                    nourriture = [random.randint(0, LARGEUR_GRILLE - 1), random.randint(0, HAUTEUR_GRILLE - 1)]
                    score += 1
                else:
                    corps.pop()

                pygame.draw.rect(ECRAN, NOIR, [nourriture[0] * TAILLE_CASE, nourriture[1] * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE])

                for segment in corps:
                    pygame.draw.rect(ECRAN, VIOLETF, [segment[0] * TAILLE_CASE, segment[1] * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE])

                afficher_score()

        pygame.display.flip()
        pygame.time.Clock().tick(10)
