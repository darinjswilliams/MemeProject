# Meme Generator Project
A fun new way to make your own memes! The app lets you combine images with perfectly timed quotes to generate unique memes. Simply click on random button to generate meme, or choose create button to grab image from web. A quote, is over - layed on top of the image and watch as the app instantly combines them.  
The project consist of generating memes with quotes from the command line or web interface.  

# Installation
A Python virtual environment is established to accommodate the specific version(s) of the Python interpreter installed on your system. 
After step 5 a virtual environment is activated and than you can create a meme from executing main or app.
<ol>
    <li>git clone https://github.com/darinjswilliams/MemeProject.git</li>
    <li>Install pdf reader to your machine</li>  
        <ol>
            <li>Mac: brew install xpdf in the terminal.</li>
            <li>Windows: Download the Windows command-line tools from the xpdf website</li>
        </ol>  
    <li>cd MemeProject</li>
    <li>python -m venv .venv</li>
    <li>source .venv/bin/activate</li>
    <li>pip install -r requiremets.txt</li>
</>

***Notes***  This project runs best on python versions 3.10 and above due to updated python libraries defined in requirements.txt

# Usage

## Run Command Line interface - meme
Command Line interface (cli) accepts optional parameters consisting of:  
<ul>
    <li>path - a path to image</li>
    <li>body - some quote that you like or dont like</li>
    <li>author - name of author</li>
</ul>

There are various ways to execute the command line interface with the optional parameters which can be pass in any order
<ol>
<li>python main.py --path="path to image", --body='some text' --author='Author Name'</li>
<li>python main.py  - Executed with no parameters</li>
</ol>

The CLI will throw a ***RequireParamException(f'Author Required if Body is Present')*** if you attempt to execute  
by passing in only body parameter,  

## Run Web interface - app
The web interface starts a Flask server and displays a Random Image stored with the application and a ***Random Button*** and ***Create Button*** after you click on the default address that is displayed  
Currently the default address is http://127.0.0.1:5000  


# Exceptions

The application consist of the following custom exceptions  
* RequireParamException - Throw when Body param passed in with no Aurthor
* MemException - Throw when there is an exception on creating a Meme Object
* ModelException - Throw when there is an exception instantiating a Model
* NoDirectoryException - Throw when a file is created and the system does not find the file or Directory


# Testing

Pytest framework is use to do unit testing on all the code base.  To keep things simple and clean all test are keep to minimal complexity.  
You can execute an individual test or run test on the entire testing module by executing pytest or running individual test.

* Execute individual test pytest test_app.py::test_app_setup_return_image_count
* Execute all test in modules - pytest 

Testing Directory Structure  
***tests***  
├── test_CSVIngestor.py  
├── test_DocxIngestor.py  
├── test_Ingestor.py  
├── test_MemeEngine.py  
├── test_PDFIngestor.py  
├── test_TextIngestor.py  
├── test_app.py  
├── test_app_client.py  
├── test_meme.py  
├── test_quoteModel.py  


#### Testing requires changing some to the import statements on the meme and app files  
Meme File changes add period in-front of package as indicated below. if not you will get an import error 

<ol>
    <li>from .MemeGenerator import MemeEngine</li>
    <li>from .QuoteEngine import QuoteModel, Ingestor</li>
    <li>from .CustomException import (RequireParamException, NoDirectoryException)</li>
    <li>from .Utils import create_tmp_dirs</li>
</ol>

# Roles and Responsibility  with Directory Structure

***Custom Exception Module*** - The custom exception module contains custom exceptions.  The Custom Exception Classes are used in try except block and use to raise an exception to verify test located in testing module.  

***Python Dependencies:***  No Python Library Dependencies.  
***Inheritance:*** Exception Class  
***Usage:*** Wrapp Code in Try Except Block

src  
├── CustomException  
│   ├── InvalidTextException.py  
│   ├── MemeException.py  
│   ├── ModelException.py  
│   ├── NoDirectoryException.py  
│   ├── ParseImportException.py  
│   ├── RequireParamException.py  

***MemeGenerator Module***  
The Meme Engine Module is responsible for manipulating and drawing text onto images. All meme images are saved to a tmp directory.  
The image is saved as a png file with a random sequence of number as the name.  

***Python Dependencies:***  Pillow, numpy, os,random  
***Inheritance:*** No Inheritance    
***Optional Arguments:***  image path, body, author  
***Usage:*** call ***make_meme method*** with or without arguments  
***Returns:*** name of image with path location

src  
├── MemeGenerator  
│   ├── MemeEngine.py  


***QuoteEngine Module***  
The QuoteEngine Module is responsible for ingesting parsing many file types that contain quotes. The module is based on the Strategy Object Design Pattern. All child classes inherit from parent class ***IngestorInterface***. The individual ingestor classes  call the parent class can_ingest method to determine if a file is valid.  The module includes an Ingestor class which determines what child ingestor class is called during runtime.

***Python Dependencies:***  pandas, subprocess, typing, random, os, docx    
***Inheritance:*** IngestorInterface(ABC) - Abstract Base Class    
***Arguments:***  file path  
***Usage:*** call ***parse method***  
***Returns:*** Quote Model with Text and Author  
***Roles:*** The Ingestor class roll is to call the child ingestor classes determined by the file type being processed at runtime.    
***Current File Types for Parsing:*** CSV, TXT, PDF, DOCX  
  

src  
├── QuoteEngine  
│   ├── CSVIngestor.py   
│   ├── DocxIngestor.py  
│   ├── Ingestor.py  
│   ├── IngestorInterface.py  
│   ├── PDFIngestor.py  
│   ├── QuoteModel.py  
│   ├── TextIngestor.py  

***Utility Module*** 
The role and responsibility of util_funs is creating the /tmp and /static directories. 
src  
├── Utils  
│   └── util_funs.py  

***Main Module***  
The main module provides a command line interface that is called from main and web interfaced call from app.  
The main file accepts optional arguments that is passed to the MemeEngine class. The web interface starts a Flask Server on startup.  

***main interface*** - creates a meme with quote and save it to /tmp directory. accepts optional arguments.   
***app interface*** - provides web form to generate random memes from internal photos and a form to key in a url with author and text.  

***Python Dependencies:***  Flask, requests, os, random 
***Optional Arguments:***  image path, body, author  
***Usage:*** call ***make_meme method*** with or without arguments  
***Returns:*** name of image with path location

src  
├── app.py  
├── main.py   


***HTML FORMS***  
There are three html forms which provide interaction when the app interface is called.   The base.html form contains the styling and buttons.  
The meme_form allows the user to enter an url, body text and author.  The meme html is displayed on startup showing a random meme wih quote. The meme error is displayed if an invalid url is enter.  

src  
├── base.html  
├── meme_form.html  
├── meme.html  
├── meme_error.html  










