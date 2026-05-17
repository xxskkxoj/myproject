from flask import Flask, render_template, request, redirect, url_for, flash, session
from backend_adapter import (
	init_files,
	get_all_user,
	save_user,
	get_all_activity,
	get_all_enroll,
	save_enroll,
)


app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = "silverboost"


@app.route('/')
def splash():
	return render_template('splash.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		name = request.form.get('username')
		pwd = request.form.get('password')

		users = get_all_user()
		for u in users:
			if u.get('name') == name and u.get('pwd') == pwd:
				session['username'] = name
				flash('Login successful, welcome back!', 'success')
				return redirect(url_for('dashboard'))

		flash('Incorrect username or password', 'danger')
		return redirect(url_for('login'))

	return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		name = request.form.get('username')
		phone = request.form.get('phone')
		pwd = request.form.get('password')
		repwd = request.form.get('repassword')

		if pwd != repwd:
			flash('Passwords do not match', 'danger')
			return redirect(url_for('register'))

		users = get_all_user()
		for u in users:
			if u.get('name') == name:
				flash('Username already exists', 'danger')
				return redirect(url_for('register'))

		users.append({'name': name, 'phone': phone, 'pwd': pwd})
		save_user(users)
		flash('Registration successful. Please log in.', 'success')
		return redirect(url_for('login'))

	return render_template('register.html')


@app.route('/dashboard')
def dashboard():
	if 'username' not in session:
		flash('Please log in first', 'danger')
		return redirect(url_for('login'))

	username = session.get('username')
	activities = get_all_activity()
	return render_template('dashboard.html', username=username, activities=activities)


@app.route('/activities/<path:category>')
def activities(category):
	if 'username' not in session:
		flash('Please log in first', 'danger')
		return redirect(url_for('login'))

	all_acts = get_all_activity()
	act_list = all_acts.get(category, [])
	return render_template('activities.html', category=category, activities=act_list)


@app.route('/enroll/<path:category>/<int:act_idx>')
def enroll(category, act_idx):
	if 'username' not in session:
		flash('Please log in first', 'danger')
		return redirect(url_for('login'))

	username = session.get('username')
	all_acts = get_all_activity()
	act_list = all_acts.get(category, [])
	if act_idx < 0 or act_idx >= len(act_list):
		flash('Invalid activity', 'danger')
		return redirect(url_for('dashboard'))

	selected = act_list[act_idx]
	enrolls = get_all_enroll()
	if username not in enrolls:
		enrolls[username] = []
	if selected not in enrolls[username]:
		enrolls[username].append(selected)
		save_enroll(enrolls)
		flash(f'Enrolled successfully: {selected}', 'success')
	else:
		flash('You have already enrolled in this activity', 'warning')

	return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
	session.pop('username', None)
	flash('You have logged out successfully', 'success')
	return redirect(url_for('login'))


if __name__ == '__main__':
	init_files()
	app.run(debug=True)
