a=input("Enter the data \n")    # escape character
print(a)

#addition
number1 = input("Enter the first number \n")
number2 = input("Enter the second number \n")
answer = int(number1)+int(number2)
print(answer)

print("Justin\n" * 10)

listofname=["Java","Python","PHP","NodeJS"]
for i in listofname:
	print(i)
	
newinput = input("Enter new input data \n")

listofname.append(newinput)

print("New input is added successfully")
for i in listofname:
	print(i)

