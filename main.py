# GAMZAT ABDULGALIMOV.
grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
print(grades)
students = {'Jonny','Bibo','Steve','Khendrik','Aaron'}
print(type(students))
students = list(students)
print(type(students))
students = sorted(students)
print(students)
g = sum(grades[0])
r = sum(grades[1])
a = sum(grades[2])
d = sum(grades[3])
e = sum(grades[4])
print(g,r,a,d,e)
s = g / len(grades[0])
t = r / len(grades[1])
u = a / len(grades[2])
d = d / len(grades[3])
n = e / len(grades[4])
print(s,t,u,d,n)
slovar = {students[0]:s,students[1]:t , students[2]: u, students[3]:d, students[4]:n}
print(slovar)














