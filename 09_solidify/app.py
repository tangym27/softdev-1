# import flask
from flask import Flask, render_template
# import uniform from random to generate random floats
from random import uniform
# to access csv.reader() to read csv files
import csv

# instantiate instance of Flask class
app = Flask(__name__)

collection = [0, 1, 1, 2, 3, 5, 8]

# dictionary that will hold floating percentages as keys, and key-values are
# the occupations
csvDict = {}
# list to store a list of percentages(this is for the weighted random function)
list = []

# with statement means less errors(automatically closes file)
with open("data/occupations.csv","r") as csvF:
    csvR = csv.reader(csvF) # reads the csv file
    # iterate through the csv file
    for line in csvR:
        # as long as its not the first and last lines(which has no important info)
        # add the percentages to the dictionary as a key, and add the appropriate
        # key value(occupation)
        if line[0] != "Job Class" and line[0] != "Total":
            csvDict[float(line[1])] = line[0]
            list.append(float(line[1])) # also add the percentage to the list

# sort list in ascending order
list = sorted(list)

# weighted random function takes in a list(of the percentages used earlier) as input
def weight(list):
    total = 0.0 # this will represent the total percentage(99.8)
    for i in list: # this adds the actual percentages
        total += i
    # generate a random percentage
    rand = uniform(0, total)
    index = 0
    temp = 0.0
    # iterate through the list, add the percentage at index i to a temp float,
    # and if that temp float is >= the randomly generated percentage, return the key
    # value of that percentage(occupation)
    for i in list:
        temp += i
        if temp >= rand:
            print(csvDict[list[index]])
            break
        else: # otherwise increase the index to the next-to-smallest percentage
            index += 1



            
# route 1: homepage
@app.route("/my_foist_template")
def herro():
    text = '''
    <h1 style='text-align: center;'>Hello Peeps!</h1>
    <br><br><form action="/static/index.html">
        <center><input type="submit" value="Click for Surprise!"/></center>
    </form>'''
    print(weight(list))
    return render_template('index.html',
                               d=collection,
                               i=0,
                               name="fooooo")

@app.route("/occupations")
def occu():
    return weight(list)
