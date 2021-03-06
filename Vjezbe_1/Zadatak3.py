import numpy as np

while True:
    try:
        x1 = float(input("unesi koordinatu x1: "))
        y1 = float(input("unesi koordinatu y1: "))
        x2 = float(input("unesi koordinatu x2: "))
        y2 = float(input("unesi koordinatu y2: "))
        break
    except ValueError:
        print("netocan unos")

#rjesavanje sustava jednadzbi
a = np.array([[x1, 1], [x2, 1]], dtype="float")
b = np.array([y1, y2])
solutions = np.linalg.solve(a, b)

#sortiranje rjesenja jednadzbi
k = solutions[0]
l = solutions[1]

#rjesavanje problema y=x+-l
if l > 0:
    print(f"Jednadzba pravca je: y={k}x+{l}")
else:
    print(f"Jednadzba pravca je: y={k}x{l}")
