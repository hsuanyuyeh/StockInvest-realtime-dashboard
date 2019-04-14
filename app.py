from flask import Flask, render_template, request
from pusher import Pusher
import jinja2


app = Flask(__name__)

my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('/Users/yehhsuan-yu/something/stockinvest-dashboard'),
])
app.jinja_loader = my_loader
pusher = Pusher(app_id='756786', key='f3b051950a33ecdfb88f', secret='1c8ed0c8ad2f5eec224f', cluster='us2', ssl=True)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')


@app.route('/record', methods=['POST'])
def record():
	data = request.form
	pusher.trigger(u'record', u'add', {
		u'stock_name': data['stock_name'],
		u'buy_sell': data['buy_sell'],
		u'price': data['price'],
		u'amount': data['amount'],
         u'cost_reward': data['cost_reward']
	})
	return "record added"
    

if __name__ == '__main__':

    app.run(debug=True)
