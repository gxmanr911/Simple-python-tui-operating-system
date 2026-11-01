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
	f=run_path(file_path,run_name='__main__')
	del run_path
app_selection()
print("back to OS")