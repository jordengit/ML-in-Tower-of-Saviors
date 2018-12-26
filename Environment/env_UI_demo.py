import env_UI

#設置更新時間
env_UI.setUpdateTime(100)#時間單位是毫秒,100毫秒=0.1秒


#先寫一個主要方法
def mainFunction():
	env_UI.update_canvas([[1,1,1,0,0,0],[2,2,2,1,1,0],[3,3,1,1,2,2],[0,1,2,3,4,4],[5,5,5,4,4,4]])
	print("主要迴圈,對網絡的訓練,每一步的虛擬環境邏輯都寫在這")


#先註冊function
env_UI.setLoopFuncTion(mainFunction)


#创建一个新的窗口,會永遠卡在這邊
env_UI.initWindow("河内塔")
