x = 1
y = 2
fibonacci = [x,y]
s = 0
even = 0

while x + y <=4000000:
    s = x + y 
    x = y 
    y = s
    fibonacci.append(s)
    print(fibonacci)
    

for i in range(len(fibonacci)):
    if fibonacci[i] % 2 == 0:
        even = fibonacci[i] + even
        print(even)