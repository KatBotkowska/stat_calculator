from flask import Flask, request, render_template
from patterns import z_calc
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'GET':
        #calculator form
        return render_template('calculator.html')

    else:
        #POST method
        try:
            p1 = int(request.form["p1"])
            p2 = int(request.form["p2"])
            n1 = int(request.form["n1"])
            n2 = int(request.form["n2"])

        except ValueError:
            result = "Give me numbers!"
            return render_template("calculator.html", result=result)
        except KeyError:
            result = "Don't send data"
            return render_template("calculator.html", result=result)
        try:
            result = z_calc(p1, p2, n1, n2)
        except  ValueError as e:
            result = e
        return render_template("calculator.html", result=str(result))





if __name__ == '__main__':
    app.run()
