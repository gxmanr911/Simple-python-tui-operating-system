from main import file_permisons
import user_handling
with open('args.txt','r') as f:
	if f.read()=='True':
		file_permitions=True
	else:
		file_permitions=False
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
	print('0: exit')
	for i in enumerate(files):
		print(f"{i[0]+1}: {i[1]}")
	while True:
		try:
			userin=int(input('enter index of file: '))
			break
		except:
			print("not a vailid int")
	if userin!=0:
	    return f'./files/{files[userin-1]}'
	else:
	    return False
def view_file(file_path):
	with open(file_path,'r') as f:
		x=f.read()
	print(x)
	if file_permitions:
		print('what would you like to do with the file')
		userin=input("""[D]elete: """)
		if userin.upper()=='D':
			from os import remove
			remove(file_path)
			del remove
def check_file_exists(file_path):
    try:
        with open(file_path,'r') as x:
            pass
        return True
    except:
        return False
def run():
    while True:
        x=show_files()
        if x!=False:
            view_file(x)
        else:
            break
if __name__=='__main__':
	run()
