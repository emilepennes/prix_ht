# coding:utf-8

"""The proposal of the exercice is to calculate the taxed price (TTC)
of a product based on its raw price (HT) with two decimals.
"""

print("The proposal of the exercice is to calculate the taxed price (TTC)",
      " of any product based on its raw price (HT).")

NAME_PRODUCT = "product"
RAW_PRICE = -1
TAX_PRICE = 0

while True:
    try:
        NAME_PRODUCT = str(input("what is the product you want to estimate ?"))
        break
    except ValueError:
        print("Please enter a string value")

while RAW_PRICE < 0:
    try:
        RAW_PRICE = float(input("Please enter the raw price of this " +
                                NAME_PRODUCT + " :"))
    except ValueError:
        print(NAME_PRODUCT, "must be a positive float number ;) Try again...")

RAW_PRICE_ROUND = round(RAW_PRICE, 2)
TAXE_VALUE = 1.196
TAX_PRICE = RAW_PRICE * TAXE_VALUE
TAX_PRICE_ROUND = round(TAX_PRICE, 2)
"""Convert the raw price to the taxed price"""

print("the taxed price of this " + NAME_PRODUCT + ", based on the raw price of " +
      str(RAW_PRICE_ROUND) + "€, is " + str(TAX_PRICE_ROUND) + "€.")
