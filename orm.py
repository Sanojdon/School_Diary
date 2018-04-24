from pymongo import MongoClient
from datetime import datetime

connection = MongoClient("localhost", 27017)

class Institute:
	def __init__(self):
		self.db = connection.students_diary.institutes

	def register(self, name, princi, address, contact, website, email, desc, aff, pword):
		institute = {'inst_name' : name, 'inst_principal' : princi, 'inst_address' : address,
					 'inst_contact' : contact, 'inst_website' : website, 'inst_email' : email,
					 'inst_description' : desc, 'inst_affliated' : aff, 'inst_password' : pword,
					 'inst_created_on' : datetime.now()}
		self.db.insert(institute)
		return True

	def check_institute(self, email, password):
		check = {'inst_email' : email, 'inst_password' : password}
		result = self.db.find_one(check)
		return result

	def get_institute_data(self, inst_email):
		check = {'inst_email' : inst_email }
		result = self.db.find_one(check)
		return result

	def get_institutes(self):
		check = {'inst_name' : 1}
		result = self.db.find({}, check)
		return result

	def close_connection():
		connection.close()

class Event:
	def __init__(self):
		self.db = connection.students_diary.events

	def add_event(self, name, desc, hosted, date, time):
		event = {'evt_name' : name, 'evt_desc' : desc, 'evt_hosted' : hosted,
				 'evt_date' : date, 'evt_time' : time, 'evt_created_on' : datetime.now()}
		self.db.insert(event)
		return True

	def view_events(self):
		result = self.db.find()
		return result

class Exam:
	def __init__(self):
		self.db = connection.students_diary.exams

	def add_exams(self, c, date, sub, time):
		exams = {'exm_class' : c, 'exm_dates' : date, 'exm_subjects' : sub, 'exm_times' : time, 
				 'exm_created_on' : datetime.now()}
		self.db.insert(exams)
		return True

class Timetable:
	def __init__(self):
		self.db = connection.students_diary.timetables

	def add_timetable(self, cs, mon, tues, wed, thur, fri):
		timetable = {'tbl_class' : cs, 'tbl_mon' : mon, 'tbl_tues' : tues, 'tbl_wed' : wed,
					  'tbl_thur' : thur, 'tble_fri' : fri, 'tbl_created_on' : datetime.now()}
		self.db.insert(timetable)
		return True

class Teacher:
	def __init__(self):
		self.db = connection.students_diary.teachers

	def register(self, inst, name, dob, address, contact, email, pword):
		teacher = {'tchr_institute_name' : inst, 'tchr_name' : name, 'tchr_dob' : dob,
					 'tchr_address' : address, 'tchr_phone' : contact, 'tchr_email' : email,
					 'tchr_password' : pword, 'tchr_created_on' : datetime.now() }
		self.db.insert(teacher)
		return True

	def check_teacher(self, email, password):
		check = {'tchr_email' : email, 'tchr_password' : password}
		result = self.db.find_one(check)
		return result

class Student:
	def __init__(self):
		self.db = connection.students_diary.students

	def register(self, inst, name, dob, std, address, phone, email, parent, pword):
		student = {'stud_institute_name' : inst, 'stud_name' : name, 'stud_dob' : dob,
					 'stud_address' : address, 'stud_phone' : phone, 'stud_email' : email,
					 'stud_parent' : parent, 'stud_password' : pword, 'stud_created_on' : datetime.now() }
		self.db.insert(student)
		return True

	def check_student(self, email, password):
		check = {'stud_email' : email, 'stud_password' : password }
		result = self.db.find_one(check)
		return result

class Notification:
	def __init__(self):
		self.db = connection.students_diary.notifications

	def add_notification(self, student, req, subject, body, author):
		notification = {'ntfn_student' : student, 'ntfn_type' : req, 'ntfn_subject' : subject,
					    'ntfn_body' : body, 'ntfn_author' : author, 'ntfn_created_on' : datetime.now() }
		self.db.insert(notification)
		return True

	def view_notifications(self, student):
		check = {'ntfn_student' : student}
		result = self.db.find(check)

		return result

class Doubts:
	def __init__(self):
		self.db = connection.students_diary.doubts

	def add_doubts(self, student, teacher, title, body):
		doubt = { 'dbts_student' : student, 'dbts_teacher' : teacher, 'dbts_title' : title,
				  'dbts_body' : body, 'dbts_created_on' : datetime.now()}
		self.db.insert(doubt)
		return True

	def view_doubts(self):
		result = self.db.find()
		return result

class Activities(object):
	def __init__(self):
		self.db = connection.students_diary.activities

	def add_activity(self, title, body, date):
		activity = {'act_title' : title, 'act_body' : body, 'act_date' : date,
					'act_created_on' : datetime.now()}
		self.db.insert(activity)
		return True

	def view_activities(self):
		result = self.db.find()
		return result