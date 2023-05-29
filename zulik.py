#简述面向对象中__new__和__init__区别 __init__是初始化方法，创建对象后，就立刻被默认调用了，可接收参数
class Bike:
    def __init__(self, newWheelNum, newColor):
        self.wheelNum = newWheelNum
        self.color = newColor
    def move(self):
        print('车会跑')
#创建对象
BM = Bike(2, 'green')
print('车的颜色为:%s'%BM.color)
print('车轮子数量为:%d'%BM.wheelNum)