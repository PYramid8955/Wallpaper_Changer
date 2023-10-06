import os
import shutil
if input("\u001b[31mYou are sure that you want to delete Wallpaper_Changer?\u001b[0m \u001b[33m(Y/N)\u001b[0m: ").strip().lower() == "y":
	home = os.path.expanduser('~')
	os.remove(f"{home}/.config/autostart/wpch.desktop")
	shutil.rmtree(f"{home}/.WallpaperCh")
	print("\nDone! Wallpaper_Changer was successfully deleted from your system. If you change your mind you can download it at any time at https://github.com/PYramid8955/Wallpaper_Changer .")
	quit()
