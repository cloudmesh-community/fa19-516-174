# AI REST Services using Open API

Sahithi Ancha, sancha@iu.edu, [fa19-516-174](https://github.com/cloudmesh-community/fa19-516-174)

:o2: please finish

:o2: gregor also addea a README.md with some notes that chould be
pointed to or integarted

## Abstract

This project aims to provide an AI-service for the logistic regression functionality via two methods, namely Scikit-Learn and Keras. The user inputs a file which is saved to the MongoDB database. Then we retrieve the same file and perform logisctic regression on it according to the user input, i.e., based on the service the user specifies.

## Introduction

We first connect to the MongoDB database via the server file which also directs us to the Open Api scpecification which contains the endpoints for the user to access. I created a seperate python file to make uploading files by the user much easier. The uploaded file that is in the '.csv' format is converted to json and then uploaded to the database. When the user indicates that they want to fit and predict based on the dataset they provide, this same file is retrieved and then processed in order to fit a logistic regression model, predict values and also print out the accuracy score.

To connect to the MongoDB database, I used cloudmesh -> mongo -> cmdatabase.
Also, I can upload any file in the same directory with ease but if it's in a different folder, this upload function does not work and I have to fix it. 

(To-do: 
* I'm trying to figure out how to convert the json file back into a csv file before proscessing it. Alternatively, i'm also trying to save the csv file as it is without changing its format so that it's easier to retrieve and process.
* I got the part of returning values after fitting them wrong and need to use Jsonify as Professor mentioned. While my program can fit and predict with an average accuracy score, I need to find a better way to pass the values returned from fit to the predict function.)

## Related Work

## Architecture

## Technologies used

* cloudmesh
* Python
* REST
* Open API
* Flask
* MongoDB

## Progress

* Set up the computer
* Installed cloudmesh
* Set up MongoDB
* Uploaded files to MongoDB database
* Wrote API programs for 4 AI services
* Wrote programs for the Scikit-Learn and Keras Logistic Regression.

## Benchmark and Evaluation 

* Access and use the AI services 

## Conclusion

## References

*
