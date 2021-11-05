#!/usr/local/bin/python3

data=open("data.csv")
for i in data:
	data2=i.split(",")
	if data2[0]=="Drosophila melanogaster" or data2[0]=="Drosophila simulans":
		print(data2[2])
	if len(data2[1])>90 and len(data2[1])>90  <100:
		print(data2[2])
	counts=data2[1].count('a')+data2[1].count('t')
	percent=counts/len(data2[1])
	if round(percent,2)>0.5 and int(data2[3])>200:
		print(data2[2])
	
	if data2[2].startswith('k') or data2[2].startswith('h') and data2[2]!='Drosophila melanogaster':
		print(data2[2])
	counts=data2[1].count('a')+data2[1].count('t')
	percent=counts/len(data2[1])
	if round(percent,2)>0.65:
		print(data2[2],'high')
	elif round(percent,2)<0.45:
		print(data2[2],'low')
	else:
		print(data2[2],'medimum')
data.close()

