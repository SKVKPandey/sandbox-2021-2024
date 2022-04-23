names = {'Shashank', 'Seerat', 'Akshit', 'Sanchit', 
'Anubhava', 'Riya', 'Banshaj', 'Ojasvi', 'Owais', 
'Aditya D', 'Prince', 'Shreya', 'Kshitij', 'Manav', 'Aditya S'}

groups = []
for name in names:
    groups.append(name)

for i in range(0, len(names), 3):
    print(f'{(i//3) + 1}. {groups[i]}, {groups[i+1]}, {groups[i+2]}')

