from flask import Flask, render_template
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    '''
    This function just responds to the browser URL
    localhost:5000/

    :return: the rendered template 'home.html'
    '''
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)