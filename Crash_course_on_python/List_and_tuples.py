def guest_list(guests):
	for name, age, profession in guests:
		print(("{} is {} years old and works as {}").format(name, age,profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
