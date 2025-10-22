from flask import Flask, render_template
from routes.recommend_route import recommend_bp

app = Flask(__name__)
app.register_blueprint(recommend_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
