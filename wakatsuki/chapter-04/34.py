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

def noun_series(text):
  preword = {}
  prepreword = {}
  ans = []
  series = ""
  for line in text:
    f = 0
    for word in line:
      if word["pos"] == "名詞":
        series += word["base"]
        f += 1
      elif f >= 2 :
        ans.append(series)
        series = ""
        f = 0
      elif f <= 1 :
        f = 0
        series = ""

  return ans



        
print(noun_series(allLists(path)))

