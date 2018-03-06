import os
from Bio import SeqIO

########################################################################
def LoadDataBP(dbname,n):
	final_record=[]
	for i,filename in enumerate(os.listdir("Database/"+dbname)):
		if(n!=0):
			x=0
			for record_num,record in enumerate(SeqIO.parse("Database/"+dbname+"/"+filename,"fasta")):
				record.id="F"+str(i+1)+"|"+record.id
				record.description="F"+str(i+1)+"|"+record.description
				record.name="F"+str(i+1)+"|"+record.name
				if(len(record.seq)<200 and record_num<n+x):								#200 is because monomer length of heamoglobin was ~150
					final_record.append(record)
				else:
					x=x+1
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
	#selected_data=LoadDataBP("Globins",30)
	selected_data=LoadDataBP("Globins",0)
	print len(selected_data)
	SeqIO.write(selected_data, "Globins.fasta", "fasta")
	
	#outfile=open("Globins.fasta","w")
	#selected_examples=LoadData("Globins",30)
	#for i in selected_examples:
	#	outfile.write(i)
	#outfile.close()
	
if(__name__=="__main__"):
	main()
