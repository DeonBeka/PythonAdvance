my_sets = set(1,2,3)
my_sets = set(1, 2, 2 ,3 , 3 , 3 )
my_sets1 = set()
print(my_sets1)
set1= {1,2,3}
set2 = {3,4,5}

unm = set1.union(set2)
umm = set1 | set2

print(unm)
print(umm)

irm = set1.intersection(set2)
iro = set1 & set2

print(irm)
print(iro)

drm = set1.difference(set2)
dro = set1 - set2
print(drm)
print(dro)

srm = set1.symmetric_difference(set2)
sro = set1 ^ set2
print(srm)
print(sro)

#methods
my_set2= {1,2,3}
my_set2.add(7)
my_set2.remove(3)
my_set2.discard(8)
print(my_set2)
my_set2.clear()
set2_len = len(my_set2)
print(set2_len)

mylist = [1,2,3,2,3,2,4,4,4]
unique_list = set(mylist)
unique_list = list(unique_list)
print(unique_list)

user1_interest = {"music", "movies", "travel"}
user2_interest = {"music", "reading", "cooking"}
common = user1_interest.intersection(user2_interest)
print(common)

colors = {"red", "green", "blue"}
color = "green"
print(color in colors)
print(color not in colors)


