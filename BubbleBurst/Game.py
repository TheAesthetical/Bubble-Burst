# Example file showing a basic pygame "game loop"
import pygame 
import random
import os

from Bubble import Bubble

pygame.init()

# pygame setup

NoTilesX = 16
NoTilesY = 12

ZoomMultiplier = 3
MoveValue = 2.5 * ZoomMultiplier

TileEdge = 16 * ZoomMultiplier

SpriteX = 16 * ZoomMultiplier
SpriteY = 32 * ZoomMultiplier

JumpIndex = 0
Jump = False

BackgroundIndex = 0

BubbleIndex = 0
BubblesPopped = 0
PulseIndex = 0

Screen = pygame.display.set_mode((TileEdge*NoTilesX, TileEdge*NoTilesY))
pygame.display.set_caption('Bubble Burst')

Clock = pygame.time.Clock()
running = True

Background = pygame.image.load('assets/tiles/background1.png')
Background = pygame.transform.scale(Background , (TileEdge*NoTilesX, TileEdge*NoTilesY))

Base = pygame.image.load('assets/tiles/basecloud.png')
Base = pygame.transform.scale(Base , (TileEdge*NoTilesX, TileEdge*4))

BubbleList = [Bubble]

BubbleBackdrop = pygame.Surface((Screen.get_width() , Screen.get_height() - Base.get_height()), pygame.SRCALPHA, 32).convert_alpha()

Player = pygame.image.load('assets/sprites/player.png')
Player = pygame.transform.scale(Player , (SpriteX, SpriteY))

PlayerPos = pygame.Vector2(((Screen.get_width() / 2) - (SpriteX / 2)), (((Screen.get_height() / 2) + (Base.get_height() / 2)) - (SpriteY / 2)))

PlayerRec = pygame.Rect(PlayerPos , (SpriteX, SpriteY))

def backgroundGen():
    global BackgroundIndex
    BackgroundIndex += 0.02
    Filename = ""

    Background = pygame.image.load("assets/tiles/background1.png")

    if round(BackgroundIndex , 1) < 1:
        Background = pygame.image.load("assets/tiles/background2.png")
    if round(BackgroundIndex , 1) == 2:
        BackgroundIndex = 0

    Background = pygame.transform.scale(Background , (TileEdge*NoTilesX , TileEdge*NoTilesY))
    Screen.blit(Background , (0,0))
    Screen.blit(Base , (0,Screen.get_height() - (64*ZoomMultiplier)))

def checkInputs():
    global JumpIndex
    global Jump
    global Player
    global PlayerRec

    JumpValue = 11

    Player = pygame.image.load('assets/sprites/player.png')

    Keys = pygame.key.get_pressed()

    if Keys[pygame.K_SPACE] and Jump == False:
        Jump = True
        Player = pygame.image.load('assets/sprites/playerjump.png')
    if Keys[pygame.K_a]:
        PlayerPos.x -= MoveValue
        Player = pygame.image.load('assets/sprites/playerleft.png')
    if Keys[pygame.K_d]:
        PlayerPos.x += MoveValue
        Player = pygame.image.load('assets/sprites/playerright.png')

    if Jump == True:
        Player = pygame.image.load('assets/sprites/playerjump.png')

        if round(JumpIndex , 1) == 2:
            Jump = False
            JumpIndex = 0
            return
        
        if round(JumpIndex , 1) < 1:
            PlayerPos.y -=  JumpValue * ZoomMultiplier
        elif round(JumpIndex , 1) < 2:
            PlayerPos.y +=  JumpValue * ZoomMultiplier
        
        JumpIndex += 0.1

    PlayerRec = pygame.Rect(PlayerPos , (SpriteX, SpriteY))
    Player = pygame.transform.scale(Player , (SpriteX, SpriteY))

def checkOOB():
    if PlayerPos.x > Screen.get_width():
        PlayerPos.x = Screen.get_width()
    elif PlayerPos.x < 0:
        PlayerPos.x = 0

def genBubble():
    BubbleBackdrop = pygame.Surface((Screen.get_width() , Screen.get_height() - Base.get_height()), pygame.SRCALPHA, 32).convert_alpha()
    global BubbleIndex
    global BubbleList

    for i in range(len(BubbleList)):
        BubbleBackdrop.blit(BubbleList[i].BubbleImage,(BubbleList[i].X, BubbleList[i].Y))
        animateBubble(BubbleList[i])

    if round(BubbleIndex,1) < 1:
        BubbleIndex += 0.025
    elif round(BubbleIndex,1) >= 1:
        NewBubble = Bubble(TileEdge,random.randint(0,(TileEdge*NoTilesX) - TileEdge),random.randint(0,((TileEdge*NoTilesY) - Base.get_height() - TileEdge)))

        BubbleList.append(NewBubble)

        BubbleBackdrop.blit(NewBubble.BubbleImage,(NewBubble.X, NewBubble.Y))
        BubbleIndex = 0
    
    Screen.blit(BubbleBackdrop , (0,0))

def checkPop():
    global BubblesPopped

    for i in range(len(BubbleList)):
        if(PlayerRec.colliderect(BubbleList[i].BubbleRec)):
            BubbleList.remove(BubbleList[i])
            BubblesPopped += 1
            break

def animateBubble(AnimatedBubble):
    global PulseIndex

    PulseIndex += 0.02

    if round(PulseIndex , 1) < 1:
        AnimatedBubble.BubbleImage = AnimatedBubble.BubbleImages[0]
    if round(PulseIndex , 1) == 2:
        AnimatedBubble.BubbleImage = AnimatedBubble.BubbleImages[0]
        PulseIndex = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    backgroundGen()
    checkInputs()
    checkOOB()
    genBubble()
    checkPop()

    Screen.blit(Player , PlayerPos)

    pygame.display.update()

    Clock.tick(60)  # limits FPS to 60

pygame.quit()