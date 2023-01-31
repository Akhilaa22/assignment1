import random
traffic_light=['red','yellow','green']
traffic_light=random.choice(traffic_light)
print(traffic_light)
if(traffic_light=='red'):print('stop')
 elif(traffic_light=='yellow'):print('get ready to stop')
else:
print("go")
