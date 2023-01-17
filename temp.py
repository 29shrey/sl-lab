tuplelist = []
def celcius_to_fahrenheit():
    celsius = int(input("Enter temperature in celcius"));
    fahrenheit = 9/5*celsius+32;
    tuplelist.append((celsius,fahrenheit))
    print("Temperatur in  Fahrenheit is " + str(fahrenheit));

def fahrenheit_to_celsius():
    fahreheit = int(input("Enter temperature in fahrenheit"));
    celsius = (fahreheit-32)*5/9
    tuplelist.append((fahreheit,celsius))
    print("Temperature in celsius is " + str(celsius));

print("Enter Choice\n1.celsius to fahrenheit\n2.fahrenheit to celsius\n3.display tuple\n4.exit")
choice=0
while(choice!=4):
    choice=int(input())
    if(choice==1):
        celcius_to_fahrenheit()
    elif(choice==2):
        fahrenheit_to_celsius()
    elif(choice == 3):
        print(tuplelist)
    elif(choice == 4):
        exit()
    else:
        print("Invalid choice")