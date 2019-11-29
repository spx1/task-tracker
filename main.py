from flask import  Flask, render_template
from os import environ

mode = environ.get('RUN_MODE','Development')
app = Flask(__name__)
app.config.from_object(f'config.{mode}')

@app.route('/health_check')
def health_check():
    return render_template('health_check.html', msg=app.config['TEST_STRING'])

if __name__ == '__main__':
    #print('hello world')
    app.run(debug=True)

