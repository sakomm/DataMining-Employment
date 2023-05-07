# DataMining Final Project 

## Project Motivation and Background

As Computer Science students about to enter the job market, we're concerned about the volatility of the tech industry. We want to analyze and create a system that can help people understand the markets, plan an exit strategy, and alleviate these concerns.

## Project Goal:

The goal of our project is to analyze trends in companies' recent layoffs in a variety of industries (aerospace, travel, retail, etc.) and detect patterns and trends. This will be done by looking at the number of employees laid off, the location of the companies, their stages, and the funds they have raised.

## Data Sources:

layoffs.fyi - https://layoffs.fyi/

US Bureau of Labor Statistics - https://www.bls.gov/ This was supposed to be a source of data for unemployment rates, but we were unable to find a 
dataset that was a proper fit for our project.

### How to run the project:

1. Clone the repository
2. Run `pip install -r requirements.txt` to install the required packages

There are three main files in the project: 

FinalProject.ipynb - This is the main file that contains all of the code for the project. It contains the code for the data collection, cleaning, and analysis. This file does analysis by Ridge Regression 

FinalProject-SVR.ipynb - This file contains the code for the Support Vector Regression analysis.

FinalProject-NN.ipynb - This file contains the code for the Neural Network analysis.

if you would like to make some novel predictions run the ./site.py file and go to the localhost:5000 in your browser.
-------------------------
