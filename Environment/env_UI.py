import tkinter as tk
from PIL import Image,ImageTk
import threading
STONE_WIDTH = 50
window = None#tk.Tk()
canvas = None
map_updated=False
newMap=[]
Update_Cycle = 100#每100毫秒更新一次
mainFunc =None
#window.title("我也是個廣東人,我們可能是老♂鄉")
#window.geometry("300x300")
def setUpdateTime(time):
	global Update_Cycle
	Update_Cycle = time
""""def threadFunc():
	global window
	window.after(Update_Cycle,checkUpdate)
	window.mainloop()"""
def setLoopFuncTion(function):
	global mainFunc 
	mainFunc= function

def checkUpdate():
	#global map_updated
	global mainFunc
	mainFunc()
	window.after(Update_Cycle,checkUpdate)

def initWindow(name = "tower of SM"):
	global window
	global canvas
	print("创建window")
	window = tk.Tk()
	window.title(name)
	window.geometry("300x300")
	canvas =tk.Canvas(window,bg = 'black',height=STONE_WIDTH*5,width = STONE_WIDTH*6)
	#thread1 = threading.Thread(target=threadFunc,name="线程1",args=())
	#thread1.start()
	window.after(Update_Cycle,checkUpdate)
	window.mainloop()
'''
t = tk.StringVar()
label1= tk.Label(window,textvariable=t,bg = 'white',font = ('Arial',12),width=15,height=2)
label1.pack()
clicking = False
def hit_me():
	global clicking
	print("被點擊!")
	print(e.get())
	if not clicking:
		t.set("精密!地精!工程學!")
		clicking = True
	else:
		t.set("")
		clicking = False
	'''
#b = tk.Button(window, text='hit me',width=15, height=2,command=hit_me)#点击按钮式执行的命令
#b.pack()# 按钮位置

stoneList=[]
#打開6個符石file
heart = Image.open('.\\Img\\heart.png').resize((STONE_WIDTH,STONE_WIDTH),Image.BILINEAR)
stoneList.append(heart)
wood = Image.open('.\\Img\\wood.png').resize((STONE_WIDTH,STONE_WIDTH),Image.BILINEAR)
stoneList.append(wood)
fire = Image.open('.\\Img\\fire.png').resize((STONE_WIDTH,STONE_WIDTH),Image.BILINEAR)
stoneList.append(fire)
water = Image.open('.\\Img\\water.png').resize((STONE_WIDTH,STONE_WIDTH),Image.BILINEAR)
stoneList.append(water)
dark = Image.open('.\\Img\\dark.png').resize((STONE_WIDTH,STONE_WIDTH),Image.BILINEAR)
stoneList.append(dark)
light = Image.open('.\\Img\\light.png').resize((STONE_WIDTH,STONE_WIDTH),Image.BILINEAR)
stoneList.append(light)

#image2 = ImageTk.PhotoImage(fire)
#image_file2=image_file.copy()
#image = canvas.create_image(0,0,anchor='nw',image = image_file)
#ima = canvas.create_image(0,0,anchor = 'nw',image = image2)
#image3 = ImageTk.PhotoImage(heart)
#ima = canvas.create_image(100,0,anchor = 'nw',image = image3)
#canvas.pack()

#e = tk.Entry(window,show='*')
#e.pack()
StoneMap=[]
TKimages=[]
def update_canvas(map):#map是二維陣列
	if window == None:
		print("请先初始化window initWindow()")
	else:
		canvas.delete("all")
		print("進入update map:stoneList length:{0}".format(len(stoneList)))
		TKimages.clear()
		StoneMap.clear()
		for y in range(len(map)):
			print("----y:{0}".format(y))
			newList = []
			newImgs = []
			for x in range(len(map[y])):
				kind = map[y][x]
					
				#imgtk = ImageTk.PhotoImage(stoneImg)
				#print("ImgTk kind:{0} image:{1} stoneList[kind]:{2}".format(kind,imgtk,stoneList[kind]))
				if kind<len(stoneList):
					newImgs.append(ImageTk.PhotoImage(stoneList[kind]))
					id = canvas.create_image(x*STONE_WIDTH,y*STONE_WIDTH,anchor='nw',image = newImgs[x])
				newList.append(id)
				#print("--x:{0} pos {1},{2} ImgTk{3}".format(x,x*STONE_WIDTH,y*STONE_WIDTH,newImgs[x]))
			StoneMap.append(newList)
			TKimages.append(newImgs)
		canvas.pack()


