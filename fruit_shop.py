fruits = [] 

while True:
	print("1. Add fruit")
	print("2. Delete fruit")
	print("3. Search fruit by name and rate")
	print("4. Change fruit name and rate")
	print("5. Display all fruits name with rate") 
	print("6. exit")
	ch = int(input("Enter your choice\n"))

	if ch == 1:
		#Add fruit
		f_name = input("Enter fruit name")
		f_rate = input("Enter fruit rate")
		fruits.append([f_name,f_rate])
		#fruits.append(input("Enter name"))
	elif ch == 2:
		#Delete fruit
		print(fruits)
		print("Choose any fruit from the list")
		f_name = input("Enter fruit to delete")
		for i in range(0,len(fruits)):
			if fruits[i][0] == f_name:
				fruits.pop(i)
#				print(f_name+"fruit is deleted")
	elif ch == 3:
		#Search fruit
		f_name = input("Enter fruit you want to search")
		if f_name in fruits[i]:
			print(f_name + " is in the shop")
		else:
			print(f_name + "not in the shop")
	elif ch== 4:
		#Change a student name in the list
		#Index,remove,insert
		#Index,assignment
		f_name = input("Enter the fruit name")
		f_rate = input("Enter the fruit rate")
		new_fruit = input("Enter the fruit name to change")
		new_rate = input("Enter the fruit rate to change")
		for i in (0,len(fruits)):
			if(fruits[i][0] == name and fruits[i][1] == rate):
				print("Entered")
				fruits[i] = [new_fruit,new_rate]
				break
		#students[students.index(name)] = input("Enter new name")
	elif ch == 5:
		#Display fruits
		print(fruits)
	elif ch == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")
