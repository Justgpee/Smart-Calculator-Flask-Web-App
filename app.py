from flask import Flask, request, render_template
from calculator.arithmetic import add, subtract, multiply, divide
from calculator.area import circle, rectangle, square, triangle
from calculator.quadratic import solve

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        num1 = request.form.get("num1", type=float)
        num2 = request.form.get("num2", type=float)
        operation = request.form.get("operation")

        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
    return render_template("index.html", result=result)


#area route 
@app.route("/area", methods=["GET", "POST"])
def area():
    result = None
    if request.method == "POST":
        shape = request.form["shape"]   # read shape first to decide which inputs to read next 
        if shape == "rectangle":
            length = float(request.form["length"])
            width = float(request.form["width"])
            result = rectangle(length, width)
        elif shape == "square":
            side = float(request.form["side"])
            result = square(side)
        elif shape == "triangle":
            base = float(request.form["base"])
            height = float(request.form["height"])
            result = triangle(base, height)
        elif shape == "circle":
            radius = float(request.form["radius"])
            result = circle(radius)
    return render_template("area.html", result=result)

#quadratic route 
#reads three inputs (a, b, c) and calls solve()
@app.route("/quadratic", methods=["GET", "POST"])
def quadratic():
    result = None
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        c = float(request.form["c"])
        result = solve(a, b, c)    # returns tuple (x1, x2) or "No solution"
    return render_template("quadratic.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)