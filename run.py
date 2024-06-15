from flask import Flask, render_template

print("Initializing FLask app...")

app = Flask(__name__)

@app.route('/')
def index():
    print("Rendering index.html")
    return render_template('index.html')

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)
