import os
try:
	import time
except:
	print("Установка модулей(1/4)")
	os.system("pip3 install time")
	os.sytem("clear")
try:
	import random
except:
	print("Установка модулей(2/4)")
	os.system("pip3 install random")
	os.sytem("clear")
try:
	import string
except:
	print("Установка модулей(3/4)")
	os.system("pip3 install string")
	os.sytem("clear")
try:
	import discord
except:
		print("Установка модулей(4/4)")
		os.system("pip3 install discord")
		os.system("clear")
from discord.ext import commands
functionList=" Discord Framework\nᛁ------------------ᛁ\nФункции:\n[1] Token Checker\n[2] Password Generator\n[Help] Function List\n[Dev] Dev Information\nᛁ------------------ᛁ"
print(f"{functionList}")
while True:
		function=input("Введите номер функции: ")
		if function=="1":
			token=input("Введите токен: ")
			if token=="":
				print("Укажите токен!")
			else:
					os.system("clear")
					bot=commands.Bot(command_prefix="df")
					bot.remove_command("help")
					@bot.event
					async def on_ready():
						print(f"Токен является ботом: {bot.user.name}#{bot.user.discriminator}")
						await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,name="Discord Framework"), status=discord.Status.online)
					bot.run(f"{token}")
		elif function=="2":
				os.system("clear")
				print("Начинаем генерацию discord паролей!")
				while True:
					time.sleep(1)
					print("".join(random.choice(string.ascii_letters + string.digits) for _ in range(8)))
		elif function=="Help":
			print(f"{functionList}")
		elif function=="Dev":
			print(" Discord Framework\nᛁ------------------ᛁ\nСоздан: 05.03.2021\nСоздатель: Harikso\nВерсия: 0.0.4.beta\nЛицензия: GPL-3.0\nᛁ------------------ᛁ")