import time
day=time.strftime("%A, %d/%m(%b)/%Y , %H:%M:%S");
hour=int(time.strftime("%H"))
if( hour < 4):
    print("Its late at night... why still upp??!")
elif(hour <12 and hour >= 4):
    print("Good morning!How u doing?")
elif(hour >=12 and hour <17):
    print("Good afternoon!How u doing?")
elif(hour >=17):
    print("Good evening!How u doing?")
print(day)