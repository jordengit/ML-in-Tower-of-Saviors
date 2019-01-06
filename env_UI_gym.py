from gym.envs.classic_control import rendering
import time
import random
class env_window:
	def __init__(self):
		self.WINDOW_WIDTH=300
		self.WINDOW_HEIGHT=300
		self.STONE_WIDTH=50
		self.STONE_HEIGHT=50
		self.NUM_WIDTH =35
		self.NUM_HEIGHT =50
		self.viewer = rendering.Viewer(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
		self.paths=[]
		self.paths.append(".//Img//heart.png")
		self.paths.append(".//Img//wood.png")
		self.paths.append(".//Img//fire.png")
		self.paths.append(".//Img//water.png")
		self.paths.append(".//Img//dark.png")
		self.paths.append(".//Img//light.png")
		self.n_paths= []
		self.n_paths.append(".//Img//num_0.png")
		self.n_paths.append(".//Img//num_1.png")
		self.n_paths.append(".//Img//num_2.png")
		self.n_paths.append(".//Img//num_3.png")
		self.n_paths.append(".//Img//num_4.png")
		self.n_paths.append(".//Img//num_5.png")
		self.n_paths.append(".//Img//num_6.png")
		self.n_paths.append(".//Img//num_7.png")
		self.n_paths.append(".//Img//num_8.png")
		self.n_paths.append(".//Img//num_9.png")
	def updateWindow(self,map,combo):
		self.viewer.geoms=[]
		for x in range(len(map)): # max_x == 5
			for y in range(len(map[x])): # max_y == 6
				Img = rendering.Image(self.paths[map[x][y]],self.STONE_WIDTH,self.STONE_HEIGHT)
				Img.add_attr(rendering.Transform(translation=(25+x*self.STONE_WIDTH,75+y*self.STONE_HEIGHT)))
				Img.set_color(1.,1.,1.)
				self.viewer.add_geom(Img)
		if combo<0 or not type(combo) == int:
			self.viewer.render()
			return
		nums=[]
		end = False
		while not end:
			if combo<10:#個位數是最後一次
				end =True
			num= combo%10
			print("num為{0}".format(num))
			combo=int(combo/10)
			nums.insert(0,num)
		print('最後結果為:{0}'.format(nums))
		for i in range(len(nums)):
			Img = rendering.Image(self.n_paths[nums[i]],self.NUM_WIDTH,self.NUM_HEIGHT)
			print('位於 {0}'.format((25+i*35,25)))
			Img.add_attr(rendering.Transform(translation=(25+i*35,25)))
			Img.set_color(1.,1.,1.)
			self.viewer.add_geom(Img)
		self.viewer.render()
	def runing(self):
		return self.viewer.isopen
