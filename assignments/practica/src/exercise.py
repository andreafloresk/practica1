def main():
    import math
    #este codigo calcula la hipotenusa
    
    la = float(input("Dame el valor del largo: "))
    an = float(input("Dame el valor del ancho: "))

    diagonal= math.sqrt(math.pow(la,2)+math.pow(an,2))
    
    print(diagonal)



    

if __name__=='__main__':
    main()
