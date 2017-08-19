num =int(raw_input("Enter a number: "))
if num <= 1:
	print "The number is not prime."
else:
	x=2
	check = True
	while x != num:
		if num % x == 0:
			print "The number is not prime."
			check = False
			break
		x += 1
	if check == True:
		print "The number is prime."
