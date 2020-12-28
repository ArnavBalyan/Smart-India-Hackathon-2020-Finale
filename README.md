![Build](https://github.com/arnavbalyan/SIH/workflows/Python%20application/badge.svg)
# Production Scale Web App for Smart India Hackathon '20 (Finals) 
A uWsgi Production level application built for hosting the architecture of our project and APIs for Smart India Hackathon Finals 2020. <br>
The application serves the following:
> - 8 poweful machine learning models
> - 5 APIs
> - 2 Mobile Applications
> - Privacy Policy
> - Routes to the Backend Database and our Dashboards. <br>
The Flask uWsgi app is deployed using a Gunicorn server which is behing Nginx for production scale along with Restful APIs which serve json data to the hardware. 

## Machine Learning Models:
The following algorithms were used for creating ML models:
> - Random Forest
> - Bagging Classifier
> - Extra Trees
> - LSTM
> - XGBoost
> - AdaBoost
> - Decision Tree
> - LightGBM

## APIs 
5 Restful APIs hosted for returning json data the Hardware Hub. The following are the API endpoints (root is the host url):
> - root/search/v1/params
> - root/search/v2/params
> - root/privacy-policy
> - root/android
> - root/iOS
These are essential to integrate all components of the solution together.

## Mobile Applications:
![alt text](https://github.com/ArnavBalyan/SIH/blob/master/dashboards/sih_dashboard.png "Main Dash")
![alt text](https://github.com/ArnavBalyan/SIH/blob/master/dashboards/sih_dashboard1.png "Dash")
![alt text](https://github.com/ArnavBalyan/SIH/blob/master/dashboards/sih_dashboard2.png "Main Db")
![alt text](https://github.com/ArnavBalyan/SIH/blob/master/dashboards/sih_dashboard3.png "Db")
