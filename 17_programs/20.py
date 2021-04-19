#x = ["a","b","c"]
#x.append("d")
#x.append("e")
#print(x)
#x.pop()
#print(x)

import queue
L = queue.Queue(maxsize=10)

L.put(9)
L.put(6)
L.put(7)
L.put(4)
print(L.get())
print(L.get())
print(L.get())
print(L.get())