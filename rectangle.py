def area():
    shape=width*length
    print("area= ",shape,)
def perimeter():
    peri=(2*width)+(2*length)
    print("perimeter= ",peri," m")
width=int(input("Whats the width in m? "))
length=int(input("Whats the length in m?"))

op=input("Perimter or area? ")
if op=="Perimeter":
    peri
elif op=="Area":
    area
else:
    print("Nuh uh")
