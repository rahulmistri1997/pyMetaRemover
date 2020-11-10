@echo off

echo Upgrading pip
python -m pip install --upgrade pip

echo Installing virtual-environment
pip install --upgrade virtualenv

echo Creating a virutal environment
virtualenv venv

REM Activating the virtual environment.
cd venv\
cd Scripts\
activate

echo Installing the required packages

cmd
pip install -r requirements.txt

echo Setup executed successfully.

echo Activate the virtual-environment using 
echo    `venv\Scripts\activate`