from Tkinter import *
from datetime import datetime

nowlist = []
def get_time():
    del nowlist[0:len(nowlist)]
    now = datetime.now()
    nowstr = str(now)
    hh = int(nowstr[11:13])
    nowlist.append(hh)
    mm = int(nowstr[14:16])
    nowlist.append(mm)
    return nowlist

win = Tk()
v = StringVar()
u = StringVar()

def check_wages():
    wage = float(v.get())
    new = datetime.now()
    newstr = str(new)
    HH = float(newstr[11:13])
    MM = float(newstr[14:16])
    hh = nowlist[0]
    mm = nowlist[1]
    passed_h = float(HH - hh)
    passed_m = float(MM - mm)
    if passed_m < 0:
        passed_m = (60 - mm) + (MM)
    passed_m = passed_m / 60.0
    hours_worked = passed_h + passed_m
    wages_earned = round(hours_worked * wage, 2)
    t1.delete("1.0", END)
    t1.insert(INSERT, wages_earned)


f1 = Frame(win)
l1 = Label(f1, text="What is your hourly wage? $")
l2 = Label(f1, text="What state do you live in?")
e1 = Entry(f1, textvariable=v, width=5)
e2 = Entry(f1, textvariable=u, width=2)
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
f1.pack()

f2= Frame(win)
b1 = Button(f2, text="Start Work", command=get_time)
b2 = Button(f2, text="Check Wages", command=check_wages)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
f2.pack()

f3 = Frame(win)
l3 = Label(f3, text="So far today, you've made: $")
t1 = Text(f3, height=1, width=7)

l3.grid(row=0,column=0)
t1.grid(row=0,column=1)
f3.pack()

win.mainloop()
