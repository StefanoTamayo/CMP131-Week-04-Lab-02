#Stefano Tamayo
#CMP-131
#Week 4 Lab 2
#Arithmetic Operation
#9/23/26

num1=float(input("Enter Value 1: ")) #Asking user for first input
num2=float(input("Enter Value 2: ")) #Asking user for second input
add=num1+num2 #Equation for Addition
sub=num1-num2 #Equation for Subtraction
multi=num1*num2 #Equation for multiplication
div=num1/num2 #Equation for division
power=num1**num2 #Equation for power of value 1 raised to value 2
average=(num1+num2)/2 #Equation for the average of the two values
print()
print(f"Value 1 = {num1:,.2f}") 
print(f"Value 2 = {num2:,.2f}") 
print()
print(f"Addition (+) : {num1} + {num2} = {add:,.2f}") #Displaying addition equation step by step
print(f"Subtraction (-) : {num1} - {num2} = {sub:,.2f}") #Displaying subtraction equation step by step
print(f"Multiplication (x) : {num1} * {num2} = {multi:,.2f}") #Displaying multiplication equation step by step
print(f"Division (÷) : {num1} ÷ {num2} = {div:,.2f}") #Displaying division equation step by step
print(f"Power (^) : {num1} ^ {num2} = {power:,.2f}") ##Displaying pwoer equation step by step
print(f"Average : ({num1} + {num2}) ÷ (amount of variables) = {average:,.2f}") #Displaying average/mean equation step by step
