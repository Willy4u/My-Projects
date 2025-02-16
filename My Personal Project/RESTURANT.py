Nachos = Pizza= 6.00
Cheessburger = 10.00
Water = 4.00
Coke = 5.00
Tax = 0.07



order = [ x for x in input().split()]

cost = 0

dummy = ['Nachos','Cheessburger','Water','Coke']

for i in order:
    if i == 'Nachos':
        cost+= Nachos
    else:
        cost+= 0

    if i == 'Pizza':
        cost+= Pizza

    else:
        cost+= 0

    if i == 'Cheessburger':
        cost+= Cheessburger
    else:
        cost+=0

    if i == 'Water':
        cost+= Water
    else:
        cost+=0
    if  i == 'Coke':
        cost+=Coke
    else:
        cost+=0
    if i not in dummy:
        cost+=Coke

plustax = (cost*Tax) + cost
print(plustax)
