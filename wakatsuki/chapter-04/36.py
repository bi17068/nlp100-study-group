from janome.tokenizer import Tokenizer
from JapaneseAnalyz import *

path = "neko.txt"
wpath = "ma.txt"

analyze = JapaneseAnalyz()


for line in analyze.allLists(path)[:5]:
  print(line)

