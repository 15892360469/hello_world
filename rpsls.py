#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
2019.11.20
"""
# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("����������ѡ��:")
player_choice=input()#����Ϊ�ַ�����
print("----------------")

def name_to_number(name):#�����û���ѡ�񣬲�����ת��Ϊ����
	if name=="ʯͷ":
		name=0
	if name=="ʷ����":
		name=1
	if name=="��":
		name=2
	if name=="����":
		name=3
	if name=="����":
		name=4
	return name
player_choice_number=name_to_number(player_choice)#���к���

import random#����random����
comp_number=random.randrange(0,5)#�����Ը�ֵһ�������

def rpsls(player_choice_number,comp_number):#�ж���Ӯ
	if player_choice_number==comp_number:
			print("���ͼ��������һ����")
	elif player_choice_number==0 and comp_number==(4 or 3):
			print("��Ӯ��")
	elif player_choice_number==1 and comp_number==(4 or 0):
			print("��Ӯ��")
	elif player_choice_number==2 and comp_number==(0 or 1):
			print("��Ӯ��")
	elif player_choice_number==3 and comp_number==(1 or 2):
			print("��Ӯ��")
	elif player_choice_number==4 and comp_number==(2 or 3):
			print("��Ӯ��")
	else:
			print("����Ӯ��")
	return print

def number_to_name(number):#�����������ת���ɶ�Ӧ�Ľ��
	if number==int(0):
		number="ʯͷ"
	if number==int(1):
		number="ʷ����"
	if number==int(2):
		number="��"
	if number==int(3):
		number="����"
	if number==int(4):
		number="����"
	return number
comp_number_name=number_to_name(comp_number)#���к���

if player_choice_number not in [0,1,2,3,4]:#�ж������Ƿ�Ϊ�����ڵ�ѡ��
	print("Error: No Correct")
else:
	print("����ѡ��Ϊ��%s"%player_choice)
	print("�������ѡ��Ϊ��%s"%comp_number_name)
	print(rpsls(player_choice_number,comp_number))
	
