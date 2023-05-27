from flask import Flask, render_template, request


app = Flask(__name__)





@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run()
