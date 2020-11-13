import jsabacusframework
import fileinput

def test_part1_example_1():
  data = '[1,2,3]'
  assert jsabacusframework.part1(data) == 6

def test_part1_example_2():
  data = '{"a":2,"b":4}'
  assert jsabacusframework.part1(data) == 6

def test_part1_example_3():
  data = '[[[3]]]'
  assert jsabacusframework.part1(data) == 3

def test_part1_example_4():
  data = '{"a":{"b":4},"c":-1}'
  assert jsabacusframework.part1(data) == 3

def test_part1_example_5():
  data = '{"a":[-1,1]}'
  assert jsabacusframework.part1(data) == 0

def test_part1_example_6():
  data = '[-1,{"a":1}]'
  assert jsabacusframework.part1(data) == 0

def test_part1_example_7():
  data = '[]'
  assert jsabacusframework.part1(data) == 0

def test_part1_example_8():
  data = '{}'
  assert jsabacusframework.part1(data) == 0

def test_part1():
  with open(jsabacusframework.input_file) as f:
    data = f.read()
  expected = 111754
  assert jsabacusframework.part1(data) == expected

def test_part2_example_1():
  data = '[1,2,3]'
  assert jsabacusframework.part2(data) == 6

def test_part2_example_2():
  data = '[1,{"c":"red","b":2},3]'
  assert jsabacusframework.part2(data) == 4

def test_part2_example_3():
  data = '{"d":"red","e":[1,2,3,4],"f":5}'
  assert jsabacusframework.part2(data) == 0

def test_part2_example_4():
  data = '[1,"red",5]'
  assert jsabacusframework.part2(data) == 6

def test_part2():
  with open(jsabacusframework.input_file) as f:
    data = f.read()
  expected = 65402
  assert jsabacusframework.part2(data) == expected
