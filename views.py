from flask import Flask,redirect, url_for, request,render_template,session

import models

app = Flask(__name__, template_folder='./templates/')

@app.route('/')
def index():
	return render_template('general/index.html')



# Institutes Section
#Index page of Institutes
@app.route('/institutes')
def institute_index():
	return render_template('institutes/index.html')

#Login Page of Institutes
@app.route('/institutes/login', methods=['GET', 'POST'])
def institutes_login():
	if(request.method == "POST"):
		email = request.form['inst_email']
		password = request.form["inst_password"]
		result = models.check_institute(email, password)
		if result:
			session['email'] = result['inst_email']
			session['name'] = result['inst_name']
			print("Session Created..")
			return render_template("institutes/homepage.html", detail=session['name'])
	return render_template('institutes/login.html')

# Registration of Institutes
@app.route('/institutes/register', methods=['GET', 'POST'])
def add_institute():
	if(request.method== 'POST'):
		name = request.form["inst_name"]
		princi = request.form["inst_principal"]
		addr = request.form["inst_address"]
		phone = request.form["inst_phone"]
		website = request.form["inst_website"]
		email = request.form["inst_email"]
		desc = request.form["inst_description"]
		aff = request.form['inst_affliated']
		pword = request.form['pword']
		status = models.add_institute(name, princi, addr, phone, website, email, desc, aff, pword)
		if status == True:
			return render_template('general/index.html')
	
	return render_template('institutes/registration.html', data=0)

@app.route('/institutes/edit', methods=['GET', 'POST'])
def edit_institute():
	data = models.get_institute_data(session['email'])
	if(request.method == 'POST'):
		return "Posting.."

	return render_template('institutes/registration.html', data=data)

#Adding Events Institutes
@app.route('/institutes/add_event', methods=['GET', 'POST'])
def add_event():
	if(request.method=='POST'):
		name = request.form["evt_name"]
		desc = request.form["evt_description"]
		hosted = request.form["evt_host"]
		date = request.form["evt_date"]
		time = request.form["evt_time"]
		status = models.add_event(name, desc, hosted, date, time)
		if status:
			return render_template('institutes/add_event.html')
			
	return render_template('institutes/add_event.html')

@app.route('/view_events', methods=['GET', 'POST'])
def view_events():
	events = models.view_events()
	return render_template('general/events.html', events=events)

#Adding Timetable Institutes
@app.route('/teachers/add_timetable', methods=['GET', 'POST'])
def add_timetable():
	if(request.method == 'POST'):
		cs = request.form["cs"]
		mon = list()
		tues = list()
		wed = list()
		thur = list()
		fri = list()
		for i in range(1,9):
			mon.append(request.form["mon"+str(i)])
			tues.append(request.form["tues"+str(i)])
			wed.append(request.form["wed"+str(i)])
			thur.append(request.form["thu"+str(i)])
			fri.append(request.form["fri"+str(i)])
		status = models.add_timetable(cs, mon, tues, wed, thur, fri)
		return render_template('teachers/add_timetable.html')
	return render_template('teachers/add_timetable.html')

# Adding Exams Institutes
@app.route('/institutes/add_exams', methods=['GET', 'POST'])
def add_exams():
	if(request.method == 'POST'):
		cs = request.form["cls"]
		sub = list()
		date = list()
		time = list()
		for i in range(1,7):
			date.append(request.form["date"+str(i)])
			sub.append(request.form["subject"+str(i)])
			time.append(request.form["time"+str(i)])
			
		status = models.add_exams(cs, date, sub, time)
		if status:
			return render_template('institutes/add_exams.html')

	return render_template('institutes/add_exams.html')













# Teachers Section
# Index Page of Teachers
@app.route('/teachers')
def teachers_index():
	return render_template('teachers/index.html')

