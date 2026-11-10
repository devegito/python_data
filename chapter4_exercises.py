for fighter in range(1,21):
    print(fighter)
    
soldiers=list(range(1,1000001))
print(min(soldiers))
print(max(soldiers))
print(sum(soldiers))

odds=list(range(1,21,2))
for odd in odds:
    print(odd)

threes=list(range(3,31,3))
for three in threes:
    print(three)

cubes=[]
for value in range(1,11):
    cube=value**3
    cubes.append(cube)

print(cubes)
cubes=[value**3 for value in range(1,11)]
print(cubes)