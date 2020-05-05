from janome.tokenizer import Tokenizer
path = "neko.txt"

def allLists(path):
  with open(path) as f:
    s = f.read()
  t = Tokenizer()
  # c = 0
  all_list = []
  for line in s.split("\n"):
    # c += 1
    line_list = []
    for token in t.tokenize(line):
      word_map = {}
      word_map["surface"] = token.surface
      word_map["base"] = token.base_form
      word_map["pos"] = token.part_of_speech.split(',')[0]
      word_map["pos1"] = token.part_of_speech.split(',')[1]
      line_list.append(word_map)
    all_list.append(line_list)
    # if c == 20:
    #   break
  return all_list

def insert_no (text):
  preword = {}
  prepreword = {}
  ans = []
  for line in text:
    preword["base"] = ""
    preword["pos"] = ""
    prepreword["base"] = ""
    prepreword["pos"] = ""
    if len(line):
      for word in line:
        if prepreword["pos"] == "名詞" and preword["base"] == "の" and word["pos"] == "名詞":
          ans.append(prepreword["base"] + preword["base"] + word["base"])
        prepreword["base"] = preword["base"]
        prepreword["pos"] = preword["pos"]
        preword["base"] = word["base"]
        preword["pos"] = word["pos"]
  return ans

# def insert_no_first (text):
#   preword = {}
#   prepreword = {}
#   for line in text:
#     if len(line):
#       c = 0
#       for word in line:
#         if word["base"] == "の":

        
print(insert_no(allLists(path)))

