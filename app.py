from flask import Flask, render_template,jsonify

app = Flask(__name__)

jobs = [
  {
    'id' : 1,
    'title' : 'Data Analyst',
    'location' : 'Pulchowk, Nepal',
    'salary' : 'Rs. 1,00,000'
  },
  {
    'id' : 2,
    'title' : 'Data Scientist',
    'location' : 'Maitidevi, Nepal',
    'salary' : 'Rs. 50,000'
  },
  {
    'id' : 3,
    'title' : 'Gre Tutor',
    'location' : 'Putalisadak, Nepal',
    'salary' : 'Rs. 40,000'
  },
  {
    'id' : 4,
    'title' : 'Junior Delivery Engineer',
    'location' : 'Maharajgunj, Nepal',
    'salary' : 'Rs. 65,000'
  }
]

@app.route('/') #decorators
def hello_world():
  return render_template('home.html', jobs=jobs)

@app.route('/api/jobs')  # doesnot render html page 
def list_jobs():
  return jsonify(jobs)

  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)