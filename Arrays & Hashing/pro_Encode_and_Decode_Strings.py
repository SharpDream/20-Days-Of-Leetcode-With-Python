class Solution:

def encode(self, strs):
    en = []
    for x in strs:
        en.append(f"{len(x)}#{x}")
    return "".join(en)

def decode(self, s):
    de = []
    i = 0
    while i<len(s):
        hashtag = s.find("#", i)
        length = int(s[i:hashtag])
        de.append(s[hashtag+1:length+1+hashtag])
        i = length + 1 + hashtag
    return de
