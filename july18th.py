hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# floor division returns the integer value of the the quotient. (it dumps the decimal)
#  dura//60

print("End  Time:", ((hour + (mins+dura)//60)%24), ":", (mins+dura) % 60)


