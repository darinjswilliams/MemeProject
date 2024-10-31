# Meme Generator Project
A fun new way to make your own memes! The app lets you combine images with perfectly timed quotes to generate unique memes. Simply click on random button to generate meme, or choose create button to grab image from web. A quote, is over - layed on top of the image and watch as the app instantly combines them.  
The project consist of generating memes with quotes from the command line or web interface.  

# Installation
A Python virtual environment is established to accommodate the specific version(s) of the Python interpreter installed on your system
<ol>
    <li>git clone https://github.com/darinjswilliams/MemeProject.git</li>
    <li>cd MemeProject</li>
    <li>python -m venv .venv</li>
    <li>source .venv/bin/activate</li>
    <li>pip install -r requiremets.txt</li>
</ol>

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
<li>python meme.py --path="path to image", --body='some text' --author='Author Name'</li>
<li>python meme.py  - Executed with no parameters</li>
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

### Directory Structure  
src  
├── CustomException  
│   ├── InvalidTextException.py  
│   ├── MemeException.py  
│   ├── ModelException.py  
│   ├── NoDirectoryException.py  
│   ├── ParseImportException.py  
│   ├── RequireParamException.py  
├── MemeGenerator  
│   ├── MemeEngine.py  
├── QuoteEngine  
│   ├── CSVIngestor.py  
│   ├── DocxIngestor.py  
│   ├── Ingestor.py  
│   ├── IngestorInterface.py  
│   ├── PDFIngestor.py  
│   ├── QuoteModel.py  
│   ├── TextIngestor.py  
├── Utils  
│   └── util_funs.py  
├── app.py  
├── meme.py    








