import os
########################################################################
def GetNumberofExamples(dbname):
	for i,filename in enumerate(os.listdir("Database/"+dbname)):
		temp=open("Database/"+dbname+"/"+filename).read().split('>')
		print filename,"| Number of Examples: ",len(temp)
	return 0

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
	#GetNumberofExamples("Globins")
	outfile=open("Globins.fasta","w")
	selected_examples=LoadData("Globins",30)
	for i in selected_examples:
		outfile.write(i)
	outfile.close()
	
if(__name__=="__main__"):
	main()
