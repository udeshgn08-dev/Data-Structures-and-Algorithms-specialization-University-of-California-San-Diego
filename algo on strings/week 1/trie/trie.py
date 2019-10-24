#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    '''uncomment print commands to know a little idea of what is happening'''
    trie = {}
    trie[0] = {}
    index = 1

    for pattern in patterns:
        curr_node = trie[0]
        for letter in pattern:
            if letter in curr_node.keys():  #if the alphabet is there in the Current paths emanating from Current node
#                 print('\n',letter,' is there \n')
                curr_node = trie[curr_node[letter]] #move to the next root node
#                 print('\n trie {} : \n'.format(trie), 'Current', curr_node)
            else:
                curr_node[letter] = index # adding node number to this letter, ex 0: {'a': 1} means 0-1 edge is a
                trie[index] = {} # creating dictionary for letters to follow the Current letter, ex: creating 1:{} so we can store  1-somenode
                #                 where some alphabet  is on edge 1-somenode
                curr_node = trie[index]  #shifting to the newly created node
#                 print('\n else loop trie{} \n'.format(trie))
                index = index + 1
    return trie

if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))

