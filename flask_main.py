from flask import Flask, render_template

app = Flask(__name__)
projects = [
    {
        'title': 'Python and Flask',
        'description': 'Description on project',
        'technologies': ['Python', 'Flask', 'HTML', 'CSS'],

    },
    {
        'title': 'Golang',
        'description': 'Description on project',
        'technologies': ['Golang', 'HTML', 'CSS'],

    },

]


@app.route('/')
def index():
    return render_template('index.html', projects=projects)


if __name__ == '__main__':
    app.run(debug=True)
