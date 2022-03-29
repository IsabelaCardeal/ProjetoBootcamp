import pygame

print('Tô na area!!!')

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('musica.mp3')
# Escreva o nome do arquivo da música escolhida sempre em .mp3
pygame.mixer.music.play()
pygame.event.wait()
