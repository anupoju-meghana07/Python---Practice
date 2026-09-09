"""#1.Student Marks

marks = []
# Accept 3 marks
for i in range(3):
    mark = int(input("Enter mark: "))
    marks.append(mark)
print("Original marks:", marks)
# Insert 90 at beginning
marks.insert(0, 90)
# Add 75 and 85
marks.extend([75, 85])
# Remove 75 if it exists
if 75 in marks:
    marks.remove(75)
    print("75 removed")
# Remove final mark
removed = marks.pop()
print("Removed final mark:", removed)
# Final list and length
print("Final marks:", marks)
print("Number of marks:", len(marks)) 

#2.Number list Analyzer

numbers = [20, 10, 30, 20, 40, 20]
# Sort in ascending order
numbers.sort()
print("Ascending order:", numbers)
# Reverse to descending order
numbers.reverse()
print("Descending order:", numbers)
# Search for a number
search = int(input("Enter a number to search: "))
if search in numbers:
    print("Number found")
    print("Count:", numbers.count(search))
    print("First index:", numbers.index(search))
else:
    print("Number not found")
# Numerical summary
print("Smallest value:", min(numbers))
print("Largest value:", max(numbers))
print("Total:", sum(numbers)) 

#3.Even Odd Seperator

numbers = [10, 15, 20, 25, 30, 35]
even = []
odd = []
# Separate even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even numbers:", even)
print("Odd numbers:", odd)
# Slicing
print("First three values:", numbers[:3])
print("Last three values:", numbers[-3:])
# Create backup
backup = numbers.copy()
# Clear original list
numbers.clear()
print("Original list after clear:", numbers)
print("Backup list:", backup) 

#4.Unique Name Manager

names = ["Asha", "Rahul", "Asha", "John", "Rahul"]
# Convert list to set
unique_names = set(names)
# Add Meera
unique_names.add("Meera")
# Add Arun and Priya
unique_names.update(["Arun", "Priya"])
# Remove John if he exists
if "John" in unique_names:
    unique_names.remove("John")
# Try to remove David safely
unique_names.discard("David")
# Display every unique name
print("Unique names:")
for name in unique_names:
    print(name)              """
    
#5.Course Student Comparision 

python_data={"Asha","Rahul","John","Meera"}
da_students={"Rahul","Meera","Arun"}
#Union
all_students=python_data.union(da_students)
#Intersection
all_students=python_data.intersection(da_students)
#Only Python Students
python_students=python_data.difference(da_students) 





