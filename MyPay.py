
# hi. This is a little program
overTimeRate = 1.5                                              # Set overtime rate to 1.5/ Time and a half.
continueLoop = "1"                                                # initialize loop flag to 1. continue loping.

while continueLoop == "1" :
    hourlyRate = input("Please enter you Hourly rate= ")  		# Get user input. the hourly rate.
    hourlyRate = float(hourlyRate)					# convert to a number just in case.

    hoursWorked = input("Please enter total number of hours= ")	# get user input. number of hours
    hoursWorked = float(hoursWorked)				# convert to a number just in case.

    if( hoursWorked >40):
        overTimeHours = hoursWorked - 40
        hoursWorked = 40
    else:
        overTimeHours = 0

    # print(overTimeHours)                                      # helper function to find bug in calculations. not needed in run time.
    # print(overTimeHours * hourlyRate * overTimeRate)          # helper function to find bug in calculations. not needed in run time.
        
    totalPay = (hoursWorked * hourlyRate) + (overTimeHours * hourlyRate * overTimeRate)

    print("Total Pay = ", totalPay)

    continueLoop = input("Press 1 to run again")
    print(continueLoop)
else :
    print("Thank you .  Bye.")
    

