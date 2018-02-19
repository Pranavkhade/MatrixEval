
"MEGA (Molecular Evolutionary Genetics Analysis) Computational Core
Authors: Koichiro Tamura, Glen Stecher, and Sudhir Kumar
URL: http://www.megasoftware.net/
License: See the usageAgreement.txt file
 
MEGA-CC is the command-line version of MEGA that implements its core
analysis functions and is useful for iterative and automated execution.
There are two executables, megacc and megaproto. You start with megaproto
which is used to create a MEGA Analysis Options (.mao) file that specifies
the analysis to run as well as relevant options. Then you call megacc from
a command shell and pass the .mao filename and input data filenames as parameters.
For example:

  megacc -a myMaoFile.mao -d mySequenceAlignment.fas -o myOutput

To get started, checkout MEGA7-CC-User-Manual.pdf"


