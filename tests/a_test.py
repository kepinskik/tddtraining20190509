
import pytest

#test code
def test_empty_inputs_list_returns_empty_results_list():
  measure = WithLines()
  system = ComplexityMeter(measure)
  input = []
  result = system.measure(input)
  assert result == []

def test_single_input_returns_single_measure():
  measure = WithLines()
  system = ComplexityMeter(measure)
  input = [""]
  result = system.measure(input)
  assert len(result) == 1


@pytest.mark.parametrize(
  "file,                              expected_value",[
  ("",                                0),
  ("  ",                              1),
  ("one_liner",                       1),
  ("one_line\nline 2\nline 3",        3),
  ("one_line\nline 2\n",              2),
  ("\n\n\n\n\n\n",                    0)
])
def test_code_lines_complexity(file, expected_value):
  measure = WithLines()
  system = ComplexityMeter(measure)
  assert system.measure([file]) == [expected_value]

@pytest.mark.parametrize(
  "file,                              expected_value",[
  ("",                                0),
  ("  ",                              0),
  ("one_line\nline 2\nline 3",        0),
  ("\n\n\n\n\n\n",                    0),
  ("\tline",                          1),
  ("\t\tline",                        2)
])
def test_code_indents_complexity(file, expected_value):
  measure = WithIndents()
  system = ComplexityMeter(measure)
  assert system.measure([file]) == [expected_value]

#production code

class WithIndents:
  def __init__(self):
    pass

  def get(self, file):
    return file.count("\t")


class WithLines:
  def __init__(self):
    pass
  
  def get(self, file):
    return len(list(filter(lambda line: line != "", file.split('\n'))))


class ComplexityMeter:
  def __init__(self, measure):
    self._measure = measure

  def measure(self, input):
    return [self.measure_single(x) for x in input]

  def measure_single(self, file):
    return self._measure.get(file)
