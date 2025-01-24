# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()

NoTilesX = 16
NoTilesY = 16

ZoomMultiplier = 2
MoveValue = 2 * ZoomMultiplier

TileEdge = 16 * ZoomMultiplier

SpriteX = 16 * ZoomMultiplier
SpriteY = 32 * ZoomMultiplier

Jump = False
JumpIndex = 0

Screen = pygame.display.set_mode((TileEdge*NoTilesX, TileEdge*NoTilesY))
pygame.display.set_caption('Cobblestone Land? idfk what this is')

CobbleBackdrop = pygame.Surface((Screen.get_width() , Screen.get_height()))

Clock = pygame.time.Clock()
running = True

Cobble = pygame.image.load('assetts/tiles/cobble.png')
Cobble = pygame.transform.scale(Cobble , (TileEdge, TileEdge))

MossyCobble = pygame.image.load('assetts/tiles/mossycobble.png')
MossyCobble = pygame.transform.scale(MossyCobble , (TileEdge, TileEdge))

Ghost = pygame.image.load('assetts/sprites/ghost.png')
Ghost = pygame.transform.scale(Ghost , (SpriteX, SpriteY))
PlayerFloatIndex = 0.0
PlayerPos = pygame.Vector2((Screen.get_width() / 2) - (SpriteX / 2), Screen.get_height() / 2 - (SpriteY / 2))

def checkInputs():



    Keys = pygame.key.get_pressed()

    if Keys[pygame.K_SPACE]:
        PlayerPos.y -=  5 * ZoomMultiplier
        PlayerPos.y +=  5 * ZoomMultiplier
        Jump = True
    if Keys[pygame.K_a]:
        PlayerPos.x -= MoveValue
    if Keys[pygame.K_d]:
        PlayerPos.x += MoveValue

def checkOOB():
    if PlayerPos.y > Screen.get_height():
        PlayerPos.y = 0
        genCobble()
    elif PlayerPos.y < 0:
        PlayerPos.y =  Screen.get_height()
        genCobble()
    elif PlayerPos.x > Screen.get_width():
        PlayerPos.x = 0
        genCobble()
    elif PlayerPos.x < 0:
        PlayerPos.x =  Screen.get_width()
        genCobble()

def playerFloat(Index):
    Index += 0.1
    #print("indexed at " + str(Index))

    if(round(Index , 1) >= 1.0):
        if(round(Index , 1) >= 1.0 and round(Index , 1) <= 3.0):
            PlayerPos.y -= 0.05 * ZoomMultiplier
        elif(round(Index , 1) >= 4.0 and round(Index , 1) <= 6.0):
            PlayerPos.y += 0.05 * ZoomMultiplier
            if round(Index , 1) == 6.0:
                Index = 0

    return Index

def genCobble():
    for i in range(NoTilesX):
        for j in range(NoTilesY):
            if(random.randint(0,5) == 1):
                CobbleBackdrop.blit(MossyCobble,(i*TileEdge,j*TileEdge))
            else:
                CobbleBackdrop.blit(Cobble,(i * TileEdge , j * TileEdge))

genCobble()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    checkInputs()
    checkOOB()

    PlayerFloatIndex = playerFloat(PlayerFloatIndex)

    Screen.blit(CobbleBackdrop , (0,0))
    Screen.blit(Ghost , PlayerPos)

    pygame.display.update()

    Clock.tick(60)  # limits FPS to 60

pygame.quit()