# ここにコードを書いてね :-)
from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
gold = 41

mc.postToChat("begin! column")
x, z = (5, 10)
y = 0
for i in range(10):
    mc.setBlock(x, y, z, gold)
    time.sleep(0.1)
    y = y + 1
    print(y)

mc.postToChat("completed!")