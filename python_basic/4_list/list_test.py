my_list = [1,2,3,4]
my_list2 = [5,6,7,8]

for item1 in my_list:
    for item2 in my_list2:
        print(item1,item2)

print(my_list.pop(1))
del my_list2[1]
print(my_list)
print(my_list2)
del my_list2[1:3]
print(my_list2)

#tuple 생성(Packing)
movie = 'superman',1987,'batman',1989,
print(type(movie))

#tuple 항목별 할당(unpacking)
t1,y1,t2,y2 = movie
print(t1,y1,t2,y2)
print(type(y1))


my_set = {'java','python','java','c++',}
print(my_set)
#my_set2 = my_set['java'] = 'Java'
#print(my_set2)

my_list = [4,3,5,1]
#my_set = set(my_list)
#print(my_set)
my_list = list(set(my_list))
print(my_list)

set1 = {'a','b','c'}
set2 = {'b','d','e'}
#차집합
result = set1 - set2
print(result)
#여집합
result = set1 ^ set2
print(result)

my_dict = {}
print(type(my_dict))
my_dict = dict()
print(type(my_dict))
my_dict = {'red':10,'blue':5,'red':20,'Red':40}
print(my_dict)
keys = my_dict.keys()
print(type(keys))
print(sorted(keys))
values = my_dict.values()
print(type(values))
items = my_dict.items()
print(type(items))
#값 변경
my_dict['red'] = 30
print(my_dict)
# key 존재 여부 확인
print('blue' in my_dict)
print(my_dict)

#값이 존재하는지 여부 체크
print(40 in my_dict.values())

#키가 존재하는지 여부 체크
print('red' in my_dict)
print('red' in my_dict.keys())