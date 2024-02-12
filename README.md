## Introduction
The above project involves building a web application using Python and Django to visualize trade data. The application includes features such as displaying a table of trade data, updating trade information, and visualizing trade data using line and bar charts.

## Key components of the project include:

### Model:
Define a Django model to represent trade data, including fields such as date, trade code, high, low, open, close, and volume.
#### This Project has two models part one for jsonModel which is used to make table visualization. Another one is databaseModel which is used to work on databases.If you click the jsonModel branch, you will get jsonModel code. Similarly, if you click database model,it will take to database model-related work
### Database: 
Utilize Django's ORM to interact with a database (e.g., MySQL) to store and retrieve trade data. I have used MYSQL here to save data

### Frontend Interface:
I have created HTML templates for the frontend interface using Django's template engine. Include features such as displaying trade data in a table, adding new trade entries, updating existing entries, and deleting entries.
#### I have added a beautiful navar, about section where you will get the idea of the project.
### Crud application
I have worked on all crud operations for insert, delete, update, and display data.

### Visualization:
Integrate JavaScript charting library (e.g., Chart.js) to visualize trade data as line and bar charts. Allow users to select trade codes via a dropdown menu to dynamically update the chart data.

### User Interaction:
Implement user-friendly features such as navigation links in the navbar, buttons for CRUD operations, and interactive dropdown menu for selecting trade codes.



## Project Problem solution
### Task No1
 Build a basic web app with Python and Django with this json, make a table visualization
 with the data in the home page of the website. Here is the csv of the same data if you
 need it.

 ### My Solution of Task 01
 I have made a table to visualize JSON file trade data.
 ![Screenshot (578)](https://github.com/injamul3798/StockProject_MLTechnicalTest/assets/101572467/6285d8a5-8657-4103-bfd9-dc5f7e75bc0b)

 
### Task No2 
 Loadthe data in an sql server, and make the frontend table rows editable. We want to
 see if you can make a crud application. If you have moved into this step, you are
 switching your model from the json to the sql server, keep the json and sql models
 separate, and use the new sql model from this step and onward. If you can make a git
 version for the previous step named jsonModel, and starting from this step make the new
 version sqlModel, it will be easier for us to go back and forth between the different
 models and test it out.

 ### My Solution of Task 02
 I have created frontend table rows editable. I have applied crud applications such as insert, delete, update, and display.Below some code
 I have also added the data in mysql database.We have added new data into mysql database
  ![Screenshot (583)](https://github.com/injamul3798/StockProject_MLTechnicalTest/assets/101572467/2cb63860-9906-4377-9d30-ec5c355211b9)
 ##### After inserting new data we can apply crud application on that.
 ![Screenshot (584)](https://github.com/injamul3798/StockProject_MLTechnicalTest/assets/101572467/5b23650c-17c9-4372-a414-650ce21cdb0e)


#### Add new trade
![Screenshot (580)](https://github.com/injamul3798/StockProject_MLTechnicalTest/assets/101572467/089ff25f-33b9-4080-8056-82e2ce1b5194)
#### Update Trade
![Screenshot (581)](https://github.com/injamul3798/StockProject_MLTechnicalTest/assets/101572467/2902c61a-e39a-4a86-831a-f3261ae8b06f)
#### Delete Trade
![Screenshot (582)](https://github.com/injamul3798/StockProject_MLTechnicalTest/assets/101572467/a3cd58d1-e58d-42b4-b801-420803a335fb)

### Task3 Visulization
![Screenshot (585)](https://github.com/injamul3798/StockProject_MLTechnicalTest/assets/101572467/f07cd037-654e-482c-b3f7-c5397524578d)

### Project Description
![Screenshot (586)](https://github.com/injamul3798/StockProject_MLTechnicalTest/assets/101572467/63e3dd03-a74c-4406-85e7-20212ec86618)
### About Project Devloper
![Screenshot (587)](https://github.com/injamul3798/StockProject_MLTechnicalTest/assets/101572467/239c0103-419b-4f57-8230-733e78b2b552)



Overall, the project demonstrates the development of a basic web application using Django framework, combining backend logic with frontend visualization to provide users with a comprehensive platform for managing and analyzing trade data.
