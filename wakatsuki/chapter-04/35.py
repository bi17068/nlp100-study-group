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

def noun_freq(text):
  preword = {}
  prepreword = {}
  ans = {}
  for line in text:
    if len(line):
      for word in line:
        if word["pos"] == "名詞":
          if word["base"] in ans:
            ans[word["base"]] += 1
          else :
            ans[word["base"]] = 1
  return sorted(ans.items(), key=lambda x:x[1], reverse=True)



        
print(noun_freq(allLists(path)))

