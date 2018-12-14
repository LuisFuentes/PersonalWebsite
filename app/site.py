from app import application, render_template

@application.route('/')
def home():
    #return 'Hello, world!'
    #return render_template('home.html')
    return render_template('index.html')

