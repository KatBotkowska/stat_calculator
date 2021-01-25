from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/stat_calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'GET':
        #formularz kalkulatora
        return render_template('calculator.html')

    else:
        #POST method
        #zwrot danych z kalkulatora

        pass



if __name__ == '__main__':
    app.run()
