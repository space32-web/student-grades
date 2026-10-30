import os
def Average(Grades):
    if len(Grades)==0: return 0
    return sum(Grades)/len(Grades)
def best(students) :
    return max(students,key=lambda s:Average(students[s]))
students={'Иванов':[5,4,5],'Петров':[3,4,4],'Сидорова':[5,5,5]}
for name in students: print(name,round(Average(students[name]),2))
print('Лучший студент:',best(students))
