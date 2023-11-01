from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def do_add():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)

    return str(result)


@app.route('/sub')
def do_sub():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)

    return str(result)


@app.route('/mult')
def do_mult():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)

    return str(result)


@app.route('/div')
def do_div():

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)

    return str(result)

________________________________------------________________

#PART TWO

operators = {
    "add" : add,
    "sub" : sub,
    "mult" : mult,
    "div" : div,
    }

@app.route('/math/<opp>')
def do_calc(opp):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    # finds the opp that is in the url and what it corresponds to 
    # in the dictionary operators and sets that as the function
    # and passes in a and b as arguments
    result = operators[opp](a,b)
    return str(result)

