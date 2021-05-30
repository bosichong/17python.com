import queue
import os

qq = queue.Queue()


with open(os.path.join(os.path.dirname(__file__),'God.py'),"rb") as f :
    data = f.read()
    qq.put(data)

data = qq.get()
print(data)