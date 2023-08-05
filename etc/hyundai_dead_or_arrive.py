# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
car_number = input()
car_list = [list(map(int, input().split())) for _ in range(int(car_number))]
#print ("car number " + car_number)
#print ("car_list " , car_list)

car_dic = {}
for i in range(len(car_list)):
	if car_dic.get(str(car_list[i][0])) is None:
		car_dic[str(car_list[i][0])] = [i,car_list[i][1]]
	elif car_dic[str(car_list[i][0])][1] <= car_list[i][1]:
		car_dic[str(car_list[i][0])] = [i,car_list[i][1]]

#print(car_dic)
answer = 0
for key, value in car_dic.items() :
    answer += value[0]+1
		
print(answer)