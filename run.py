from flask import Flask, render_template
from src.app import create_app
from src import routes

app = create_app()

routes.init_app(app)

if __name__ == '__main__':
    app.run(debug = True)