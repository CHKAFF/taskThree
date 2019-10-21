
class DBHandlerClass(object):
	"""docstring for ClassName"""
	def __init__(self, uid):
		self.base_name = "base_id"
		self.base_password = "base_password"
		self.user_id = uid
		
	def CreateNewVoucher(self, ):
		insert_query = "''INSERT INTO base_name (id) VALUES user_id''"
        cursor.execute(insert_query)