[![Wang lab logo](https://static.wixstatic.com/media/c544bf_0e3064b159ae42238c83dca23bc352e8~mv2.png/v1/crop/x_0,y_0,w_1918,h_2080/fill/w_91,h_100,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/lab_icon_3.png)](https://www.dianewanglab.com/)



[![Python version](https://img.shields.io/pypi/pyversions/pandas)](https://www.python.org/)
[![JupyterLab](https://img.shields.io/badge/Jupyter-lab-orange)](https://jupyter.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange)](https://jupyter.org/)
[![R](https://img.shields.io/badge/R-blue)](https://www.r-project.org/)
[![RStudio](https://img.shields.io/badge/RStudio-blue)](https://posit.co/download/rstudio-desktop/)

# Wang Lab Database Connection Options

This repository offers two options for connecting to the Wang Lab Database: using R or Python. Below are instructions for each option:

## Option 1: Connecting with R

### Using R_Wang-Lab_dbcon.Rmd

1. Open the `R_Wang-Lab_dbcon.Rmd` file in RStudio or any other R Markdown editor.
2. Replace the placeholder values for database credentials with your actual database credentials.
3. Run the R code chunks sequentially to establish the connection, list tables in the database, query data, and display the results.

## Option 2: Connecting with Python

### Using R_Wang-Lab_dbcon.ipynb

1. Make sure you have Jupyter Notebook installed.
2. Open the `R_Wang-Lab_dbcon.ipynb` notebook in Jupyter Notebook.
3. Replace the placeholder values for database credentials with your actual database credentials.
4. Place the `functions.py` file in the same directory as the notebook file.
5. Run the notebook cells sequentially to import libraries, establish the connection, query data, and display the results.

### Note

- For Python, ensure that the `functions.py` file is in the same directory as the Jupyter Notebook to access the custom functions for database operations.
- Both options provide flexibility in querying the database and analyzing the fetched data.