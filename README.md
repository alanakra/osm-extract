# MATRIMOINE PROJECT - EXTRACTING DATA FROM OPENSTREETMAP (VIA GEODATAMINE)

This repository contains a script designed to extract named places from OpenStreetMap (OSM) using data provided by [GeoDataMine](https://geodatamine.fr/) , and convert them into a Python dictionary of tuples. Each tuple contains key information such as the name of the place, its INSEE code, and the commune name.

## **Overview**

The script reads input data from a CSV file containing geographic information and transforms it into a set of unique tuples. The output is written into a Python file for further use in other parts of the project.

### **Example Input and Output**

#### **CSV Input Format:**

A CSV file used as input should have the following format, with semicolons (`;`) used as delimiters between fields:

``` csv
    2.7439253;48.4342121998324;node/2890030601;sports_centre;ANFA - Aviron du Pays de Fontainebleau;;rowing;;;"77441";Samois-sur-Seine
```

The relevant fields that the script will process are:
    - Name: The name of the place.
    - INSEE Code: The unique code for the commune.
    - Commune Name: The name of the commune.

#### **Python Output Format:**
The output is a Python file that contains a set of tuples, where each tuple represents a labeled place:

``` python
    {
        ('ANFA - Aviron du Pays de Fontainebleau', 77441, 'Samois-sur-Seine')
    }
```

## **Script Structure**

### **Dependencies:**

-   `os` for managing file directories.
-   `pandas` for reading and processing CSV files.
-   `pprint` for formatting the Python output.
-   `datetime` for timestamping the generated Python file.

### **Workflow:**

1.  **Install dependencies:**
    -   Install all dependencies with: pip install -r requirements.txt.
2.  **File and Directory Setup:**
    -   Create a `datas` directory at the root of the project where you store your CSV files. I strongly recommend using `data-placeType-region`, such as `data-school-normandie`.
    -   If the `extracts` directory does not exist, the script will create it.
    -   The user is prompted to enter the file name (without the `.csv` extension) to read from. 
3.  **CSV Reading and Data Processing:**
    -   The script reads specific columns (`name`, `com_insee`, `com_nom`) from the CSV file located in the `datas` directory.
    -   It processes each row to extract and clean the relevant fields (place name, INSEE code, and commune name).
4.  **Set of Tuples Creation:**
    -   A set of unique tuples is generated, ensuring that places are not duplicated.
    -   Each tuple consists of:
        -   The place name.
        -   The INSEE code.
        -   The commune name.
5.  **File Output:**
    -   The resulting set of tuples is saved in a new Python file within the `extracts` directory.
    -   The file is named based on the input file and includes a timestamp in its header.
6.  **Logging:**
    -   The script prints the total number of labeled places found and confirms the creation of the output file.
