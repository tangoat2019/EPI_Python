import re
from collections import Counter
def most_common_words(paragraph: str):
  reg = re.split('\W+', paragraph.upper())
  words = Counter(x for x in reg)
  return words.most_common(1)[0][0]
p = "Bob hit a ball, the hit BALL flew far after it was hit."
print(most_common_words(p))