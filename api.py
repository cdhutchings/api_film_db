from flask import Flask, request, render_template, json
app = Flask(__name__)


@app.route('/') #endpoint route to receive get or post requests
def index():
    #do something
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'



@app.route('/filmpost', methods = ['POST'])
def filmpost():
    # Capture the incoming JSON Body
        # Capture the params
        # Access the incoming params
        # get the JSON

    # Extract relevant data
    # Call our method that saves to the DB
        # Send in the relevant data

    params = request.data
    param_dict = json.loads(params)

    return render_template("filmresult.html", param_dict=param_dict)




@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/postform", methods=["POST"])
def postform():


    data = request.data
    dataDict = json.loads(data)

    fname = dataDict["firstname"]
    lname = dataDict["lastname"]

    return render_template("result.html", fname=fname, lname=lname)


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)