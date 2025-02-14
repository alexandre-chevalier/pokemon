import pygame
import os

pygame.init()
pygame.font.init()

BASE_DIR = r"C:/Users/Windows/Desktop/projets/1a/pokemon"
font_path = os.path.join(BASE_DIR, "Audiowide-Regular.ttf")

try:
    test_font = pygame.font.Font(font_path, 70)
    print("La police a été chargée avec succès !")
except pygame.error as e:
    print(f"Erreur lors du chargement de la police : {e}")