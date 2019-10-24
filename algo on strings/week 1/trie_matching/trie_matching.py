# python3
import sys

# NA = -1

# class Node:
# 	def __init__ (self):
# 		self.next = [NA] * 4

# def solve (text, n, patterns):
# 	result = []

# 	// write your code here

# 	return result

# text = sys.stdin.readline ().strip ()
# n = int (sys.stdin.readline ().strip ())
# patterns = []
# for i in range (n):
# 	patterns += [sys.stdin.readline ().strip ()]

# ans = solve (text, n, patterns)

# sys.stdout.write (' '.join (map (str, ans)) + '\n')

def build_trie(patterns):
    trie = {}
    trie[0] = {}
    index = 1

    for pattern in patterns:
        curr_node = trie[0]
        for letter in pattern:
            if letter in curr_node.keys():  #if the alphabet is there in the Current paths emanating from Current node
                curr_node = trie[curr_node[letter]] #move to the next root node
            else:
                curr_node[letter] = index # adding node number to this letter, ex 0: {'a': 1} means 0-1 edge is a
                trie[index] = {} # creating dictionary for letters to follow the Current letter, ex: creating 1:{} so we can store  1-somenode
                #                 where some alphabet  is on edge 1-somenode
                curr_node = trie[index]  #shifting to the newly created node
                index = index + 1
    return trie

def prefix_trie_matching(text, trie):
    index = 0 
    symbol = text[index] #start comparing from 0th index
    current = trie[0] #and also trie from 0th index

    while True:
        if not current:  #if there is no node in this trie
            return True
        elif symbol in current.keys(): #check if there is link from this node to next level of nodes
            current = trie[current[symbol]] #move to that node
            index = index + 1 #and increase the index
            if index < len(text):
                symbol = text[index]
            else: 
                symbol = '$'
        else:
            return False

def solve(text, n, patterns):
    result = []
    trie = build_trie(patterns) #BUILD TRIE USING FIRST WEEK FUNCTION

    n = len(text)
    for i in range(n):
        if prefix_trie_matching(text[i:], trie):
            result.append(i)

    return result

if __name__ == "__main__":
    text = sys.stdin.readline().strip()
#     text = input().strip()
    n = int(sys.stdin.readline().strip())
#     n = int(input().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]
#         patterns+= [ input().strip()]

    ans = solve(text, n, patterns)
#     print(' '.join(map(str,ans))+'\n')
    sys.stdout.write(' '.join(map(str, ans)) + '\n')