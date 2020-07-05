from mamba import description, context, it
from expects import expect, equal

from fibonacci_last_digit import *

t_cases = [3,331,327305]
results = [2,9,5]
for t_case,inp in enumerate(t_cases):
	expect(get_fibonacci_last_digit_naive(inp)).to(equal(results[t_case]))
print('all the toy testcases have passed')