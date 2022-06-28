import sys

#check number of arguments
if len(sys.argv) == 1:
	sys.exit(1)
if len(sys.argv) > 2:
	assert False, "Assertion error: wrong number of arguments"

#convert string to int
try:
	int_arg = int(sys.argv[1])
except ValueError:
	assert False, "Assertion error: argument is not an integer"

if int_arg:
	if (int_arg % 2) == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")