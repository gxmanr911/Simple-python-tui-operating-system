import user_handling
def login():
	while True:
		username=input("Username:")
		userinfo=user_handling.login(username)
		if userinfo== False:
			userin=input("Not a valid username, [T]ry again or [C]reate a new user")
			if userin.upper()=="C":
				if user_handling.create_user(username):
					print("user created")
					userinfo=user_handling.login(username)
					return userinfo
				else:
					print('An error has occured')
		else:
			return userinfo
def app_selection():
	from os import listdir
	apps=[]
	app=listdir('./apps')
	del listdir
	for i in app:
		apps.append(i.replace('.py','').replace('_'," ").capitalize())
	for i in enumerate(apps):
		print(f"{i[0]}:{i[1]}")
	while True:
		try:
			userin=int(input('enter index: '))
			if userin<=len(app)-1:
				break
			pass
		except:
			pass
	from runpy import run_path
	file_path=f'./apps/{app[userin]}'
	with open('args.txt','w') as f:
		f.write(str(UserData['file_perm']))
	f=run_path(file_path,run_name='__main__')
	del run_path
def file_permisons():
	if UserData['file_perm']:
		userin=input("you have file permitions would you like to grant another user file permitions[Y]/[N]: ")
		if userin.upper()=='Y':
			userin=input('enter username of the user you would like to grant file permitions: ')
			if user_handling.test_username(userin):
				if user_handling.login(userin)['file_perm']==False:
					user_handling.update_file_perms(userin)
					print('file perms added')
					return False
				else:
					print('user already has file permition')
					RemovePermUserIn=input("would you like to remove file perms[Y]/[N]: ")
					if RemovePermUserIn.upper()=='Y':
						user_handling.update_file_perms(userin)
						print('file perms removed')
						return True
			else:
				print('invalid username returning to menu')
				return False
		else:
			return None
	else:
		print('you dont have file perms')
def menu():
	userin=input('[O]pen app\n[F]ile permisons\n[L]ogout\nEnter letter: ')
	if userin.upper()=='O':
		app_selection()
	elif userin.upper() == 'L':
		start_up()
	elif userin.upper()=='F':
		file_permisons()
	menu()
def start_up():	
	global UserData
	UserData=login()
	menu()
if __name__=="__main__":
	start_up()