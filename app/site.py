from app import app, render_template

@app.route('/')
def home():
    #return 'Hello, world!'
    #return render_template('home.html')
    return render_template('index.html')

