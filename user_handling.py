from json import loads,dumps,load,dump
from os import remove

def login(username):
	if test_username(username):
		with open(file_name,'r') as f:
			content=load(f)
		return content
	return False
def test_username(username):
	global file_name
	file_name=f'users/{username}.json'
	try:
		with open(file_name):
			return True
	except:
		return False
def create_user(username):
	file_name=f'users/{username}.json'
	try:
		with open(file_name,'x') as f:
			f.write('{"file_perm":false}')
		return True
	except:
		return False
def save_user(username,content):
	file_name=f'users/{username}.json'
	try:
		with open(file_name,'w') as f:
			dump(content,f)
			return True
	except:
		return False
def update_file_perms(username):
	base_user_data=login(username)
	if base_user_data['file_perm']==False:
		base_user_data['file_perm']=True
	else:
		base_user_data['file_perm']=False
	save_user(username,base_user_data)
def delete_user(username):
	if test_username(username):
		remove(file_name)
	else:
		return False
def check_file_perm(username):
	base_user_data=login(username)
	return base_user_data['file_perm']
if __name__=="__main__":
	if not test_username('default'):
		if create_user('default'):
			update_file_perms('default')
			print('default user has been created')
		else:
			print('ERROR')
	else:
		print('default user already exists')
