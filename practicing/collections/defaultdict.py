from collections import defaultdict

groups = defaultdict(list)

print(groups)

students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]

for student, group in students:
    groups[group].append(student)

print(groups)
print(groups[2])
print(groups[200])
print(groups)

groups.clear()

print(groups)