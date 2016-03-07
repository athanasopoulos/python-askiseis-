from bitarray import bitarray
import mmh3
import urllib
import os


class BloomFilter:
    
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        
    def add(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            self.bit_array[result] = 1
            
    def lookup(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            if self.bit_array[result] == 0:
                
                return "--%s--"%(words_list[i])
        return "Probably"
            


bf = BloomFilter(500000, 7)



link_leksiko="https://gunet2.cs.unipi.gr/modules/document/file.php/TMA111/american-english.txt"
htmltext = urllib.urlopen(link_leksiko).read()
file = open("american-english.txt", "w")
file.write(htmltext)
file.close()
lines = open("american-english.txt").read().splitlines()
for line in lines:
    bf.add(line)



k=raw_input("balte onoma arxeiou:")
open_file = open(k+".txt", 'r')
words_list =[]
data=[]
contents= open_file.readlines()
for i in range(len(contents)):
        words_list.extend(contents[i].split())
for i in range(len(words_list)):
        words_list[i]= bf.lookup(words_list[i])

print ' '.join(words_list)



os.remove("american-english.txt")



