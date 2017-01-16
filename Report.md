# CSCI544 Final Project Group 10 

## Movie Genre identification based on plot summary

Steps For Deploying the Application on the web:

 * Clone the bitbucket repository
 * Copy the contents of web_deployment folder into the servlet container of CGI Server like Apache Httpd.
 * Make sure the server has support to run the python programs. if it does not install python 2.7 from: https://www.python.org/downloads/
 * Follow the steps for installing NLTK module given here: http://www.nltk.org/data.html
 * Download the Cornell multi class svm Classifier binary from here: https://www.cs.cornell.edu/people/tj/svm_light/svm_multiclass.html
 * go to web_deployment directory and update the path of the classifier to point to the SVM binaries.
 * Open the genre.html from within the server like below.
  
 ```localhost:8080/~username/web_deployment/genre.html ```
 * Enter the plot summary in the text box given and click on get genre button.
 * The system takes some time to predict the genre the first time since it has to load the model into memory.