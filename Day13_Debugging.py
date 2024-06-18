# Tips to tackle debugging
# 1.Describe Problem
# 2.Reproduce the Bug
# 3.Play Computer
# 4.Fix the Errors (they may show up or not eg- name error, f-string forgot)
# 5. Print is Your Friend
# 6. Use a Debugger
# 7. Take a break
# 8. Ask a friend (A real human not print :))
# 9. Run often (run after every little execution)
# 10. Ask stack overflow

# Problem
# target = int(input())
# for number in range(1, target + 1):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

# Solution
target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)