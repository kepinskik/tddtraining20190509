
#test code
def test_empty_inputs_list_returns_empty_results_list():
  system = ComplexityMeter()
  input = []
  result = system.measure(input)
  assert result == []

def test_single_input_returns_single_measure():
  system = ComplexityMeter()
  input = [""]
  assert len(input[0]) == 0
  result = system.measure(input)
  assert len(result) == 1
  assert result == [0]


#production code
class ComplexityMeter:
  def __init__(self):
    pass

  def measure(self, input):
    return [len(x) for x in input]
