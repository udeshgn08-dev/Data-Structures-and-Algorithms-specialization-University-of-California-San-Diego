# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    recent,last = 0,0
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
#             recent = 0
            if (last != next):
                recent = i
            last = next
#             if opening_brackets_stack[-1] == next:
#                 continue
#             else:
#                 recent = i

        if next in ")]}":
            if len(opening_brackets_stack)==0:
                return i+1
            elif are_matching(opening_brackets_stack[-1],next):
                opening_brackets_stack.pop()
                continue
            else:
                return i+1
    if len(opening_brackets_stack)!=0:
        return recent+1
    return 'Success'

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
