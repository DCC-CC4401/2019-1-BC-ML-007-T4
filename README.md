# CC4401-BC-ML007

A repo for the webpage group project of Universidad de Chile's CC4401 course: Software Engineering

## Instalation Requirements

* A local instalation of [git](https://git-scm.com/)
* A local instalation of [Python 3.7](https://www.python.org/)
* Python 3.7's [venv module](https://docs.python.org/3.7/library/venv.html)

## Instalation Instructions

### Getting the repository

Download the source code into a new `2019-1-BC-ML-007-T4` directory in `Linux` with the command:

~~~{bash}
git clone https://github.com/DCC-CC4401/2019-1-BC-ML-007-T4.git
~~~

### Installing Django

Installing a new `Python 3.7` virtual environment is highly recommended, you can do this using the command:

~~~{bash}
cd 2019-1-BC-ML-007-T4
python3 -m venv venv
~~~

Then activate the virtual environment with:

~~~{bash}
source venv/bin/activate
~~~

Finally, install all dependencies with:

~~~{bash}
pip install --upgrade pip
pip install django==2.2
~~~

## Running the Server

To run the server, run:

~~~{bash}
cd src
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
~~~

Then, simply access the `url` the server prints to the terminal in your browser of choice.

## Group Members

* [Miguel Huenchuleo](https://github.com/Miguel-SH)
* [Diego Ortego](https://github.com/Gedoix)
* [Luis Pinochet](https://github.com/shenkok)
* [Bryan Riveros](https://github.com/BryanRrs)
* [Valeria Valdés](https://github.com/valeriavaldes)
