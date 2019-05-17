
import pytest

#test fixtures
@pytest.fixture
def measure_lines():
  measure = WithLines()
  return ComplexityMeter(measure)

@pytest.fixture
def measure_indents():
  measure = WithIndents()
  return ComplexityMeter(measure)

#test code
def test_empty_inputs_list_returns_empty_results_list(measure_lines):
  assert measure_lines.measure([]) == []

def test_single_input_returns_single_measure(measure_lines):
  assert len(measure_lines.measure([""])) == 1

@pytest.mark.parametrize(
  "file,                              expected_value",[
  ("",                                0),
  ("  ",                              1),#??
  ("one_liner",                       1),
  ("one_line\nline 2\nline 3",        3),
  ("one_line\nline 2\n",              2),
  ("\n\n\n\n\n\n",                    0)
])
def test_code_lines_complexity(file, expected_value, measure_lines):
  assert measure_lines.measure([file]) == [expected_value]

@pytest.mark.parametrize(
  "file,                              expected_value",[
  ("",                                0),
  ("  ",                              0),#??
  ("one_line\nline 2\nline 3",        0),#??
  ("\n\n\n\n\n\n",                    0),
  ("\tline",                          1),
  ("\t\tline",                        2)
])
def test_code_indents_complexity(file, expected_value, measure_indents):
  assert measure_indents.measure([file]) == [expected_value]

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
