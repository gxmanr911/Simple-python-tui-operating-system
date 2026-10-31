#import user_handling
#file_permitions=UserData['file_perm']
file_permitions=True
if file_permitions:
	print('you have File permitions that means you can edit and create files')
else:
	print('you do not have File permitions that means you can not edit and create files')
def update_files():
	from os import listdir
	global files
	if __name__=='__main__':
		files=listdir('./files')
	else:
		files=listdir('./files')
	del listdir

def show_files():
	update_files()
	for i in enumerate(files):
		print(f"{i[0]}: {i[1]}")
	while True:
		try:
			userin=int(input('enter index of file: '))
			break
		except:
			print("not a vailid int")
	return f'./files/{files[userin]}'
def view_file(file_path):
	with open(file_path,'r') as f:
		x=f.read()
	print(x)
def run():
	view_file(show_files())
if __name__=='__main__':
	run()