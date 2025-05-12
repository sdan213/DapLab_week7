#NumPy Operations with Arrays
import numpy as np
a = np.array([[1, 2], [4, 5]])
b = np.array([[1, 2], [4, 5]])
while True:
    print("1.Add , 2.Subtract , 3.Multiply , 4.Divide , 5.Dot product , 6.Exponentiation ,7.Logarithm , 8.Natural logarithm , 9.Exit")
    n = int(input("Enter the option number : "))
    if not n < 1 and not n > 8:
        if n == 1:
            c = np.add(a, b)
            print("Sum\n", c)
            print("\n")
        elif n == 2:
            d = np.subtract(a, b)
            print("Difference\n", d)
            print("\n")
        elif n == 3:
            e = np.multiply(a, b)
            print("Product\n", e)
            print("\n")
        elif n == 4:
            f = np.divide(a, b)
            print("Remainder\n", f)
            print("\n")
        elif n == 5:
            g = np.dot(a, b)
            print("Dot product\n", g)
            print("\n")
        elif n == 6:
            h, i = np.exp(a), np.exp(b)
            print("Exponentiation for array a : \n", h)
            print("Exponentiation for array b : \n", i)
            print("\n")
        elif n == 7:
            l, m = np.log(a), np.log(b)
            print("Logarithm for array a : \n", l)
            print("Logarithm for array b : \n", m)
            print("\n")
        elif n == 8:
            x, y = np.log10(a), np.log10(b)
            print("Natural logarithm for array a : \n", x)
            print("Natural logarithm for array b : \n", y)
            print("\n")
    elif n == 9:
        break
    else:
        print("No such option exist,please enter existing options.\n")
