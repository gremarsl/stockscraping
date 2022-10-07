# Fundamental Stock Analysis - An approach
## Motivation
I am kind of interested in programming and economics. Both combined, has led me to write irregularly but every now and then on this little Python script.

## User Manual
Unfortunately, using the program with the current version is not very user-friendly.
Therefore, I will try to answer all the important points in this section.

### Prerequisites
Python Interpreter: v3.10 is installed and functioning on the computer.
The Python packages are installed and ready for usage.The necessary packages are included in requirements.txt and can be installed quickly and easily with the following command:  
`pip install -r requirements.txt`


### Preparations for use
Preparations are required so that the program can be used successfully and companies can be analyzed for key figures. 
These are described in this section. 

#### What approaches are available to me?
1. Using the yahoo stock API.
2. Creating your own format, with individually / customized data. Current format: JSON.

#### Where does the data for a company analysis come from ?
For an in-depth look at financial metrics, two data sources are available: 
1. Yahoo finance (https://pypi.org/project/yfinance/)
2. Use of a standalone data filled file (currently json format).

### Usage
Before the program execution an individual adjustment of the parameters and the companies can be made. 
For these adjustments the file `global_vars.py` is available.
This again is subdivided into different sections. A section always starts with `# START <section name>` and ends with `# END <section name>`.

To analyze a company, enter the stock symbol under which the company is listed on the stock exchange. 
The list of companies can be extended at will. The limiting factor is at some point the computing capacity of your own PC.

### The first Execution
After you have downloaded and installed the necessary packages for a successful execution of the script, nothing stands in the way of a first program execution. 
After a few seconds, graphs should be displayed one after the other, showing you a comparison between Apple and Microsoft. 
If you want to continue to the next graph, press X to close the current graphic.

### Hints
* The file `companies.txt` contains some symbols of other companies.

## Possible Improvements
- Simplified extension of additional indicators. The extension of additional indicators is currently time-consuming, since the extension must be made in several places within the implementation.
- Error Handling.
- future usage as module? Execution via CLI?

## Contribution
If you like and use this program, feel free to donate here: 
[Donate this program](https://www.paypal.com/donate/?hosted_button_id=FR84QT6MVPKFS)


## Licence
Standard Github license. Feel free to view and fork this project for personal use.

## Get in contact 

Github - [gremarsl](https://github.com/gremarsl)\
E-Mail:  [startwitharduino@gmail.com ](startwitharduino@gmail.com)
