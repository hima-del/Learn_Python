txt_1 = "my name is {fname},I am {age}".format(fname = "john",age = 36)
print(txt_1)

x = "we have {:>8}chickens"
print(x.format(49))

y = "we have {:<8}chickens"
print(y.format(50))

word = "the universe is {:,} years old"
print(word.format(138000000000))
