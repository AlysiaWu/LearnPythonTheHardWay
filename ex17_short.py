# author Zhu Xiuwei
from sys import argv
script, from_f, to_f = argv
open(to_f,'w').write(open(from_f).read())