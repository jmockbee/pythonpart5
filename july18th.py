hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# floor division returns the integer value of the the quotient. (it dumps the decimal)
#  dura//60

print('end time: ', ((hour + (min*dura)//60)%24)                                    %60  )


# Write your code here.