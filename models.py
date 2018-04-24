import orm
# Institutes Section
def get_institutes():
	institute = orm.Institute()
	result = institute.get_institutes()
	return result

def add_institute(name, princi, address, contact, website, email, desc, aff, pword):
	institute = orm.Institute()
	result = institute.register(name, princi, address, contact, website, email, desc, aff, pword)
	return result

def get_institute_data(inst_id):
	institute = orm.Institute()
	result = institute.get_institute_data(inst_id)
	return result


def check_institute(email, password):
	institute = orm.Institute()
	result = institute.check_institute(email, password)
	return result

def add_event(name, desc, hosted, date, time):
	event = orm.Event()
	result = event.add_event(name, desc, hosted, date, time)
	return result

def view_events():
	event = orm.Event()
	result = event.view_events()
	return result

def add_timetable(cs, mon, tues, wed, thur, fri):
	timetable = orm.Timetable()
	result = timetable.add_timetable(cs, mon, tues, wed, thur, fri)
	return result

def add_exams(c, date, sub, time):
	exam = orm.Exam()
	result = exam.add_exams(c, date, sub, time)
	return True

# Teachers Section
def add_teacher(inst, name, dob, address, contact, email, pword):
	teacher = orm.Teacher()
	result = teacher.register(inst, name, dob, address, contact, email, pword)
	return result

def check_teacher(email, password):
	teacher = orm.Teacher()
	result = teacher.check_teacher(email, password)
	return result

def add_activity(title, body, date):
	activity = orm.Activities()
	result = activity.add_activity(title, body, date)
	return result

def view_activities():
	activity = orm.Activities()
	result = activity.view_activities()
	return result

# Students Section
def add_student(inst_name, name, dob, std, address, phone, email, parent, pword):
	student = orm.Student()
	result = student.register(inst_name, name, dob, std, address, phone, email, parent, pword)
	return result

def check_student(email, password):
	student = orm.Student()
	result =  student.check_student(email, password)
	return result

def add_notice(student, req, subject, body, author):
	notice = orm.Notification()
	result = notice.add_notification(student, req, subject, body, author)
	return result

def view_notice(student):
	notice = orm.Notification()
	result = notice.view_notifications(student)
	return result

def add_doubts(student, teacher, title, body):
	doubt = orm.Doubts()
	result = doubt.add_doubts(student, teacher, title, body)
	return result

def view_doubts():
	doubt = orm.Doubts()
	result = doubt.view_doubts()
	return result