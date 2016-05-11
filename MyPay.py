
# hi. This is a little program

hourlyRate = input("Please enter you Hourly rate+ ")  		# Get user input. the hourly rate.
hourlyRate = float(hourlyRate)							# convert to a number just in case.

hoursWorked = input("Please enter total number of hours= ")	# get user input. number of hours
hoursWorked = float(hoursWorked)							# convert to a number just in case.

totalPay = hoursWorked * hourlyRate;

print("Total Pay = ", totalPay)

