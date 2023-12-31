import os
from Packages.getUnsplImg import *

class Config:
	db = 'lastRun=None\n'
	
	def searchQuery(self, src = []):
		search = input('Enter your search query: ').strip()
		print("Verifying for results...\n")
		results = getLinks(search, 1)
		if results == None:
			return 'err'
		else:
			inp = input(f"Found \u001b[32m{results}\u001b[0m results. Would you like to \u001b[33m1) proceed\u001b[0m, \u001b[33m2) to use another query (and to cancel this one, but keep the previous ones)\u001b[0m or \u001b[33m3) to add an additional query\u001b[0m? \u001b[33m(1 / 2 / 3 / any key to start over)\u001b[0m: ").strip()
			if inp == '1': 
				print("Proceeding...\n")
				return src + [search]
			elif inp == '2': return self.searchQuery(src)
			elif inp == '3': return self.searchQuery(src + [search])
			else:
				return 'err'
				
	def config(self, err = 0):
		if err: print("\u001b[31mSomething went wrong, it may be because you entered something wrong... Please try again.\u001b[0m\n")
		query = input("You can choose from the following options. Get wallpaper based on...\n\u001b[34m1) The season.\n2) Your search query.\n3) Unsplash trending.\u001b[0m\nYour choice: ").strip()
		self.db = 'lastRun=None\n'
		if not query in ('1', '2', '3'): self.config(1)
		self.db += 'option=' + query + '\n'
		if query == '2':
			sq = self.searchQuery()
			if sq == 'err':
				self.config(1)
				return
			else:
				self.db += 'search=' + str(sq) + '\n'
		time = input("How often do you want your wallpapers to change?\n\u001b[37m1) On every log in\u001b[0m\n\u001b[36m2) Daily\u001b[0m\n\u001b[34m3) Weekly\u001b[0m\n\u001b[30m4) When season changes\u001b[0m\nYour choice: ").strip()
		if not time in ('1', '2', '3', '4'):
			self.config(1)
			return
		self.db += 'time=' + time + '\n'
		inp = input(f"This is the chosen data:\n{self.db}\nIf you choose to proceed it would be written into database, otherwise we'll start the configuration over again. Proceed? (Y/N): ").strip().lower()
		if inp == 'y': print("Proceeding...\n")
		elif inp == 'n':
			self.config()
			return
		else:
			self.config(1)
			return
		self.db += """###########################################################
	# Be careful! Editing this can lead to unexpected errors! #
	# Syntax:  (Suggest - run client.py, it'll edit it for u) #
	# option=1|2|3                                            #
	# search=STRING       - Only if the option is 2           #
	# time=1|2|3|4                                            #
	#                                                         #
	# Values for option: Get wallpaper based on...            #
	# 1 - The season.                                         #
	# 2 - Your search query.                                  #
	# 3 - Unsplash trending.                                  #
	#                                                         #
	# Values for time: How often do you want your wallpapers  #
	# to change?                                              #
	# 1 - On every log in                                     #
	# 2 - Daily                                               #
	# 3 - Weekly                                              #
	# 4 - When season changes                                 #
	###########################################################"""
		with open("db.txt", 'w') as f:
			f.write(self.db)

def readConfig(home):
	with open(f"{home}/.WallpaperCh/db.txt", "r") as f:
		db = f.read().split('\n')
	print('\n'.join(db[:db.index('###########################################################')]))

config = Config().config
home = os.path.expanduser('~')
if os.path.exists(f'{home}/.WallpaperCh/'):
	op = input("Do you want to \u001b[31mdelete the app (1)\u001b[0m, to \u001b[32mchange it's configuration (2)\u001b[0m or \u001b[33msee it's configuration (3)\u001b[0m? (1 / 2 / 3): ")
	if not op in ('1', '2', '3'):
		print("\u001b[31mEntered wrong symbol. Please try again.\u001b[0m")
		quit()
	if op == '1': import remove
	elif op == '2': config()
	else: readConfig(home)
elif input("\u001b[32mDo you want to install the app?\u001b[0m \u001b[33m(Y/N)\u001b[0m: ").strip().lower() == "y":
	config()
	autostart = f'''[Desktop Entry]
	Type=Application
	Exec=/usr/bin/python3 {home}/.WallpaperCh/main.py
	Hidden=false
	NoDisplay=false
	X-GNOME-Autostart-enabled=true
	Name[en_US]=Wallpaper Changer
	Name=Wallpaper Changer
	Comment[en_US]=Changes your wallpaper everytime according to your needs. To change options just run "python3 ~/WallpaperCh/client.py" and choose the desired option.
	Comment=Changes your wallpaper everytime according to your needs. To change options just run "python3 ~/.WallpaperCh/client.py" and choose the desired option. To properly delete the app run: "python3 ~/.WallpaperCh/remove.py".'''

	with open(f"{home}/.config/autostart/wpch.desktop", "w") as f:
		f.write(autostart)
	commands = [f"mkdir {home}/.WallpaperCh", f'cp ./* {home}/.WallpaperCh -r']
	for i in commands: os.system(i)
	print("\u001b[32mDone. You can delete this folder as the app was installed successfully!\u001b[0m")
