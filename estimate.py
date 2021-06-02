import math
import unittest
import random

def wallis(n):
	x=1
	product=1
	while x<=n:
		product=product*((4*x*x)/((4*x*x)-1))
		x=x+1
	product=product*2
	return product
	
	
def monte_carlo(n):
	x=1
	circle=0
	total=0
	while x<=n:
		a=random.random()
		b=random.random()
		dist=math.sqrt((a*a)+(b*b))
		if dist<1:
			circle=circle+1
		total=total+1
		x=x+1
	ratio=circle/total
	pi=ratio*4
	return pi
		

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
