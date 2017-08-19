	def palindrome():
	seq = raw_input("Enter a sequence: ")
	line = ""
	for letter in seq:
		if letter == "A":
			line += "T"
		if letter ==  "T":
			line += "A"
		if letter == "C":
			line += "G"
		if letter == "G":
			line += "C" 
	seq2 = line[ : :-1]
	if seq2 == seq:
		print("The sequence is a palindrome")
	else:
		print("The sequence is not a palindrome")
