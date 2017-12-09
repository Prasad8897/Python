class Email(object):
	"""docstring for Email"""
	def __init__(self, arg):
		super(Email, self).__init__()
		self.date = arg['date']
		self.from_email = arg['from_email']
		self.to_email = arg['to_email']
		self.subject = arg['subject']
		self.mailing_list = arg['mailing_list']
		self.id = arg['id']

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		