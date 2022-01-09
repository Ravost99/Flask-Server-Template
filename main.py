from flask import Flask, render_template, request, url_for
import config
app = Flask('app')

@app.route('/')
def home():
  return 'Hello World!'

@app.route('/main/')
@app.route('/main/<name>')
def main(name=None):
  return render_template('main.html', name=name)

print(config.start_msg)
app.run(host=config.host, port=config.port)
