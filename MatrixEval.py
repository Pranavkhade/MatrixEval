import os
from Bio import SeqIO

########################################################################
def LoadDataBP(dbname,n):
	for i,filename in enumerate(os.listdir("Database/"+dbname)):
		final_record=[]
		x=0
		if(n!=0):
			for record_num,record in enumerate(SeqIO.parse("Database/"+dbname+"/"+filename,"fasta")):
				record.id="F"+str(i+1)+"|"+record.id
				record.description="F"+str(i+1)+"|"+record.description
				record.name="F"+str(i+1)+"|"+record.name
				if(len(record.seq)<200):
					final_record.append(record)
				else:
					x=x+1
					print x
				if(record_num==n-x):
					continue
					
		else:
			for record in SeqIO.parse("Database/"+dbname+"/"+filename,"fasta"):
				record.id="F"+str(i+1)+"|"+record.id
				record.description="F"+str(i+1)+"|"+record.description
				record.name="F"+str(i+1)+"|"+record.name
				if(len(record.seq)<200):								#200 is because monomer length of heamoglobin was ~150
					final_record.append(record)
	return final_record

def LoadData(dbname,n):
	selected_examples=[]
	for i,filename in enumerate(os.listdir("Database/"+dbname)):
		multifasta=[]
		if(n!=0):
			temp=open("Database/"+dbname+"/"+filename).read().split('>')
			multifasta=multifasta+[">F"+str(i+1)+"|"+x for x in temp[1:n+1]]
			selected_examples.extend(multifasta)
		else:
			temp=open("Database/"+dbname+"/"+filename).read().split('>')
			multifasta=multifasta+[">F"+str(i+1)+"|"+x for x in temp]
			selected_examples.extend(multifasta)
	return selected_examples



########################################################################\
def main():
	print LoadDataBP("Globins",1)
	#outfile=open("Globins.fasta","w")
	#selected_examples=LoadData("Globins",30)
	#for i in selected_examples:
	#	outfile.write(i)
	#outfile.close()
	
if(__name__=="__main__"):
	main()
