
==========================
Copernicus Climate test
==========================

Selenium based automated testing.

Usage
-----------
This package requires **Python 3.5**!
::

    $ virtualenv copenv
    $ source copenv/bin/activate
    $ pip3 install selenium
    $ download the browser webdrivers for Firefox (geckodriver) and Chrome (chromedriver) 
    $ The given browser webdriver must be in your $PATH\n
    $ or given via the --browserpath option.
    $ help: python3 climateTestSuite.py -H
    $ for instance, it can be run on Firefox, 800x600 resolution, verbosity 2 as follows:
    $ python3 climateTestSuite.py -V -sw 800 -sh 600 -B firefox
    
