from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

members = []

@app.route('/')
def index():
    return render_template('index.html', members=members)

@app.route('/add_member', methods=['POST'])
def add_member():
    member_name = request.form['member_name']
    members.append({'name': member_name, 'workouts': []})
    return redirect(url_for('index'))

@app.route('/add_workout/<int:member_id>', methods=['POST'])
def add_workout(member_id):
    workout_type = request.form['workout_type']
    workout_duration = request.form['workout_duration']
    members[member_id]['workouts'].append({'type': workout_type, 'duration': workout_duration})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

