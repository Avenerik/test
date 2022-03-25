#! /usr/bin/env python3

print("Hello from She Goes Tech")

# F-string 

s = "hello, world"
a = "how are you?"
d = "HELLO"
za = "hi my name is veronika and i try to learn python"
x = 4
y = 5
x1 = 7
y2 = 9
k = "result:"
print(s.upper(), a.upper())
print(d.lower())
#print(d.title())
#print(a.split())
#print(za.split("on"))
#print(za.split().append("a"))
#print(s+' \t\t '+s.upper())
#print(s+' \n\t\t '+s.upper())
#print(x*y)
#print(x*y, "\t\t", x+y)
#print(k.upper(), x1*y2)
#print(f"{k} {x*y:2f}")
#print(f"hello "

print(f"x and y equality {x == y}")
if x == y:
	print((f"x and y are equal {x == y}"))
elif x < y:
	print(f"x is smaller")
else: 
	print(f"x is bigger")
	
while x >= y:
	print(f"current x is {y}")
	y += 1
else:
	print("no")
	
for i in range(x):
	print(i)

for i in range(10)
	print(i)
