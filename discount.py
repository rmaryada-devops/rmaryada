#/usr/bin/python

"""
Purpose : Cost of Grocery after Discount and GST
Products : Home Grocery

"""

GST = 12.5
DISCOUNT = 20
white_rice = 25 # PerKG
santoor_soap = 12 # PerPiece

print("Hello Sir Welcome to the store !")
Type_Of_Rice = input("Which Rice you want to buy :")
print("Sir , You have chosen :" , Type_Of_Rice)
Quantity_Of_Rice = int(input("Number of Kgs of Rice you want to buy:"))
print("Sir , You have chosen :" , Quantity_Of_Rice)

Type_Of_Soap = input("Which Soap you want to buy :") 
print("Sir , You have chosen :" , Type_Of_Soap) 
Num_Of_Soap = int(input("Number of Soaps you want to buy:"))

Total_Rice = ( white_rice * Quantity_Of_Rice )
print("Rice Price is :" ,Total_Rice)
Total_Soap = ( santoor_soap * Num_Of_Soap )
print("Soap Price is :" ,Total_Soap)

Total_Before_Discount = Total_Rice + Total_Soap
print("Total Before Discount is :" , Total_Before_Discount)

Total_After_Discount = Total_Before_Discount - ( Total_Before_Discount * ( DISCOUNT / 100 ))
print("Total After 20% Discount is : ", Total_After_Discount)

Final_Total_Gst = Total_After_Discount + ( Total_After_Discount * ( GST / 100 ))
print("Total Amount to paid after adding GST - 12.5% , Thanks for shopping !!! : ", Final_Total_Gst)








