#definig variables
days=0
squats=0
total=0
print("enter the no.of squats you did on last one week")
#body of loop
while days<=6:
    days=days+1
    squats=int(input("squats on day {}:".format(days)))
    total=total+squats
#statement outside of loop
avg=total/days
print("in the last {} days,you did an avg of {} squats:" .format(days,avg))
