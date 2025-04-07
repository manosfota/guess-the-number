def menu():
    print("Option1: Celsium to Fahrenheit")
    print("Option2: Fahrenheit to Celsium")
    print("Option3: Kelvin to  Celsium")
    print("Option4: Celsium to Kelvin")
    option=1

    while option !=0:
        option=int(input('Enter your option: '))
        if option == 1:
            Kels_degr=int(input("Give the Celsium Degree: "))
            F=((Kels_degr*(9/5))+32)
            print(f"The {Kels_degr} degrees Celsium is {F:.2f}  degrees Fahrenheit")    

        elif option == 2:
            Far_degr=int(input("Give the Fahrenheit Degree: "))
            T=((Far_degr)-32)*(5/9)
            round_T=round(T,2)
            print(f"The {Far_degr} degrees Fahrenheit is {round_T}  degrees Celsium ")    
            
        elif option == 3:
            cls=-273.15
            Kelv_degr=int(input("Give the kelvin Degree: "))
            Klv_convert=float(cls)+float(klv)
            round_Klv=round(Klv_convert,2)
            print(f"The {klv}  K  is  {round_Klv}  Celsium Degree")    

        elif option == 4:
            klv=273.15
            Kels_degr=int(input("Give the kelvin Degree: "))
            Cels_conv=int(Kels_degr)+int(klv)
            round_Cels=round(Cels_conv,2)
            print(f"The {Kels_degr}  C  is {round_Cels}  Celsium Degree")
            
        else:
           print("Invalid option")
        break  


print("\u2764\uFE0F")
def main():                                 
    menu()                        
                          
                          
                          
                          












   





