fruits = {}
cart = []
while True:
	print("1.Add fruit")
	print("2.Delete fruit by name")
	print("3.Search fruit by name and rate")
	print("4.Change fruit name and rate")
	print("5.Add to Cart")
	print("6.Display all fruits details") 
	print("7.exit")
	ch = int(input("Enter your choice\n"))
	if ch == 1:
		#Add fruit
		serial_no = input("\tEnter serial No ")
		if serial_no not in fruits.keys():
			id = input("\tEnter fruit id ")		
			name = input("\tEnter fruit name ")
			rate = int(input("\tEnter fruit rate "))
			imp_from = input("\tEnter fruit imported from ")
			imp_date = str(input("\tEnter the fruit imported date "))
			buy_price = input("\tEnter buy price of fruit")
			temp ={
				"id":id,
				"name":name,
				"rate":rate,
				"imp_from":imp_from,
				"imp_date":imp_date,
				"buy_price":buy_price
				}
			fruits[serial_no] = temp
		else:
			print("\tSerial No already Exists")
	elif ch == 2:
		#Delete fruit
		serial_no = input("\tEnter serial_no")
		if serial_no not in fruits.keys():
			print("\tFruit name does not exits")
		else:
			del fruits[serial_no]
	elif ch == 3:
		#Search fruit
		name = input("\tEnter fruit name")
		found = False
		for i in fruits.values():
			if i["name"] == name: # find name
				print(f"\t{i['id']} | {i['name']} | {i['rate']} | {i['imp_from']} | {i['imp_date']} | {i['buy_price']}")
				found = True
				break

		if found == False :
			print("\tNot found")
	elif ch== 4:
		#Change a fruit name in the list
		serial_no = input("\tEnter serial no.")
		if serial_no not in fruits.keys():
			print("\tWrong serial no")
		else:
			fruits[serial_no]['name'] = input("\tEnter new name")
	elif ch == 6:
		#Display fruit
		for serial,fruit in fruits.items():
			print(f"\t{serial} | {fruit['id']} | {fruit['name']} | {fruit['rate']}| {fruit['imp_from']} | {fruit['imp_date']} | {fruit['buy_price']}")
	elif ch == 7:
		#To exit
		break
	else:
		print("Invalid choice")
