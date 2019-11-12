# Stock Data Application

This application is a PyQt5 desktop application written as a project for my business partners and me. 

## Overview

The core of the application uses an underlying, propietary algorithm (not included in the repo) to look at specific stock data and calculate a predicted price on a certain date.
The application takes a search of stock symbol and first searches the internal database for a matching stock ticker. If the stock ticker is found the 
application will then scrape data from an online source utilizing Selenium and Beautiful Soup to gather the relevent data. Once the data is gathered,
the algorithm is implemented on the data and the result is imported into a table to preview. Once all stocks wanted are in the table, you can then export the table to an Excel table for further data processing.

## Application Features

The application utlizes multiple Python and PyQt5 implementations. 

Some of these features include:  
&nbsp;&nbsp;&nbsp;&nbsp;-> QThreads  
&nbsp;&nbsp;&nbsp;&nbsp;-> Context Menus  
&nbsp;&nbsp;&nbsp;&nbsp;-> SQLite Database with Python  
&nbsp;&nbsp;&nbsp;&nbsp;-> Web Scraping  

## Aplication Preview


