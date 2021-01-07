![Build](https://github.com/arnavbalyan/SIH/workflows/Python%20application/badge.svg)
<span style="color:black">
# Production Scale Web Application for Smart-India-Hackathon '20 (Finals) 
A uWsgi Production level application built for hosting the architecture of our project and APIs for Smart India Hackathon Finals 2020. <br>
The application serves the following:
> - 8 machine learning models
> - 5 APIs
> - 2 Mobile Applications
> - Privacy Policy
> - Routes to the Backend Database and our Dashboards. <br>
 
The Flask uWsgi app is deployed using a Gunicorn server which is behing Nginx for production scale along with Restful APIs which serve json data to the hardware. 

## Machine Learning Models:
The following algorithms were used for creating ML models:
 - Random Forest
 - Bagging Classifier
 - Extra Trees
 - LSTM
 - XGBoost
 - AdaBoost
 - Decision Tree
 - LightGBM

## APIs: 
5 Restful APIs hosted for returning json data the Hardware Hub. The following are the API endpoints (root is the host url):
 - root/search/v1/params
 - root/search/v2/params
 - root/privacy-policy
 - root/android
 - root/iOS <br>
 
 These are essential to integrate all components of the solution together.

## Mobile Applications:
Independent Web Views have exist for both Android and iOS, however real time dynamic data is served to them via this web application.
 - Refer to APIs to access them.
 
## Privcacy Policy:
The collected data is not processed by or shared with any third parties. Detailed Privacy Policy is available on the web app, refer to API for endpoint.

## Backend Database and Dashboards:
The Dashboards serve real time data and visualizations by making use of InfluxDb which is a no-SQL based application. The routes to Db and Dashboards are not disclosed for security reasons.

## Continuous Integration/ Continuous Delivery:
CI/CD pipeline is set up with Github Actions for seamless deployment to the servers.  ![Build](https://github.com/arnavbalyan/SIH/workflows/Python%20application/badge.svg)


## Images:
This is how the app looks like to an operator where real time data, visualizations and analytics are available. 
<br/>
&nbsp;

![alt text](https://github.com/ArnavBalyan/SIH/blob/master/dashboards/sih_dashboard.png "Main Dash")
![alt text](https://github.com/ArnavBalyan/SIH/blob/master/dashboards/sih_dashboard1.png "Dash")
![alt text](https://github.com/ArnavBalyan/SIH/blob/master/dashboards/sih_dashboard2.png "Main Db")
![alt text](https://github.com/ArnavBalyan/SIH/blob/master/dashboards/sih_dashboard3.png "Db")
</span>

## Team:
The people who made this possible.
 - [Arnav Balyan](https://github.com/ArnavBalyan)
 - [Pushpinder Pal Singh](https://github.com/pushpinderpalsingh)
 - [Devesh Sangwan](https://github.com/deveshsangwan)
 - [Shubhankar Rawat](https://github.com/ShubhankarRawat)
 - [Anshita Goel](https://github.com/anshitagoel19)
 - [Aditi Chawla](https://github.com/aadiitii)

