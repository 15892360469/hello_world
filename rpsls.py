#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：邓玉龙
2019.11.20
"""
# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("请输入您的选择:")
player_choice=input()#输入为字符串型
print("----------------")

def name_to_number(name):#输入用户的选择，并将其转化为数字
	if name=="石头":
		name=0
	if name=="史波克":
		name=1
	if name=="布":
		name=2
	if name=="蜥蜴":
		name=3
	if name=="剪刀":
		name=4
	return name
player_choice_number=name_to_number(player_choice)#运行函数

import random#导入random函数
comp_number=random.randrange(0,5)#给电脑赋值一个随机数

def rpsls(player_choice_number,comp_number):#判断输赢
	if player_choice_number==comp_number:
			print("您和计算机出的一样呢")
	elif player_choice_number==0 and comp_number==(4 or 3):
			print("您赢了")
	elif player_choice_number==1 and comp_number==(4 or 0):
			print("您赢了")
	elif player_choice_number==2 and comp_number==(0 or 1):
			print("您赢了")
	elif player_choice_number==3 and comp_number==(1 or 2):
			print("您赢了")
	elif player_choice_number==4 and comp_number==(2 or 3):
			print("您赢了")
	else:
			print("电脑赢了")
	return print

def number_to_name(number):#将计算机数字转换成对应的结果
	if number==int(0):
		number="石头"
	if number==int(1):
		number="史波克"
	if number==int(2):
		number="布"
	if number==int(3):
		number="蜥蜴"
	if number==int(4):
		number="剪刀"
	return number
comp_number_name=number_to_name(comp_number)#运行函数

if player_choice_number not in [0,1,2,3,4]:#判断输入是否为规则内的选择
	print("Error: No Correct")
else:
	print("您的选择为：%s"%player_choice)
	print("计算机的选择为：%s"%comp_number_name)
	print(rpsls(player_choice_number,comp_number))
	
