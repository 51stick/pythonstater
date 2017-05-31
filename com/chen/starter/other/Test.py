from collections import namedtuple

'''列表推导'''
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(size, color) for size in sizes for color in colors]

print(tshirts)

print([i for i in range(10) if i > 5])

'''生成器'''
for shirt in [(size, color) for size in sizes for color in colors] :
    print(shirt)

'''数据交换'''
a,b = 1, 2
print("%r, %r" % (a, b))
a,b = b, a
print("%r, %r" % (a, b))

'''具名元祖'''
City = namedtuple('City', 'name address age')
chengdu = City('Chengdu', 'chengdu', 20)
print(chengdu.name, chengdu.address, chengdu.age)
print(chengdu[0], chengdu[1], chengdu[2])