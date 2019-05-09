
#test code
def test_empty_inputs_list_returns_empty_results_list():
  system = ComplexityMeter()
  input = []
  result = system.measure(input)
  assert result == []

def test_single_input_returns_single_measure():
  system = ComplexityMeter()
  input = [""]
  result = system.measure(input)
  assert len(result) == 1

def test_empty_file_has_zero_measure():
  system = ComplexityMeter()
  input = [""]
  result = system.measure(input)
  assert result == [0]

def test_single_line_file_has_measure_1():
  system = ComplexityMeter()
  input = ["one_liner"]
  result = system.measure(input)
  assert result == [1]

def test_3_line_file_has_measure_3():
  system = ComplexityMeter()
  input = ["""one_line
  line 2
  line 3"""]
  result = system.measure(input)
  assert result == [3]


#production code
class ComplexityMeter:
  def __init__(self):
    pass

  def measure(self, input):
    return [self.measure_single(x) for x in input]

  def measure_single(self, file):
    if(len(file) == 0): return 0
    return len(file.split('\n'))
