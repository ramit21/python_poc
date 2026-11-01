# Unit testing


## Steps to install pytest
```
python3.10 -m venv .venv
source .venv/bin/activate
python3.10 -m pip install --upgrade pip
pip install pytest
pytest --version
pip install pytest-mock
pip install requests
```

## Running the tests
cd into pytest folder and run the test cases by simply running 
```

python3 -m pytest 
or
python3 -m pytest --log-cli-level=INFO  #to show loggers as well
or 
python3 -m pytest test_<file> to run a specific test case.
```
don't cd into test folder, you can run pytest on main code root folder.

