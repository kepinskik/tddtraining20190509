# tddtraining 20190509

What should make all things runnable:

```
pyenv local 3.7.1
pyenv virtualenv venv_tdd
pyenv activate venv_tdd
pip install pytest
pytest
```

###**Pro** VSCode tips:
To make your red-green-blue cycle smoother, have your test running under a key shortcut:
- setup python test runner in VS code to pytest
- setup a key shortcut for running all python tests

###Cool pytest features we managed to use:
- @pytest.mark.parametrize - to enable clean data driven approach
- @pytest.fixture - to abstract away details of test setup and ... teardown tbd...




### TDD TODO list:
- measuring complexity by code lines - improve coverage:
  - empty lines inside file
  - empty lines before and after non-empty lines
  - only white characters in file
- measuring complexity by indents - improve coverage:
  - only indents in line - should be counted?
  - indent characters somewhere else than line beginning
- are only tabs considered indents? what about 2*space and 4*space?
- cleanup - it's high time to split into multiple files and create modules
  - how to tdd with this?
- read from file system
- output a real report in a text format