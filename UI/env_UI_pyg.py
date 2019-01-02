import pygame
import sys
from pygame.locals import *
import threading

class gameWindow:
	def __init__(self,name,callback,cycle=0.1):
		pygame.init()
		self.callback = callback
		self.stones=[]
		self.bg_color=(47,47,47)
		self.window_name=name
		self.screen=None
		self.WINDOW_WIDTH=300
		self.WINDOW_HEIGHT=250
		self.STONE_WIDTH=50
		self.STONE_HEIGHT=50
		self.running=True


	def initWindow(self):
		
		print("進入initwindow")
		self.screen = pygame.display.set_mode((self.WINDOW_WIDTH,self.WINDOW_HEIGHT))
		#載入符石:
		self.stones.append(pygame.transform.scale(pygame.image.load(".\\Img\\heart.png").convert_alpha(),(self.STONE_WIDTH,self.STONE_HEIGHT)))
		self.stones.append(pygame.transform.scale(pygame.image.load(".\\Img\\wood.png").convert_alpha(),(self.STONE_WIDTH,self.STONE_HEIGHT)))
		self.stones.append(pygame.transform.scale(pygame.image.load(".\\Img\\fire.png").convert_alpha(),(self.STONE_WIDTH,self.STONE_HEIGHT)))
		self.stones.append(pygame.transform.scale(pygame.image.load(".\\Img\\water.png").convert_alpha(),(self.STONE_WIDTH,self.STONE_HEIGHT)))
		self.stones.append(pygame.transform.scale(pygame.image.load(".\\Img\\dark.png").convert_alpha(),(self.STONE_WIDTH,self.STONE_HEIGHT)))
		self.stones.append(pygame.transform.scale(pygame.image.load(".\\Img\\light.png").convert_alpha(),(self.STONE_WIDTH,self.STONE_HEIGHT)))
		pygame.display.set_caption(self.window_name)
		self.thread = threading.Thread(target = self.callback,args=(self,))
		self.thread.start()

		print("初始化完成")
		while True:
			#print("gogo")
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running=False
					#self.thread._Thread_stop()
					sys.exit()
	def updateWindow(self,map):
		self.screen.fill(self.bg_color)
		for y in range(len(map)):
			for x in range(len(map[y])):
				self.screen.blit(self.stones[map[y][x]],(self.STONE_WIDTH*x,self.STONE_HEIGHT*y))
				#print("y:{1} x:{2} 畫{0}".format(map[y][x],self.STONE_HEIGHT*y,self.STONE_WIDTH*x))
		pygame.display.update()
#thread = threading.Thread(target = initWindow)
#print("物件產生完畢")
#thread.start()
def mainFunc(UI):
	#surf = pygame.Surface((50,100))
	# 设定Surface的颜色，使其和屏幕分离
	#surf.fill((255,255,255))
	
	#image = pygame.image.load("wood.png").convert_alpha()
	#rect = image.get_rect()
	#rect.width = 50
	#rect.height = 50
	#image=pygame.transform.scale(image,(50,50))
	
	#print("rect is {0}".format(rect))
	#window.blit(self.stones[0],(0,0))
	#pygame.display.flip()
	#window.blit(image,(100,0))
	
	#window.blit(surf,(0,0))
	#pygame.display.flip()
	#while True:
	#	print("loop")
	
	UI.updateWindow([[0,0,3,4,5,1],[2,2,3,4,4,4],[1,1,1,2,2,2],[0,0,0,4,4,4],[5,5,5,5,5,3]])

#window = gameWindow("命運石",mainFunc)
#window.initWindow()