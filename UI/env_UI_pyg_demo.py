import env_UI_pyg
import time
import random

UPDATE_CYCLE=2

def mianCycle(contorler):
	start_time = time.time()
	while contorler.running:
		interval = time.time() -start_time
		#print("間隔:{0}".format(interval))
		if interval >= UPDATE_CYCLE:
			print("interval: {0}".format(interval))
			start_time = time.time()
			randMap=[]
			for y in range(5):
				list = []
				for x in range(6):
					list.append(random.randint(0,5))
				randMap.append(list)
			contorler.updateWindow(randMap)
		#print("ans:{0}".format(random.randint(0,10)))


window = env_UI_pyg.gameWindow("demo",mianCycle)
window.initWindow()