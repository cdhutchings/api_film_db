from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/postform", methods=["POST"])
def postform():

    # result = request.form
    # return render_template("result.html", result=result)
    # CAPTURE A BODY OF JSON
    # SORT NOUT DATA
    # CALL MATHOD TO MAKE DATA PERSISTENT

    return "Hello!"
    pass

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)