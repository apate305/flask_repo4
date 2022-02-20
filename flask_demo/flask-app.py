#!/usr/bin/env python

# Flask is looking for certain "folders" that it holds certain data in. 
# Like a static folder for flat data files (like the gdp file)
# Also flask is looking for template folder which contains HTML file. 

# We are doing 2 things here. We are creating a flask app that is going 
# to have a basic website to show our data. And we are going to render it 
# in the HTML file.

# Building flask app to display our us_gdp file into index.html 

# REMINDER: WATCH HTML SECTION IN DATACAMP AND ALEXIS WROTE AN ARTICLE
#  HOW TO BUILD A REST API THAT DOES BASIC CRUD FUNCTIONS

#pip install flask and specify what modules you need from library 
# to make application smaller so it can go faster! 

# Flask = lets you create instance of app
# Json = cux we will format it in json 
# render_template = cuz we are going to be rendering our data into 
#                   our template called HTML
# request = cuz we are going to accept data in the form of a request


from flask import Flask, json, render_template, request

# this allows flask to work with the folder structure
import os

#create instance of Flask app
# __name__ specifies what file this is, 
# name or file being called from another file
app = Flask(__name__)

#decorator: they are calling a function (used in web frameworks)
# flask is calling a function called route which lets us run the 
# code we put underneath when we go to the forward slash route: "/"

@app.route("/")
def echo_hello():
    return "Hello World!"


# Another decorator for a different route: this is for the gdp route
# create function called gdp
# return this file in our static folder by telling our flask app what 
# This is how we are telling the flask app to go from where it is to
# the us_gdp.json file: it is taking in the static folder by being 
# referenced as 'app.static_folder' followed by the actual name of file 
# (there is no path between those 2 things which is why we have "")
# Now we can open this file and load it to a json format
# Now we will use the render template: render will take any HTML file 
# that we pass into it and render data_json into it (Look at data in HTML 
# to see how the this py file and HTML file are connected)

# Note: YOU JUST HAVE TO RUN 'flask run' AFTER DOING THE FOLLOWING
@app.route("/gdp")
def gdp():
    json_url = os.path.join(app.static_folder,"","us_gdp.json")
    data_json = json.load(open(json_url))

    return render_template('index.html',data=data_json)

#Now, we will create a decorator to get the data based on year!
# we want our "link" to have "/gdp" and also whatever year we 
# pass into the "/<year>" parameter.
# that year is passed into the functon 'gdp_year and the same code 
# as above is used.

@app.route("/gdp/<year>")
def gdp_year(year):
    json_url = os.path.join(app.static_folder,"","us_gdp.json")
    data_json = json.load(open(json_url))

# Now lets examine the json file and see what we are working with: 
# there are a bunch of dictionaries inside of a list so we need to 
# get into that list first.
# 
# Now we are going to use request which will take what we pass into it 
# and let us interact with the file. We use 'view_args to get what is 
# passed in and convert to a variable 'year'

    data = data_json[1]
    #print(data) --> if you want to see it in terminal for troubleshoot purposes!
    year = request.view_args['year']

#filter data we want to show in HTML file and filter it down based on year 
#passed in using list comprehension checking to see if the date matches the
# year otherwise it would look teh same as the previous decorator code. 

    output_data = [x for x in data if x['date']==year]
    return render_template('index.html',data=output_data)

# this is checking: "if this is the main file that we are calling 
# (which it is) we want to do stuff otherwise we dont want to run it"
if __name__ == "__main__":
    app.run(debug=True)

# Now, we can run this by going to terminal and cd-ing into flask_demo. 
# And run the flask command: 
# we are exporting our flask app to what we called our flask app: 'flask-app'
# then we connect to our localhost thru 'flask run'
#      export FLASK_APP=flask-app
#      flask run  

