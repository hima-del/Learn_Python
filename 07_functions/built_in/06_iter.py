mylist=iter(["apple","orange","banana","mango"])
while True:
    try:
        x=next(mylist)
        print(x)
    except StopIteration:
        break
