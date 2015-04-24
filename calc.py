from datetime import datetime

now = datetime.now()
nowstr = str(now)
hh = int(nowstr[11:13])
mm = int(nowstr[14:16])
working = True

print "The time is %s:%s" % (now.hour, now.minute)

wage = float(raw_input("How much do you make an hour?: $"))

def check_wages(wage):
    new = datetime.now()
    newstr = str(new)
    HH = int(newstr[11:13])
    MM = int(newstr[14:16])
    passed_h = int(HH - hh)
    passed_m = int(MM - mm)
    if passed_m < 0:
        passed_m = (60 - mm) + (MM)
    passed_m = passed_m / 60.0
    hours_worked = passed_h + passed_m
    wages_earned = hours_worked * wage
    return wages_earned


ready = raw_input("Are you ready to check your wages? Y/N ").lower()
while working == True:
    if ready == "y":
        current = check_wages(wage)
        print "You've made $%s so far today!" % (round(current, 2))
        ready = raw_input("Would you like to check your wages again? Y/N: ").lower()
    elif ready == "n":
        working = False
    else:
        pass
