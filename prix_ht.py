# coding:utf-8

# The proposal of the exercice is to calculate the taxed price (TTC) of a product based on its raw price (HT).

def name_product(product) :
    while True :
        try :
            product = str(input("what is the product you want to estimate ?")) 
            return product
        except ValueError :
            print("Please enter a string value")

def raw_price(x):
    a = x
    x = -1
    while x < 0 :
        try :
            x = float(input("Please enter the raw price of this " + str(a) + " :"))  
        except ValueError :
            print(str(a), "must be a positive float number ;) Try again...")
    return x

print ("The proposal of the exercice is to calculate the taxed price (TTC) of any product based on its raw price (HT).")

product = 0
x = 0
taxe_value = 1.196

product = name_product(product)
x = raw_price(product)
y = x * taxe_value



print("the taxed price of this " + str(product) + ", base on the raw price of " + str(x) + "€, is " + str(y) + "€.")

