from flask import Flask, render_template

app = Flask(__name__, static_folder='build', template_folder='build')             

@app.route('/')                   
def index():                      
    return render_template('index.html') 
    # return 'Hi'

@app.route('/api')
def api():
    return "hello!"


if __name__ == "__main__":        
    app.run(debug=True) 