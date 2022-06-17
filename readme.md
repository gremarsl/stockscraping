# Fundamental Stock Analysis - An approach

## Motivation
I am kind of interested in programming and economics. Both combined, has led me to write irregularly but every now and then on this little Python script.

## User Manual
Unfortunately, using the program with the current version is not very user-friendly.
Therefore, I will try to answer all the important points in this section.

### Prerequisites
Python Interpreter: v3.10 is installed and functioning on the computer.
The Python packages are installed and ready for usage.

### Preparations for use
Preparations are required so that the program can be used successfully and companies can be analyzed for key figures. 
These are described in this section. 

[TLDR]: In order to use the finnhub and alpha vantage stock api you need keys. You can find out how to get a key on the web page I referenced above.
In `keys.py` you have to enter the keys. `api_key` for using the finnhub api and `api_key_alpha` for alpha vantage.

#### What approaches are available to me?
For a better understanding, here a few words about the selectable approaches of the user. 
1. Using a stock API in order to analyze the enterprise data afterwards.
2. Creating your own format, with individually / customized data to be evaluated afterwards. Current format: JSON.

#### Where does the data for a company analysis come from ?
For an in-depth look at financial metrics, four data sources are available: 
1. finnhub stock API (https://finnhub.io/)
2. alpha vantage stock API (https://www.alphavantage.co/)
3. yahoo finance (https://pypi.org/project/yfinance/)
4. use of a standalone data filled file (currently json format).


### Usage
The program execution an individual adjustment of the parameters and the companies can be made. 
For these adjustments the file `global_vars.py` is available.
This again is subdivided into different sections. A section always starts with `# START <section name>` and ends with `# END <section name>`.

To analyze a company, enter the stock symbol under which the company is listed on the stock exchange. 
The list of companies can be extended at will. The limiting factor is at some point the computing capacity of your own PC.

### Hints
* When the program goes to sleep for 60 seconds, don´t cancel execution. The program will continue


## Possible Improvements
- Simplified extension of additional indicators. The extension of additional indicators is currently time-consuming, since the extension must be made in several places within the implementation.
- Error Handling.
- Python package and dependency management.
- Possible modularization in 3 tools. Each API own handling

## Contribution
Thanks for your feedback, help and improving this program.

## Licence
Standard Github license. Feel free to view and fork this project for personal use.

## Get in contact 
Github - [gremarsl](https://github.com/gremarsl)\
E-Mail:  [startwitharduino@gmail.com ](startwitharduino@gmail.com)