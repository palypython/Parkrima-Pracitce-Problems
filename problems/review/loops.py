"""
Loops review: use a loop to
construct a string that is the word "hello"
repeated 100 times, with each word on
a new line
"""

# we want 
# string = "hello\nhello\nhello\n....hello"
# 100 times
string=""
# the code will use a for loop like the one
# below: vvvvv

# for i in something:  
#   pass

for _ in range(100):
    print("hello")

# look at the tests to figure
# out how the program must behave
def tests(tester):
  l = string.split("\n")
  def get(i):
    return l[i] if i < len(l) else None
  tester.set_env(locals())
  tester.ae("len(l)", 100, "string should be 100 lines")
  for i in range(100):
    tester.ae(f"get({i})", "hello", f"line {i} should be 'hello'")