import logging
from flask import Flask, render_template

gunicorn_logger = logging.getLogger('gunicorn.error')


app = Flask(__name__, 
            static_folder='./build', 
            template_folder='./build', 
            static_url_path='/')             
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)

@app.route('/')                   
def index():                      
    return render_template('index.html') 

@app.route('/api')
def api():
    return "hello!"


if __name__ == "__main__":        
    app.run(debug=True) 