# CSDA Labs 

This README.md provides instructions to setup your enivornment so you can start writing code for the lab assignments. Refer to [this link](instruction.md) for instructions on the Lab. 

<br />

## Prerequisites
- Visual Studio Code
- Anaconda
- Python extension for VS Code

Refer to [this tutorial - data science on VSCode](https://code.visualstudio.com/docs/python/data-science-tutorial) to set up your environment and test out ipython (Jupyter Notebook).

<br />

## Setup Virtual Environment and Install Python packages
1. Create Your Virtual Environment  
    ```
    $ python3 -m venv env
    ```

2. Launch your virtual environment  

    A. **In VSCode**  
    Run Terminal: Create New Integrated Terminal (⌃⇧`)) from the Command Palette, which creates a terminal and automatically activates the virtual environment by running its activation script.  

    or B. **run in command line**
    ```
    $ source env/bin/activate
    ```

3. Install Packages (from a prepackaged list of programs)
    ```
    $ pip install -r requirements.txt
    ```

<br />

## Juypter Notebook
You will be able to start creating Juypter Notebook in VSCode environment, as long as you create new file with extension **.ipynb**. 

<br />

## Running Main Dash App
1. To run the Main App, run the following line.
    ```
    $ python app.py
    ```

<br />

## Running Dash App for indivdual lab  
1. To run dash app for each lab, run the following line.   
    ```
    # lab 1
    $ python lab1app.py  
    # lab 2
    $ python lab2app.py  
    # lab 3
    $ python lab3app.py  
    ```
2. Open browser in your local machine and navigate http://localhost:8050 

<br />

## Running Dockerize Dash App via Docker Compose 

- (Note: only root app app.py will be able to run from docker.)  

- Make sure you have installed docker and docker-compose in your target system.
    ```
    $ docker-compose up --build
    ```

<br />

## Notes For Reference  
### Conda  
To install packages (i.e. nltk, scikit, etc) in your anaconda environment  
```
$ conda activate base  
$ conda install -c anaconda nltk  
$ conda install -c conda-forge scikit-surprise  
# install whatever packages needed.
```

<br />

# References

## Learn GIT with Bitbucket Cloud
[Learn Git with Bitbucket Cloud - Atlassian Bitbucket](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud)

<br />

## Visual Studio Code

Data Science in Visual Studio Code
https://code.visualstudio.com/docs/python/data-science-tutorial

Flask Tutorial in VSCode
https://code.visualstudio.com/docs/python/tutorial-flask

<br />

## Flask and Container

Python in a container (Including Flask and Django)
https://code.visualstudio.com/docs/containers/quickstart-python

<br />

## Dash

Dash for Beginners
https://www.datacamp.com/community/tutorials/learn-build-dash-python

How to Build a Reporting Dashboard using Dash and Plotly - Towards Data Science
https://towardsdatascience.com/how-to-build-a-complex-reporting-dashboard-using-dash-and-plotl-4f4257c18a7f

Deploying Dash App - plotly|Dash
https://dash.plotly.com/deployment

Create a Multipage Dash Application
https://towardsdatascience.com/create-a-multipage-dash-application-eceac464de91

How to Build a Reporting Dashboard using Dash and Plotly
https://towardsdatascience.com/how-to-build-a-complex-reporting-dashboard-using-dash-and-plotl-4f4257c18a7f