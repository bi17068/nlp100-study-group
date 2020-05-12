# 30. 形態素解析結果の読み込み
# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
from janome.tokenizer import Tokenizer
path = "neko.txt"
wpath = "ma.txt"
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

# with open(wpath, 'w') as f:
#     f.writelines(str(allLists(path)))

from pprint import pprint
pprint(allLists(path)[:10])
