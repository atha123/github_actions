# Automated Tests E-Commerce Site
## Description
Automated tests using Python & PyTest for an ecommerce site. The site under test is created using WordPress, Woocommerce and the StoreFront theme. Example site for testing: http://demostore.supersqa.com/

## Steps for setting up the framework and running tests
## Clone the code
git clone https://gitlab.com/test_14382025/demostore_frontend_backend_tests
## Navigate to the cloned directory

cd demostore_frontend_backend_tests

## Create virtual environment and install requirements
## Create a virtual environment

python3 -m venv ssqatest_venv
## Activate the virtual environment
### On Mac/Linux
$ source  ssqatest_venv/bin/activate

### On 'Windows CMD'
C:\..\Scripts\activate.bat

### On 'Windows PowerShell'
C:\..\Scripts\Activate.ps1

## Install requirements in the virtual environment
python3 -m pip install -r requirements.txt
## Set environment variables
There are variables required by the framework. Some of these value can be changed directly in the code instead of setting environment variables but setting the environment variables is the easiest option. To change values in the code change them here: 
eCommerce-Site-PyTest-Automation/ssqatest/src/configs/MainConfigs.py

The Easiest way to set the variables is to set them in a file and run/source the file.

### For 'Mac/Linux' systems, update and run the 'variables_local.sh' file.

source variables_local.sh

### For 'Windows' using 'CMD' run the '' file.

C:\..\variables_local.bat
### Here are the variables that must be set (For Windows on CMD replace 'export' with 'set')

export BASE_URL=<your website url> <br>
export BROWSER=<browser type><br>
export RESULTS_DIR=$(pwd)/results<br>
export DB_PORT=<your database port><br>
export DB_HOST=<your database host><br>
export DB_DATABASE=<database/schema name><br>
export DB_TABLE_PREFIX=<tables prefix>

## Credentials (these should not be kept in source control like GitHub)
export WOO_KEY= <your woocommerce api key><br>
export WOO_SECRET=<your woocommerce api secret><br>
export DB_USER=<your database user><br>
export DB_PASSWORD=<your database password><br>
Example:

export BASE_URL=http://localhost:8888/localdemostore/ <br>
export BROWSER=chrome <br>
export RESULTS_DIR=$(pwd)/results <br>
export DB_PORT=8889 <br>
export DB_HOST=localhost <br>
export DB_DATABASE=localdemostore <br>
export DB_TABLE_PREFIX=wp_ <br>
## Credentials (These should not be kept in source control like GitHub)
export WOO_KEY= ck_1234 <br>
export WOO_SECRET= cs_1234
## Credentials for the wordpress/mysql database
export DB_USER=root <br>
export DB_PASSWORD=root

## Run tests
### To run all tests
** Make sure virtual environment is active ** <br>
** Explore the 'runner.sh' (For Mac/Linux) and consider using it.

cd ssqatest
python3 -m pytest tests
### To run frontend tests
cd ssqatest
python3 -m pytest tests/frontend
### To run backend tests
cd ssqatest
python3 -m pytest tests/backend
### To run specific test by id
cd ssqatest
python3 -m pytest tests -m fe_home_001

## Test Automation Process 
![Automation Framework](images/automation_process.png)
