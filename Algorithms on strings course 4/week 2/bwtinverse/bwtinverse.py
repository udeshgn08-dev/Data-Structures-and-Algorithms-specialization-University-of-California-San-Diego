# python3
import sys

def InverseBWT(bwt):
    A_count, C_count, G_count , T_count = 1, 1, 1, 1
    last_col_numbered = ['A'] *len(bwt)
    for idx,c in enumerate(bwt):
        if c == '$':
            last_col_numbered[idx] ='$' #there is only one $
        elif c == 'A':
            last_col_numbered[idx] = 'A'+str(A_count)
            A_count += 1
        elif c == 'C':
            last_col_numbered[idx] = 'C'+ str(C_count)
            C_count += 1
        elif c == 'G':
            last_col_numbered[idx] = 'G'+ str(G_count)
            G_count += 1
        else:
            last_col_numbered[idx] = 'T'+ str(T_count)
            T_count += 1
    first_col_numbered = sorted(last_col_numbered)
#     print(first_col_numbered)
#     first_to_last_map = {}
    first_to_last_map = dict(zip(first_col_numbered,last_col_numbered))
#     print(first_to_last_map)
    #     for i in range(len(first_col_numbered)):
#         first_to_last_map[first_col_numbered[i]] = last_col_numbered[i] #key is first letter of the string and it's value is the last letter of it
#     print(first_to_last_map)
    result = ['A']*len(bwt)
    nextChar = ('$')
    i = 0
    while i < len(first_col_numbered):
        result[i] = nextChar[0]
        nextChar = first_to_last_map[nextChar]
        i+=1
    return ''.join(result[::-1])

# def InverseBWT(bwt):
# 	A, C, G , T = 1, 1, 1, 1
# 	lastColunm = []
# 	for c in bwt:
# 		if c == '$':
# 			lastColunm.append(('$', 0))
# 		elif c == 'A':
# 			lastColunm.append(('A', A))
# 			A += 1
# 		elif c == 'C':
# 			lastColunm.append(('C', C))
# 			C += 1
# 		elif c == 'G':
# 			lastColunm.append(('G', G))
# 			G += 1
# 		else:
# 			lastColunm.append(('T', T))
# 			T += 1
# 	firstColunm = sorted(lastColunm)
# 	firstToLast = {}
# 	for i in range(len(firstColunm)):
# 		firstToLast[firstColunm[i]] = lastColunm[i]
# 	result = ""
# 	nextChar = ('$', 0)
# 	while len(result) < len(firstColunm):
# 		result += nextChar[0]
# 		nextChar = firstToLast[nextChar]
# 	result = result[::-1]
# 	return result

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))