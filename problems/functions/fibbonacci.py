"""
Create the fibonnacci function
see https://en.wikipedia.org/wiki/Fibonacci_number

fib(0) = 0
fib(1) = 1
fib(2) = 1
...
fib(n) = fib(n-1)+fib(n-2)
"""

def fibbonacci(n):
  pass # not implemented yet

  
# this functions tests if your program 
# is actually correct, do not touch it.  
def tests(tester):
  fibs=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
  fib=fibbonacci
  tester.set_env(locals())
  for idx,e in enumerate(fibs):
    tester.ae(f"fib({idx})",e,f"{idx}th fibonnaci number")
  