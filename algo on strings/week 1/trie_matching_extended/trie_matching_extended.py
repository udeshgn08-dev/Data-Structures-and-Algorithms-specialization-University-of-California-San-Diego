# python3
import sys

# NA = -1

# class Node:
# 	def __init__ (self):
# 		self.next = [NA] * 4
# 		self.patternEnd = False

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
        curr_node['$'] = {} #adding a dollar symbol at the end
    return trie

def prefix_trie_matching(text, trie,external_index):
    index = 0 
    symbol = text[index] #start comparing from 0th index
    current = trie[0] #and also trie from 0th index
    res = -1 #default result 

    while True:
        if (not current) or ('$' in current):#if there is no node in this trie or next is the end
            return res
        if symbol in current: #check if there is link from this node to next level of nodes
            current = trie[current[symbol]] #move to that node
            res = external_index # change curr result to external index
            index += 1
            if index < len(text):
                symbol = text[index]
            elif '$' in current:
                return res
            else:
                symbol = '@'
                res = -1
        else:
            return res if '$' in current else -1

def solve(text, n, patterns):
    result = set()
    trie = build_trie(patterns)#BUILD TRIE USING FIRST WEEK FUNCTION
    n = len(text)
    
    for i in range(n):
        if prefix_trie_matching(text[i:], trie,i)!=-1:
            result.add(prefix_trie_matching(text[i:], trie,i))

    return sorted(list(result))

if __name__ == "__main__":
    text = sys.stdin.readline().strip()
#         text = input().strip()
    n = int(sys.stdin.readline().strip())
#     n = int(input().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]
#         patterns+= [ input().strip()]

    ans = solve(text, n, patterns)
#     print(' '.join(map(str,ans))+'\n')
    sys.stdout.write(' '.join(map(str, ans)) + '\n')