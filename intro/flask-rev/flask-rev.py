from flask import Flask, request, render_template, url_for
app = Flask(__name__)

@app.route("/")
def start():
    return render_template('start.html')

@app.route("/reversed")
def reversed():
    rev = request.args['rev'][::-1]
    return render_template('reversed.html', rev=rev)

@app.route('/user/<username>')
def show_user_profile(username):
   # show the user profile for that user
   return f'User {username}'

@app.route('/about')
def about():
   return "About Us"

# url_for('static', filename='style.css')
# test without client
# with app.test_request_context():
#    print(url_for('index', page=2, filter='name'))  # Output: '/user/JohnDoe'