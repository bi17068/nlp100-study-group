import random
import numpy as np

#FORMAT: ID \t TITLE \t URL \t PUBLISHER \t CATEGORY \t STORY \t HOSTNAME \t TIMESTAMP

with open('NewsAggregatorDataset/newsCorpora.csv') as f:
  filtering_at_publisher = []
  for line in f:
    publisher = line.split('\t')[3]
    if 'Reuters' == publisher or 'Huffington Post' == publisher or 'Businessweek' == publisher or 'Contactmusic.com' == publisher or 'Daily Mail' == publisher:
      filtering_at_publisher.append(line)

r_filtering_at_publisher = random.sample(filtering_at_publisher, len(filtering_at_publisher))
print(r_filtering_at_publisher[:1])

train_len = round(len(r_filtering_at_publisher) * 0.8)
train_list = r_filtering_at_publisher[:train_len]
vaild_len = (len(r_filtering_at_publisher) - train_len) // 2
vaild_list = r_filtering_at_publisher[train_len + 1:train_len + vaild_len]
test_list = r_filtering_at_publisher[train_len + vaild_len:]
print(len(r_filtering_at_publisher))
print(train_len)
print(len(test_list))
print(vaild_len)


with open('train.txt', mode='w') as f:
  f.write('\t'.join(train_list))
with open('valid.txt', mode='w') as f:
  f.write('\t'.join(vaild_list))
with open('test.txt', mode='w') as f:
  f.write('\t'.join(test_list))