# Registration for teachers
@app.route('/teachers/register', methods=['GET', 'POST'])
def add_teacher():
	institutes = models.get_institutes()
	if(request.method== 'POST'):
		inst_name = request.form["tchr_institute_name"]
		name = request.form["tchr_name"]
		dob = request.form["tchr_dob"]
		address = request.form["tchr_address"]
		phone = request.form["tchr_phone"]
		email = request.form["tchr_email"]
		pword = request.form['pword']
		status = models.add_teacher(inst_name, name, dob, address, phone, email, pword)
		if status == True:
			return render_template('teachers/index.html')
	
	return render_template('teachers/registration.html', institutes=institutes)

@app.route('/teachers/login', methods=['GET', 'POST'])
def check_teacher():
	if(request.method == "POST"):
		email = request.form['tchr_email']
		password = request.form["tchr_password"]
		result = models.check_teacher(email, password)
		if result:
			session['email'] = result['tchr_email']
			session['name'] = result['tchr_name']			
			print("Session Created..")
			return render_template('teachers/homepage.html', name=session['name'])
	return render_template('teachers/login.html')

@app.route('/teachers/activity', methods=['GET', 'POST'])
def add_activity():
	if(request.method == 'POST'):
		title = request.form['title']
		body = request.form['activity']
		date = request.form['date']
		status = models.add_activity(title, body, date)
		if status:
			return render_template('teachers/homepage.html', name=session['name'])

	return render_template('teachers/add_activity.html')

@app.route('/teachers/view_doubts', methods=['GET', 'POST'])
def view_doubts():
	results = models.view_doubts()
	return render_template('teachers/view_doubts.html', doubts=results)










# Students Section
# Index Page of Students
@app.route('/students')
def students_index():
	return render_template('students/index.html')

# Students Registration
@app.route('/students/register', methods=['GET', 'POST'])
def add_student():
	institutes = models.get_institutes()
	if(request.method== 'POST'):
		inst_name = request.form["stud_institute_name"]
		name = request.form["stud_name"]
		dob = request.form["stud_dob"]
		std = request.form["stud_standard"]
		address = request.form["stud_address"]
		phone = request.form["stud_phone"]
		email = request.form["stud_email"]
		parent = request.form["stud_parent"]
		pword = request.form['pword']
		status = models.add_student(inst_name, name, dob, std, address, phone, email, parent, pword)
		if status == True:
			return render_template('students/index.html')
	
	return render_template('students/registration.html', institutes=institutes)

# Students Login
@app.route('/students/login', methods=['GET', 'POST'])
def check_student():
	if(request.method == "POST"):
		email = request.form['stud_email']
		password = request.form["stud_password"]
		result = models.check_student(email, password)
		if (result is not None):
			session['email'] = result['stud_email']
			session['name'] = result['stud_name']
			print("Session Created..")
			act = models.view_activities()
			print(act)
			return render_template('students/homepage.html', result=result, act=act)
		else:
			return render_template('students/login.html')
	return render_template('students/login.html')

# Students Notifications
@app.route('/students/notify', methods=['GET', 'POST'])
def add_notification():
	usr = request.args.get('id')
	past = models.view_notice(usr)
	if(usr is not None):
		if(request.method== 'POST'):
			notification_type = request.form["notification_type"]
			subject = request.form["subject"]
			body = request.form["body"]
			author = request.form["author"]
			status = models.add_notice(usr, notification_type, subject, body, author)
			if status:
				return render_template('students/notifications.html',records=past)
	return render_template('students/notifications.html',records=past)

@app.route('/students/add_doubt', methods=['GET', 'POST'])
def add_doubt():
	usr = request.args.get('id')
	past = models.view_notice(usr)
	if(usr is not None):
		if(request.method == 'POST'):
			teacher = request.form['teacher']
			title = request.form['title']
			body = request.form['body']
			status = models.add_doubts(session['name'], teacher, title, body)
			if status:
				return render_template('students/add_doubts.html')
	return render_template('students/add_doubts.html')






@app.route('/logout')
def logout():
	session.pop('email', None)
	session.pop('name', None)
	return render_template("general/index.html")

app.secret_key = 'SsAaNnOoJjMmAaTtHhEeWw'

if __name__ == '__main__':
	print("Running Students Diary..")
	app.run(debug = True)