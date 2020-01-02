#coding=utf-8
"""
黎明破晓的街道数据可视化
作者：邓玉龙
2020.1.1
"""
import jieba,codecs
import jieba.posseg as pseg

names ={}
relation={}
lineNames =[]

jieba.load_userdict("dict.txt")#引用自定义的字典，避免jieba识别人物错误。
with codecs.open("黎明破晓的街道.txt", "r") as f:
	for line in f.readlines():
		x=pseg.cut(line)#将每一行分词,得到的每个词有两个参数，第一个为词，第二个为词性。
		lineNames.append([])#每一行作为一个单位，内容是每一行的名字
		for y in x:
			if y.flag!="nr" or len(y.word)<2:#过滤掉不必要的词
				continue
			else:
				lineNames[-1].append(y.word)
				if names.get(y.word,0)==0:#names字典中添加所有可能存在的人名并统计次数
					names[y.word]=0
					relation[y.word] ={}
				names[y.word]+=1

#每一行的人物之间互相建立关联并以字典形式统计次数,默认出现在同一排为有关联。
for line in lineNames:
	for name1 in line:
		for name2 in line:
			if name1 == name2:
				continue
			if relation[name1].get(name2,0)==0:
				relation[name1][name2]=0
			relation[name1][name2]+=1

#建立节点集合
with codecs.open("file1.txt","w") as f:
	f.write("Id Label Weight\n")
	for name,times in names.items():
		f.write(name + " " + name + " " + str(times) + "\n")


#建立边集合
with codecs.open("file2.txt", "w") as f:
	f.write("Source Target Weight\n")
	for name, edges in relation.items():
		for v, w in edges.items():
			if w >3:#过滤关联次数太少的联系
				f.write(name + " " + v + " " + str(w) + "\n")
