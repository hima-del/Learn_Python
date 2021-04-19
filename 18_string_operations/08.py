string = "hello world"
a = (string.maketrans("h","l"))
print(string.translate(a))

txt = "india is my country and all indians are my brothers"
print(txt.partition("alll"))
print(txt.replace("and",""))

txt_1 = "one one was a race horse, two two was one too."
print(txt_1.replace("one","three",1))
print(txt_1.rfind("horse"))
