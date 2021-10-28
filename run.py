from flask import Flask
from second import app


if __name__ == '__main__':
    app.run(port=5500, debug = True)