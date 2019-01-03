from gym.envs.classic_control import rendering
import time
import random
class env_window:

	def __init__(self):
		self.WINDOW_WIDTH=300
		self.WINDOW_HEIGHT=250
		self.STONE_WIDTH=50
		self.STONE_HEIGHT=50
		self.viewer = rendering.Viewer(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
		self.paths=[]
		self.paths.append(".\\Img\\heart.png")
		self.paths.append(".\\Img\\wood.png")
		self.paths.append(".\\Img\\fire.png")
		self.paths.append(".\\Img\\water.png")
		self.paths.append(".\\Img\\dark.png")
		self.paths.append(".\\Img\\light.png")
	def updateWindow(self,map):
		self.viewer.geoms=[]
		for y in range(len(map)):
			for x in range(len(map[y])):
				Img = rendering.Image(self.paths[map[y][x]],50,50)
				Img.add_attr(rendering.Transform(translation=(25+x*self.STONE_WIDTH,25+(4-y)*self.STONE_HEIGHT)))
				Img.set_color(1.,1.,1.)
				self.viewer.add_geom(Img)
		self.viewer.render()
	def runing(self):
		return self.viewer.isopen

window = env_window()
#print(window.runing())
#window.updateWindow([[2,3,4],[5,5,4],[1,1,1,0,0,0]])
'''start_time = time.time()
while True:
	interval = time.time() -start_time
	#print("間隔:{0}".format(interval))
	if interval >= 1.:
		#print("interval: {0}".format(interval))
		start_time = time.time()
		randMap=[]
		for y in range(5):
			list = []
			for x in range(6):
				list.append(random.randint(0,5))
			randMap.append(list)
		window.updateWindow(randMap)'''