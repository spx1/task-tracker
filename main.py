from flask import  Flask, render_template

app = Flask(__name__)

@app.route('/health_check')
def health_check():
    return render_template('health_check.html')

if __name__ == '__main__':
    #print('hello world')
    app.run(debug=True)

