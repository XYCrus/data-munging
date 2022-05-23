# Raw Data Munging

## Overview
In this repository, I will make usable a real data source: **NASA's historic measurements of the Earth's surface temperatures**. In particular, I will:
1. Write a Python program to clean up/munge the data and save it into a standard Comma-Separated Values (CSV) format text file.
1. Write a second Python program to do some analysis of the data in the CSV file.

### Part 1: Download the data
NASA's [GISS Surface Temperature Analysis web site](https://data.giss.nasa.gov/gistemp/) gives an overview of the data set - they publish recordings in the change of the Earth's surface temperature going back to the year 1880.  
- The numbers do not represent actual temperature readings, but rather represent temperature *anomalies*.
- Their [FAQ page](https://data.giss.nasa.gov/gistemp/faq/#q101) includes some additional explanations.

I download [the raw data in fixed-width column format](https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.txt) and save the raw data file into the directory named `data` in this repository.

### Part 2: Munge it
The raw data has some some features that make it difficult to analyze with a program. 

I write a Python program in the file named `munge.py` to clean up the raw data and save it into a CSV-formatted file named `clean_data.csv` within the `data` directory of this repository.

Issues that my program address:
- there are many lines at the top and bottom of the file that contain notes and not the raw data - **all lines with notes are removed**.
- the column headings are repeated on multiple lines throughout the file - **remove all but the first line of column headings**.
- there are some blank lines in the middle of the data - **remove all blank lines**.
- there is missing data indicated with `***` - **missing data handling**.
- the temperature anomalies in this data are given in 0.01 degrees Celsius.  **Convert temperature anomalies to Farenheit**
- since this data is in *fixed-width column format*, there are inconsistent numbers of spaces separating the numeric values... **standardize specific numbers of spaces are used as separators**.

The way I do the cleanup and transofrmation is repeatable. A new file, `clean_data.csv`, is created under data that solve all the issues above.

### Part 3: Analyzation
Now that I have the data in easy to parse CSV format, I will perform some aggregate statistics on the data.

I write a Python program in the file named `analyze.py` that does the following:
- opens up yotheur cleaned up data file, `clean_data.csv` and imports it using Python's `csv` module.
- outputs the average temperature anomaly in degrees Farenheit for each decade since 1880 with format:
    - 1880 to 1889
    - 1890 to 1899
    - 1900 to 1909
    - ...and so on.
