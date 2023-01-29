from engine import *
import pygame, os, json

# This is here to make sure that this code doesn't run twice.
if has_ran == False:
    
    pygame.init()
    clock = pygame.time.Clock()
    
    # Font
    font_small = pygame.font.Font(None, 32)

    # Basic Color
    white = (255, 255, 255)
    black = (0, 0, 0)
    
    spriteList = []
    
    # Finds the directory of this file
    dir_name = os.path.dirname(__file__)
    # Combines dirname with the file name of the anim_data
    anim_dir = os.path.join(dir_name, "frames.json")
    # Prepares frames.json
    anim_file = open(anim_dir, "r+")
    # Copies everything in frames.json to 
    anim_data = json.load(anim_file)
    
    # This combines everything together to make a directory path for every sprite and appends it this spriteList for ease of use.
    for item in anim_data:
        spriteList.append(os.path.join(dir_name, "sprites", anim_data[item]))
    
    # Instances
    text = FrameText(black, 250, 25)
    spriteAnim = Sprite(spriteList)
    
    # Debug Text
    print("Reading animation data...")
    for i in spriteList:
        print("- ",i)

    print("No problems so far..")
    
    # Starts up the program
    Program.Run(clock, white)

has_ran = True