# scraping-flipkart-s-iphone

This project focuses on Web Scraping and Data Cleaning. The website chosen for this project was flipkart, more specifically the category of mobile phone. The purpose was to use the library BeautifulSoup to extract the information required, clean the data and export it to a MySQL table. Each stage was condensed in a function that was later included in a pipeline to make the code easier to read and to run.

#Tools and Libraries used
Requests
BeautifulSoup
Pandas
datetime

#Process
The project is divided into 3 main stages:

Extraction/Scraping of the data from the website;
Data Cleaning
Exporting the data to MySQL

#Data Cleaning
Several steps had to be performed to clean the data because we are dealing with text that is usually written in different ways for each product and, in some cases, it might be have been scraped properly for every single product.

Such steps involved **standardizing the text, replacing empty values with a standard value, changing the data types of the columns and splitting columns for each product feature.
![scrap](https://user-images.githubusercontent.com/90494573/150670388-c1c99583-541a-42a4-a8f3-21ca6817c1f8.png)
#Exporting the data
The final stage involves creating a connection the MySQL database and exporting the dataframe to the designated table. The final result is the one shown below.
![scrapping2](https://user-images.githubusercontent.com/90494573/150670449-0179984c-a439-404b-93d5-0ceafe4f3dcc.png)

Each one of these three stages is a function and all three are included in a pipeline so that all functions can be run in sequence. 
