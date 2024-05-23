import math

add = []
points = []
for i in range(0, 6):
    sides_name = ["a", "b", "c", "d", "e", "f"]
    while True:
        try:
            add = (int(input("Add meg a(z) '" + sides_name[i] + "' koordinátát: ")))
        except ValueError:
            print("Nem számot adtál meg!")
            continue
        else:
            if add > -100 and 100 > add:
                break
            else:
                print('A számnak -100 és 100 között kell lennie!')
                continue
    points.append(add)

A=[]
B=[]
C=[]
A.append(points[0])
A.append(points[1])
B.append(points[2])
B.append(points[3])
C.append(points[4])
C.append(points[5])

a = math.sqrt(((A[0] - B[0])**2) + ((A[1] - B[1])**2))     #AB
b = math.sqrt(((C[0] - B[0])**2) + ((C[1] - B[1])**2))     #CB
c = math.sqrt(((C[0] - A[0])**2) + ((C[1] - A[1])**2))     #CA
p = (a + b + c) / 2

Area = math.sqrt(p * (p - a) * (p - b) * (p - c))          #Heron's Formula
print("A háromszög területe: " + "%.1f" % Area)            #Rounding up the decimals to match to the criteria.

