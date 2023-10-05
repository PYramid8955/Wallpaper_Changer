'''from Packages.getUnsplImg import *


		
		with open('db', 'r+') as f:
            search_query = f.read().strip()
            if not search_query:
                search_query = input("Enter search query: ")
                f.write(search_query)
                
                
                
                
                
                
                
'''
import os

home = os.path.expanduser('~')
autostart = f'''[Desktop Entry]
Type=Application
Exec=python3 {home}/WallpaperCh/main.py
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=Wallpaper Changer
Name=Wallpaper Changer
Comment[en_US]=Changes your wallpaper everytime according to your needs. To change options just run "python3 ~/WallpaperCh/client.py" and choose the desired option.
Comment=Changes your wallpaper everytime according to your needs. To change options just run "python3 ~/WallpaperCh/client.py" and choose the desired option. To properly delete the app run: "python3 ~/WallpaperCh/remove.py".'''

with open(f"{home}/.config/autostart/wpch.desktop", "w") as f:
	f.write(autostart)
commands = [f"mkdir {home}/.WallpaperCh", f'cp ./* {home}/.WallpaperCh -r']
for i in commands: os.system(i)
print("Done.")
