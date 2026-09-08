"""Students Marks Manager 
marks=[]
for mark in range(3):
    mark=int(input("Enter the marks:"))
    marks.append(mark)
marks.insert(0,90)    #insert 90 at the begin
marks.extend([75,85]) #extend : Add mul values
if 75 in marks:       #Check 75 and removes it 
    marks.remove(75)
removed_mark=mark.pop() #To remove the final mark using pop
print(f'Removed Mark is {removed_mark}')
print(f'Final Student marks is {marks}')
print(f'Count the the student {len(marks)}') 

number=[20,10,30,20,40,20]
number.sort()
number.reverse()
print(number) """

#BMI UseCase --> BMI (Body Mass Index)
#Weight-->kgs
#height-->metres
#feet-->12 inches --> 2.54cm

#BMI=(Weight)/((Height)**2)

"""weight=float(input("Enter the weight"))
height=float(input("Enter the height"))
BMI=(weight)/((height)**2)
print(BMI) 

weight=float(input("Enter the weight"))
height=float(input("Enter the height"))
BMI=(weight)/((height)**2)
print(BMI)
if BMI < 18.5:
    print("Underweight")
elif 18.5<=BMI<=24.9:
    print("Normal Weight")
elif 25<=BMI<=29.9:
    print("Overweight")
elif BMI>=30:
    print("Obesity")
    
#Nested Loops
    
weight=float(input("Enter the weight"))
height=float(input("Enter the height"))
if weight>0 and height>0:
    BMI=(weight)/((height)**2)
    if BMI < 18.5:
        print("Underweight")
    elif 18.5<=BMI<=24.9:
        print("Normal Weight")
    elif 25<=BMI<=29.9:
        print("Overweight")
    elif BMI>=30:
        print("Obesity")
else:
    print("Enter only postive number") 

#Mul Inputs from the users  

no_of_users=int(input("Enter the value"))
for i in range(no_of_users):
    weight=float(input("Enter the weight"))
    height=float(input("Enter the height"))
    if weight>0 and height>0:
        BMI=(weight)/((height)**2)
        if BMI < 18.5:
            print("Underweight")
        elif 18.5<=BMI<=24.9:
            print("Normal Weight")
        elif 25<=BMI<=29.9:
            print("Overweight")
        elif BMI>=30:
            print("Obesity")
    else:
        print("Enter only postive number") """

#Task  --> Store the results of name,weight,Height --> BMI collection

#Repetion --> While
#Same above task we need to handle the errors(Exceptional handling) and also make user strictly to enter only numeric val

while True:
    weight=int(input("Enter the weight"))
    height=float(input("Enter the height"))
        try:
            if weight > 0 and height > 0:
                BMI=(weight)/((height)**2)
            if BMI < 18.5:
                print("Underweight")
            elif 18.5<=BMI<=24.9:
                print("Normal Weight")
            elif 25<=BMI<=29.9:
                print("Overweight")
            elif BMI>=30:
                print("Obesity")
            
            else:
                print("Enter only postive number")

        except Exception as e:
            print(f'the error is {e}')
            
    
    










