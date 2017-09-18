"""
Some things relating to binomial coefficients.

"""

"""
Given n, k, and some prime p, this function returns the largest integer x such that p^x divides (n choose k), but p^{x+1} does not.

"""
def divisorsInBC(n, k, p):
	x = 1
	power = p
	divisors = 0
	while n > power:
		r = n % power
		rr = k % power

		if (r < rr):
			divisors += 1
		x += 1
		power *= p

	return divisors
	
