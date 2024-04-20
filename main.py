from flask import Flask

# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'hello test'
# if __name__ == '__main__':
#     app.run()


from website import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)