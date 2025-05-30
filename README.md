# Automated Tests E-Commerce Site
## Description
Automated tests using Python & PyTest for an ecommerce site. The site under test is created using WordPress, Woocommerce and the StoreFront theme. Example site for testing: http://demostore.supersqa.com/

## Steps for setting up the framework and running tests
## Clone the repository
```commandline
git clone https://gitlab.com/test_14382025/ecommerce-site-pytest-automation.git
```

## Navigate to the cloned directory
```commandline
cd ecommerce-site-pytest-automation
```

## Create virtual environment and install requirements
## Create a virtual environment
```commandline
python3 -m venv ssqatest_venv
```

## Activate the virtual environment
#### On Mac/Linux
```commandline
$ source  ssqatest_venv/bin/activate
```

#### On 'Windows CMD'
```commandline
C:\..\Scripts\activate.bat
```
#### On 'Windows PowerShell'
```commandline
C:\..\Scripts\Activate.ps1
```


## Install dependencies in the virtual environment
```commandline
python3 -m pip install -r requirements.txt
```

## Set/Configure environment variables
There are variables required by the framework. Some of these value can be changed directly in the code instead of setting environment variables but setting the environment variables is the easiest option. To change values in the code change them here: 
eCommerce-Site-PyTest-Automation/ssqatest/src/configs/MainConfigs.py

The Easiest way to set the variables is to set them in a file and run/source the file.

#### For 'Mac/Linux' systems, update and run the 'variables_local.sh' file.
```commandline
source variables_local.sh
```


#### For 'Windows' using 'CMD' run the '' file.
```commandline
C:\..\variables_local.bat
```

#### Here are the variables that must be set (For Windows on CMD replace 'export' with 'set')
```commandline
export BASE_URL=<your website url> 
export BROWSER=<browser type>
export RESULTS_DIR=$(pwd)/results
export DB_PORT=<your database port>
export DB_HOST=<your database host>
export DB_DATABASE=<database/schema name>
export DB_TABLE_PREFIX=<tables prefix>
```


#### Credentials (these should not be kept in source control like GitHub)
```commandline
export WOO_KEY= <your woocommerce api key>
export WOO_SECRET=<your woocommerce api secret>
export DB_USER=<your database user>
export DB_PASSWORD=<your database password>
Example:

export BASE_URL=http://localhost:8888/localdemostore/ 
export BROWSER=chrome 
export RESULTS_DIR=$(pwd)/results 
export DB_PORT=8889 
export DB_HOST=localhost 
export DB_DATABASE=localdemostore 
export DB_TABLE_PREFIX=wp_ 
```

#### Credentials (These should not be kept in source control like GitHub)
```commandline
export WOO_KEY= ck_1234 
export WOO_SECRET= cs_1234
```

#### Credentials for the wordpress/mysql database
```commandline
export DB_USER= <username>
export DB_PASSWORD= <password>
```


## Run tests
### To run all tests
** Make sure virtual environment is active ** <br>
** Explore the 'runner.sh' (For Mac/Linux) and consider using it.

```commandline
cd ssqatest
python3 -m pytest tests
```

### To run frontend tests
```commandline
cd ssqatest
python3 -m pytest tests/frontend
```

### To run backend tests
```commandline
cd ssqatest
python3 -m pytest tests/backend
```

### To run specific test by id/markers
```commandline
cd ssqatest
python3 -m pytest tests -m fe001_checkout
```

## Reports
Use Allure report
1. To run the whole test suite
```commandline
pytest --alluredir = allure_results
allure serve allure_results
```
c

2. To run a specific test
```commandline
pytest -k "test_verify_mainpage_labels.py" --alluredir = allure_results
```
3. Ensure the tests have the necessary details.

![Details in each test](images/passed_test_details.jpg)


4. Ensure that the failing tests have the defect ticket mentioned. 

![Defect ticket number](images/failed_defect.jpg)

## Test Automation Process 
![Test Automation Process](images/automation_process.jpg)

