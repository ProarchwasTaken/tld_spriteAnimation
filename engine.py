import pygame, sys
has_ran = False

class Program:
    # Screen Resolution
    screenSize = 500, 500
    screen = pygame.display.set_mode(screenSize)
    
    frame = 0
    
    @classmethod
    def Run(cls, clock, bg_color):
        from init import text, spriteAnim
        while True:
            for event in pygame.event.get():
                #Allows the player to quit the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Global Frame Timer, Will be used for sprite animation.
            if cls.frame <= 80:
                cls.frame += 1
            else:
                cls.frame = 0
            
            # Refreshes the screen with white.
            cls.screen.fill(bg_color)
            
            # Updates other elements
            text.Update()
            spriteAnim.Update()
            
            #Updates the screen
            pygame.display.flip()
            #Max framerate.
            clock.tick(60)
            
class FrameText():
    # This Class variable will be used as a color variable for Update
    text_color = (0,0,0)
    
    def __init__(self, color, x, y):
        from init import font_small
        self.text = font_small.render(str(Program.frame), True, color)
        self.rect = self.text.get_rect()
        self.rect.center = x, y
        
        # Sets text_color to the color assigned to text
        FrameText.text_color = color
        
    def Update(self):
        from init import font_small
        # This text will display the Program.frame counter       
        self.text = font_small.render(str(Program.frame), True, FrameText.text_color)
        Program.screen.blit(self.text, self.rect)

class Sprite():
    
    spriteList = []
    
    def __init__(self, spriteList):
        # Sets up the first image.
        self.image = pygame.image.load(spriteList[0])
        self.rect = self.image.get_rect()
        self.rect.center = 250, 250
        
        # Copies init.py spriteList to this for further use
        Sprite.spriteList = spriteList
        print("Sprite has successfully loaded.")
    
    def Update(self):
        # Calls animation function
        self.Animation()
        
        # Draws Sprite on the screen
        Program.screen.blit(self.image, self.rect)
    
    def Animation(self):
        # This For loop is activated for every item in Sprite.spritelist.
        for i in Sprite.spriteList:
            # Checks if Program.frame is higher them the item's index * 10 and it's lower than item's index * 10 + 10
            if Program.frame > Sprite.spriteList.index(i) * 10 and Program.frame < Sprite.spriteList.index(i) * 10 + 10:
                # If true, change the sprite to the item's frame.
                self.image = pygame.image.load(i)