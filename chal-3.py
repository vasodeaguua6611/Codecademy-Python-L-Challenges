def always_false(num):
  # sourcery skip: assign-if-exp, boolean-if-exp-identity, remove-unnecessary-cast
  if num > 1 and num < 1:
    return True
  else:
    return False
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False