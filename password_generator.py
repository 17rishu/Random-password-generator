import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
specials="!@#$%^&*"

all=lower+upper+numbers+specials

length=10
password="".join(random.sample(all,length))
print(password)