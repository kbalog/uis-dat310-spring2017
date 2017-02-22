""" List and Dictionary operation

Similar to the previous exercise, a dictionary stores five students' scores:
 `e = {'Adam':95, 'Lisa':85, 'Bart':59, 'Paul': 74, 'Dave':85}`.

Write a script that lists the name(s) of those who got 85 as score.
"""

e = {'Adam':95, 'Lisa':85, 'Bart':59, 'Paul': 74, 'Dave':85}
names = []
for k,v in e.items():
    if v == 85:
        names.append(k)
print(names)
