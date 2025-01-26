import pygame

class Bubble:
    BubbleImage = pygame.image.load('assets/sprites/bubble1.png')
    BubbleImages = [pygame.image.load('assets/sprites/bubble1.png') , pygame.image.load('assets/sprites/bubble2.png')]
    BubbleRec = pygame.Rect((0,0) , (0,0))
    X = 0
    Y = 0

    def __init__(self , TileEdge , x , y):
        self.X = x
        self.Y = y

        self.BubbleImage = pygame.transform.scale(self.BubbleImage , (TileEdge, TileEdge))

        for i in range(len(self.BubbleImages)):
            self.BubbleImages[i] = pygame.transform.scale(self.BubbleImages[i] , (TileEdge, TileEdge))

        self.BubbleRec = pygame.Rect((self.X , self.Y) , (TileEdge , TileEdge))