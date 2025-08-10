
# CSV Bulanan Modifier

**CSV Bulanan Modifier** is an application designed to modify CSV files for use in the financial accounting system **SAKTI**, specifically for **SPP Type 237 - LS Multiple Recipients**. without Using CSV Generator. Fast And Simple
## Features
1. Separates employee bank accounts by bank (e.g., Mandiri and BSI)
2. Bulk edit of transfer amounts for recipient accounts in a CSV file
3. Auto-Increment Numbering in CSV File (No Shuffle Number)
## Technologies And Requirements
1. Python
2. Microsoft Visual Studio Code
3. [PyQt6](https://pypi.org/project/PyQt6)
4. [Auto-Py-To-Exe](https://pypi.org/project/auto-py-to-exe)
5. see requirements.txt
## Installation
If you're using "Windows" and want to use the application directly, please go directly to the [Release Page](https://github.com/whoishusni/csv_bulanan_modifier/releases). However, if you'd prefer to run the application using Visual Studio Code, follow the steps below.
1. open terimal / cmd,  and clone the project `git clone https://github.com/whoishusni/csv_bulanan_modifier.git`
2. Create Virtual Environment for Python (optional) `python3 -m venv .venv` (.venv is the name of virtual environment)
3. Install all Dependecy or Library in txt file
`pip3 install -r requirements.txt`
4. You're all set!
## Usage
- For Windows, Just Download and Run The exe file, see [Release Page](https://github.com/whoishusni/csv_bulanan_modifier/releases).
- For Linux and Mac run the app using visual studio code, or run direcly from terminal `python3 main.py`
## Screenshoot
![No Image Yet](#)
## Release
Download the latest release of the application [Here](https://github.com/whoishusni/csv_bulanan_modifier/releases)
## Important Notes
Ensure your CSV file uses the following header format:
`NO|NAMA_SUPPLIER|NAMA_PEMILIK_REKENING|NO_REKENING|JUMLAH_UANG`

so this is example your full csv file, look like this:

    NO|NAMA_SUPPLIER|NAMA_PEMILIK_REKENING|NO_REKENING|JUMLAH_UANG
    1|PT.MENCARI CINTA SEJATI|NAME ONE|199120022023|5200000
    2|PT.MENCARI CINTA SEJATI|NAME TWO|199120022023|4500000
