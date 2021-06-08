from os import getenv
from app import create_app

settings = getenv('FLASK_CONFIG') or 'default'

app = create_app(settings)

if __name__ == '__main__':
    app.run()