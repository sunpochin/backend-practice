# def my_generator():
#     for x in range(1, 100):
#         print("new value is generated!")
#         yield x
# gen_iter = my_generator()
# val = next(gen_iter)
# print("Value =", val)

# val = gen_iter.next()
# print("Value =", val)


def my_generator():

    x = 1
    print("new value is generated!")
    yield x
    x = x + 1
    print("new value is generated!")
    yield x
    x = x + 1
    print("new value is generated!")
    yield x


gen_iter = my_generator()
# for val in gen_iter:
#   print("Value =", val)


def yield_test(n):
    print("start n =", n)
    for i in range(n):
        yield i*i
        print("i =", i)
        print("\n")

    print("end")


tests = yield_test(5)
print("tests: ", tests)
# for test in tests:
#     print("test =", test)
#     print("--------")


def test():
    print("start...")
    while True:
      x = 10
      throw = yield x + 1
      print("throw:", throw)


p = test()
print(next(p))
print("-----------")
print(next(p))
print("-----------")
print(p.send(7))
print("-----------")
