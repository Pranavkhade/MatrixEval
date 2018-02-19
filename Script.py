"""
Created: 17 Jan 2018
Author: Pranav Khade (pranavk@iastate.edu)
"""

import argparse
import os
from Bio import SeqIO
from Bio import Phylo
from StringIO import StringIO
from Bio import AlignIO
from Bio.Align.Applications import MuscleCommandline
########################################################################
MEGA_location="MEGA/"
method="likelyhood.mao"
GeneratePDF=False

########################################################################Parser
def init():
	if not os.path.exists("output"):
		os.makedirs("output")
	else:
		for f in os.listdir("output"):
			file_path = os.path.join("output",f)
			if os.path.isfile(file_path):
				os.unlink(file_path)
	results=open("results/tress.txt","w")
	return True

def parser():
	parser=argparse.ArgumentParser()
	parser.add_argument("-n",type=int,help="Number of examples (FASTA) to be selected from the each file.(0=All files)")
	parser.add_argument("-f",type=file,nargs="+",help="Select multifasta files from which examples are to be selected.")
	args=parser.parse_args()
	return args
########################################################################Functions
"""Write file from array."""
def WriteFileFromList(given_list,filename):
	fh=open(filename,"w")
	for i in given_list:
		fh.write(i)
	return True

def SelectNFromFasta(args):
	before_alignment_filename="before-alignment.fasta"
	multifasta=[]
	n=args.n
	if(n!=0):
		for i,fh in enumerate(args.f):
			temp=fh.read().split('>')
			#print ">Family",i+1,"|",temp[1:n]
			multifasta=multifasta+[">Family"+str(i+1)+"|"+x for x in temp[1:n+1]]
	else:
		for i,fh in enumerate(args.f):
			temp=fh.read().split('>')
			multifasta=multifasta+[">Family"+str(i+1)+"|"+x for x in temp]
	WriteFileFromList(multifasta,before_alignment_filename)
	return before_alignment_filename

def GenerateTree(matrix_name,multifasta_filename,show_pdf):
	results=open("results/tress.txt","a")
	cline = MuscleCommandline(input=multifasta_filename,out=matrix_name+".fasta",matrix=matrix_name)
	stdout,stderr=cline()
	os.system(MEGA_location+"megacc True -d "+matrix_name+".fasta -o output/"+matrix_name+" -a "+method)
	tree=Phylo.read("output/"+matrix_name+"_consensus.nwk","newick")
	results.write("KMAT Tree:\n")
	Phylo.draw_ascii(tree,file=results)
	results.close()
	if(GeneratePDF):
		Phylo.draw(tree,do_show=show_pdf)
	return True
########################################################################
def main():
	init()
	#args=parser()
	#multifasta_filename=SelectNFromFasta(args)
	multifasta_filename="Globins.fasta"
	
	#From KMAT
	GenerateTree("KMAT",multifasta_filename,False)
		
	#From BLOSUM62
	GenerateTree("BLOSUM62",multifasta_filename,True)

main()
