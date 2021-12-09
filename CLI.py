import sys
from typing import Dict

args = sys.argv
for i, a in enumerate(args):
    print(a)
print(args)
if "--input-dir" == args[i]:
    print("filtre")
    inputdir = args[i + 1]
    print(inputdir)

if "--output-dir" == args[i]:
    print("filtre")
    outputdir = args[i + 1]
    print(outputdir)




#résultat cli dictionnaire