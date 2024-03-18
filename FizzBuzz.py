for pointer in range(1, 101):
  if pointer % 3 == 0 and pointer % 5 == 0:
    print("FizzBuzz")
  elif pointer % 3 == 0:
    print("Fizz")
  elif pointer % 5 == 0:
    print("Buzz")
  else:
    print(pointer)
