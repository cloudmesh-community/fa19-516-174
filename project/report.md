# AI REST Services using Open API

Sahithi Ancha, sancha@iu.edu, [fa19-516-174](https://github.com/cloudmesh-community/fa19-516-174)
  
## Abstract

We try to develop a dockerized AI-service for the Random Forest functionality via Scikit-Learn. This application is deployed on Google cloud as well as AWS. The user should be able to access and run curl commands from their own terminal with the ip address provided. CSV files can be uploaded to fit and predict.

## Introduction

The first step is to create a simple service that demonstrates the random forest function. All the required files are bundled in an app and a Dockerfile is added as well. This same file is used to build an image later on for deploying onto the cloud services. The dockerfile tells the system to install the requirements and run the server file. This server file in turn points to the yaml file that specifies and configures the end points for our application. 

The first cloud setup I've used is Google. I have created a project called cloudmesh (same as it was mentioned in the document), enabled the API and also created a service account key aand saved it as google.json in the ~/.cloudmesh/security folder and then registered it to cloudmesh. The entire procedure has been based on the document - https://cloudmesh.github.io/cloudmesh-manual/accounts/google/account.html. We create and connect to a cluster next. A docker image is built from the existing dockerfile. This image is then tagged and pushed to the google container registry. From this image we create a deployement using the deployment.yaml file, which makes it easier for us to configure any sepcifications we have. Once the deployment has been created, to be able to access it outside of the kubernetes cluster, we create a service and run it. Once created, an external IP address is provided, which we can use to run our curl commands. 

The IP address that can be used to access this service is http://34.74.93.11:5000/.
To test the service, I have created my own csv files with simple classification. The following curl commands can be used to upload csv files -

To upload a file: 
curl -X POST "http://34.74.93.11:5000/rf/upload" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@<filename>.csv;type=text/csv"

To fit the data with specified parameters: 
curl -X POST "http://34.74.93.11:5000/rf/fit" -H "accept: text/csv" -H "Content-Type: application/json" -d "{\"job_id\":0,\"model_params\":{\"max_depth\":2}}"

To predict a file: 
curl -X POST "http://34.74.93.11:5000/rf/predict" -H "accept: text/csv" -H "Content-Type: multipart/form-data" -F "job_id=0" -F "file=@<filename>.csv;type=text/csv"

## Design 
### Architecture

![Architecture](images/ar.png){#fig:174-arch}

## Implementation
### Technologies Used
* cloudmesh
* Python
* REST
* Open API
* Flask
* Google Cloud
* AWS

## Results

### Deployment Benchmarks
### Application Benchmarks
### Benchmark and Evaluation 

* Access and use the AI services -
For this, we will need to be able to run the above mention curl commands from the terminal. This has been done seamlessly and there are no issues with google cloud.

## Conclusion

## References

* https://cloud.google.com/kubernetes-engine/docs/quickstarts/deploying-a-language-specific-app#python
* https://scotch.io/tutorials/google-cloud-platform-i-deploy-a-docker-app-to-google-container-engine-with-kubernetes

## Appendix

Results for Google Cloud-

* Upload file
![Appendix](https://github.com/cloudmesh-community/fa19-516-174/blob/master/project/images/1.PNG)

* Specify parameters and fit
![Appendix](https://github.com/cloudmesh-community/fa19-516-174/blob/master/project/images/2.PNG)

* Predict a new file
![Appendix](https://github.com/cloudmesh-community/fa19-516-174/blob/master/project/images/3.PNG)
