# === Tek Shooter ===
#
# Projet complet: https://codingclubbordeaux.github.io/subject/tek-shooter

import pyxel

GAME_WIDTH = 120
GAME_HEIGHT = 160
PLAYER_WIDTH = 8
PLAYER_HEIGHT = 8
ENEMY_WIDTH = 8
ENEMY_HEIGHT = 8
PLAYER_SPEED = 2
BULLET_SPEED = 4
BULLET_WIDTH = 2
BULLET_HEIGHT = 8
BULLET_COLOR = 8

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = self.x - PLAYER_SPEED

        # TODO: Réparer le déplacement du joueur
        #
        # Touches de déplacement:
        # - Droite: pyxel.KEY_RIGHT
        # - Haut: pyxel.KEY_UP
        # - Bas: pyxel.KEY_DOWN
        #
        # ÉTAPE 2: Empêcher le joueur de se déplacer hors de la fenêtre
        #
        # Fonctions utiles:
        # - max(valeur, limite) => empêche la valeur de dépasser la limite
        # - min(valeur, limite) => empêche la valeur de passer la limite
        #
        # Constantes:
        # - PLAYER_SPEED: nombre de pixels par lequel déplacer le joueur
        # - GAME_WIDTH: largeur de la fenêtre
        # - GAME_HEIGHT: hauteur de la fenêtre
        # - PLAYER_WIDTH: largeur du joueur
        # - PLAYER_HEIGHT: hauteur du joueur
        #
        # Coordonnées:
        # - self.x: coordonnée horizontale du joueur
        # - self.y: coordonnée verticale du joueur
        #
        # La coordonnée (0,0) est le coin en haut à gauche de la fenêtre.

        if pyxel.btn(...):
            ...

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_alive = True

    def update(self):
        if self.is_alive:
            self.y += 1
            if self.y > GAME_HEIGHT:
                self.y = -ENEMY_HEIGHT

    def draw(self):
        if self.is_alive:
            pyxel.blt(self.x, self.y, 0, 8, 0, ENEMY_WIDTH, ENEMY_HEIGHT)

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_active = True

    def update(self):
        if self.is_active:
            self.y -= BULLET_SPEED
            if self.y < -BULLET_HEIGHT:
                self.is_active = False

    def draw(self):
        if self.is_active:
            pyxel.rect(self.x, self.y, BULLET_WIDTH, BULLET_HEIGHT, BULLET_COLOR)

class Game:
    def __init__(self):
        pyxel.init(GAME_WIDTH, GAME_HEIGHT, title="Tek Shooter")
        pyxel.load("shooter.pyxres")

        self.player = Player(GAME_WIDTH // 2, GAME_HEIGHT - PLAYER_HEIGHT - 10)
        self.enemies = [Enemy(0, 0), Enemy(50, 30), Enemy(100, 10)]
        self.bullets = []

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.player.update()


        # TODO: La joueur doit pouvoir tirer des projectiles en appuyant sur la
        # touche espace.
        #
        # Calcul de la position du projectile:
        # x: <position x du joueur> + <milieu du joueur> - <milieu du projectile>
        # y: <position y du joueur>
        #
        # Pour créer un projectile à la position (x, y), on utilise la fonction
        # Bullet(x, y).
        #
        # Il faut ajouter le projectile à la liste des projectiles avec
        # self.bullets.append(...)

        if pyxel.btnp(...):
            ...

        for enemy in self.enemies:
            enemy.update()

        for bullet in self.bullets:
            bullet.update()
            if bullet.is_active:
                for enemy in self.enemies:
                    if (enemy.is_alive and
                        bullet.x < enemy.x + ENEMY_WIDTH and
                        bullet.x + BULLET_WIDTH > enemy.x and
                        bullet.y < enemy.y + ENEMY_HEIGHT and
                        bullet.y + BULLET_HEIGHT > enemy.y):
                        enemy.is_alive = False
                        bullet.is_active = False
                        break

        self.bullets = [b for b in self.bullets if b.is_active]
        self.enemies = [e for e in self.enemies if e.is_alive]

    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
        for bullet in self.bullets:
            bullet.draw()

Game()
