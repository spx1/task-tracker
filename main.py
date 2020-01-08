from app import create_app
import os

app = create_app(os.environ.get('RUN_MODE','Development'))
if __name__ == '__main__':
    app.run(debug=True)

