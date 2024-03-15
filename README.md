# Roman to Arabic Number Converter

This is a web application built using the Flask microframework that allows users to convert roman numerals to arabic numerals and vice versa.  
This easy-to-use application features a front end made using the [MD Bootstrap](https://mdbootstrap.com/) library.  

A live version of the application is currently hosted on Render [here](https://illumina-take-home-assessment.onrender.com/) 
(do note the load time - the application spins down with inactivity and may require additional time to be accessible).

## Installation

As this web application is a Flask project, do ensure that you have the following installed on your machine before forking the Git repository:

1.  Python >= 3.9.13
1.  Flask >= 2.2.3
1.  Werkzeug 2.2.3

You may install Python on its [official website](https://www.python.org/); you can also install Flask and Werkzeug via the `pip` package manager
like so by calling `pip install flask` and `pip install werkzeug`.

To begin a development instance of the web application, navigate to the project's root directory input the command `flask --debug run` into the console.

## Usage

The web application offers a simple, intuitive user interface that allows users to convert between roman numerals to arabic numerals and vice versa 
with minimal guidance.  To convert a roman or arabic numeral to its respective arabic or roman equivalent, simply enter an arabic numeral or a roman
numeral (lower-cased, upper-cased, and mixed-case) into the appropriate the form and click on the "Convert!" button below the respective form.  The
web application should display the corresponding conversion after.

For cases whereby an invalid input (i.e., invalid character) has been entered, a "???" will be displayed as a result instead.