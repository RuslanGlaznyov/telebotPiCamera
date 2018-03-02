import const

def log(message):
	try:
		from datetime import datetime
		log = "time:{}\nuser_id :{}\nusername {}\nname :{}\nlast_name :{}\ntext :{}\n\n".format(str(datetime.now()),
			str(message.from_user.id), message.from_user.username, message.from_user.first_name,
				message.from_user.last_name, message.text)
	except Exception as e:
		with open(error_file_path, "a") as error:
			error.write(traceback.format_exc(10))
	with open(const.log_file_path, "a") as file:
		file.write(log)
