from janome.tokenizer import Tokenizer
path = "neko.txt"

def allLists(path):
  with open(path) as f:
    s = f.read()
  t = Tokenizer()
  c = 0
  all_list = []
  for line in s.split("\n"):
    line_list = []
    for token in t.tokenize(line):
      word_map = {}
      word_map["surface"] = token.surface
      word_map["base"] = token.base_form
      word_map["pos"] = token.part_of_speech.split(',')[0]
      word_map["pos1"] = token.part_of_speech.split(',')[1]
      line_list.append(word_map)
    all_list.append(line_list)

  return all_list

c = 0
for line in allLists(path):
  for map in line:
    print(map["surface"])
  c += 1
  if c == 10:
    break