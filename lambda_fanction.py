# lambda関数(無名関数)

s = lambda x: x + x

print(s(3))

def power(exponent):
  return lambda base: base ** exponent

third_power = power(3)
print(third_power(2))

numbers = [6, 2, 3, 43, 5, 36, 67, 2]
# filter()

def filterfunc(num):
  if num % 2 == 0:
    return False
  else:
    return True

filtered_num = filter(filterfunc,numbers)
print(list(filtered_num))
# for num in numbers:
#   print(filterfunc(num))