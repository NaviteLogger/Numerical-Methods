import numpy as np
import math


def main():
    h = float(1)
    wynik = ["krok", "h", "iloraz", "poch"]

    for k in range(60):
        iloraz = (math.exp(10+h)-math.exp(10))/h
        zapis = [k, h, iloraz, math.exp(10)]
        wynik = np.vstack([wynik, zapis])
        h /= 2

    print(wynik)


if _name_ == "_main_":
    main()
