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

    ```bash
    $ python3 -m venv env
    ```

2. Launch your virtual environment  

    A. **In VSCode**  
    Run Terminal: Create New Integrated Terminal (⌃⇧`)) from the Command Palette, which creates a terminal and automatically activates the virtual environment by running its activation script.  

    or B. **run in command line**

    ```bash
    $ source env/bin/activate
    ```

3. Install Packages (from a prepackaged list of programs)

    ```bash
    $ pip install -r requirements.txt
    ```

<br />  

## Juypter Notebook

You will be able to start creating Juypter Notebook in VSCode environment, as long as you create new file with extension **.ipynb**.

<br />

## Running Main Dash App

1. To run the Main App, run the following line.

    ```bash
    $ python index.py
    ```

<br />  

## Running Dash App for indivdual lab

1. To run dash app for each lab, run the following line.

    ```bash
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

    ```bash
    $ docker-compose up --build
    ```

## Start using git and GitHub

To get started with our repo

```bash
$ git config — global user.name “your_handle”
$ git config — global user.email “your@email.com”
$ git clone https://github.com/todatech/csda-lab.git
```

<br />  

## Notes For Reference

### Conda

To install packages (i.e. nltk, scikit, etc) in your anaconda environment  

```bash
$ conda activate base  
$ conda install -c anaconda nltk  
$ conda install -c conda-forge scikit-surprise  
# install whatever packages needed.
```

<br />  

## References

### Learn GIT with Bitbucket Cloud

[Learn Git with Bitbucket Cloud - Atlassian Bitbucket](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud)

<br />  

### Visual Studio Code

[Data Science in Visual Studio Code](https://code.visualstudio.com/docs/python/data-science-tutorial)

[Flask Tutorial in VSCode](https://code.visualstudio.com/docs/python/tutorial-flask)

### Flask and Container

[Python in a container (Including Flask and Django)](https://code.visualstudio.com/docs/containers/quickstart-python)

[The best Docker base image for your Python application (April 2020) by Itamar Turner-Trauring](https://pythonspeed.com/articles/base-image-python-docker-images/)

### Dash

[Dash for Beginners](https://www.datacamp.com/community/tutorials/learn-build-dash-python)

[How to Build a Reporting Dashboard using Dash and Plotly - Towards Data Science](https://towardsdatascience.com/how-to-build-a-complex-reporting-dashboard-using-dash-and-plotl-4f4257c18a7f)

[Deploying Dash App - plotly|Dash](https://dash.plotly.com/deployment)

[Create a Multipage Dash Application](https://towardsdatascience.com/create-a-multipage-dash-application-eceac464de91)

[How to Build a Reporting Dashboard using Dash and Plotly](https://towardsdatascience.com/how-to-build-a-complex-reporting-dashboard-using-dash-and-plotl-4f4257c18a7f)

### Cloud Deployment

[Deploy your Dash application with Google Cloud Platform App Engine](https://datasciencecampus.github.io/deploy-dash-with-gcp/)

[How To Serve Flask Applications with Gunicorn and Nginx on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04)

### Recommender Systems Library in Python

[Welcome to Surprise' documentation](https://surprise.readthedocs.io/en/stable/)

### Building a Recommender System

[How to build a Simple Recommender System in Python](https://towardsdatascience.com/how-to-build-a-simple-recommender-system-in-python-375093c3fb7d)

[Recommendation Systems : User-based Collaborative Filtering using N Nearest Neighbors](https://medium.com/sfu-cspmp/recommendation-systems-user-based-collaborative-filtering-using-n-nearest-neighbors-bf7361dc24e0)

[Quick Guide to Build a Recommendation Engine in Python & R](https://www.analyticsvidhya.com/blog/2016/06/quick-guide-build-recommendation-engine-python/)

[Recommender Systems with Python— Part II: Collaborative Filtering (K-Nearest Neighbors Algorithm)](https://heartbeat.fritz.ai/recommender-systems-with-python-part-ii-collaborative-filtering-k-nearest-neighbors-algorithm-c8dcd5fd89b2)
