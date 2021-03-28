import time
def recom():
	firstq = input("Ваше имя: ")
	secondq = input(firstq + ", какая у Вас игровая платформа (ПК, PS, Xbox, Nintendo): ")
	thirdq = input("Ваш любимый жанр игр (РПГ, Платформеры, Шутеры): ")
	if secondq == "ПК":
		fourthq = input("У Вас производительный ПК (Д/Н): ")
		if thirdq == "РПГ":
			if fourthq == "Д":
				print("Советчик говорит:")
				print("-Советую Ведьмака, Skyrim, Cyberpunk 2077. Не благодарите, " + firstq)
				time.sleep(15)
			elif fourthq == "Н":
				print("Советчик говорит:")
				print("-Советую первого Ведьмака, старый Fallout, Warcraft. Не благодарите, " + firstq)
				time.sleep(15)
		if thirdq == "Платформеры":
			print("Советчик говорит:")
			print("-Советую Limbo, Inside, Ori and the Blind Forest. Не благодарите, " + firstq)
			time.sleep(15)
		elif thirdq == "Шутеры":
			if fourthq == "Н":
				print("Советчик говорит:")
				print("-Советую Bioshock 2007 года, первый FarCry, Sniper Elite V2. Не благодарите, " + firstq)
				time.sleep(15)
			elif fourthq == "Д":
				print("Советчик говорит:")
				print("-Советую FarCry 5, Wolfenstein ||, Battlefield V. Не благодарите, " + firstq)
				time.sleep(15)
		else:
			print("Видимо я не знаю этот жанр, либо Вы написали с ошибкой. Простите если я не знаю этот жанр, я молодая программа ;)")
			time.sleep(15)
	if secondq == "PS":
		thirdq = input("Ваш любимый жанр игр (РПГ, Платформеры, Шутеры): ")
		if thirdq == "РПГ":
			print("Советчик говорит:")
			print("-Советую Bloodborne, Horizon Zero Dawn, Cyberpunk 2077. Не благодарите, " + firstq)
			time.sleep(15)
		if thirdq == "Платформеры":
			print("Советчик говорит:")
			print("-Советую LittleBigPlanet 3, Little Nightmares, Unravel. Не благодарите, " + firstq)
			time.sleep(15)
		elif thirdq == "Шутеры":
			print("Советчик говорит: ")
			print("-Советую Far Cry 5, Battlefield 4, Overwatch. Не благодарите, " + firstq)
			time.sleep(15)
		else:
			print("Видимо я не знаю этот жанр, либо Вы написали с ошибкой. Простите если я не знаю этот жанр, я молодая программа ;)")
	elif secondq == "Xbox":
		if thirdq == "РПГ":
			print("Советчик говорит:")
			print("-Советую Ведьмака, Diablo |||, Cyberpunk 2077. Не благодарите, " + firstq)
			time.sleep(15)
		if thirdq == "Платформеры":
			print("Советчик говорит:")
			print("-Советую Batman: Arkham City, Inside, Unravel. Не благодарите, " + firstq)
			time.sleep(15)
		elif thirdq == "Шутеры":
			print("Советчик говорит: ")
			print("-Советую Far Cry 5, Battlefield 4, Metro. Не благодарите, " + firstq)
			time.sleep(15)
		else:
			print("Видимо я не знаю этот жанр, либо Вы написали с ошибкой. Простите если я не знаю этот жанр, я молодая программа ;)")
			time.sleep(15)
	elif secondq == "Nintendo":
		if thirdq == "РПГ":
			print("Советчик говорит:")
			print("-Советую Zelda, Diablo |||, Xenoblade Chronicles. Не благодарите, " + firstq)
			time.sleep(15)
		if thirdq == "Платформеры":
			print("Советчик говорит:")
			print("-Советую Super Mario 3D World, Inside, Super Mario Odyssey. Не благодарите, " + firstq)
			time.sleep(15)
		elif thirdq == "Шутеры":
			print("Советчик говорит: ")
			print("-Советую Metro, Doom Enternal, Fortnite. Не благодарите, " + firstq)
			time.sleep(15)
		else:
			print("Видимо я не знаю этот жанр, либо Вы написали с ошибкой. Простите если я не знаю этот жанр, я молодая программа ;)")
	print("Спасибо за использование :)")
	time.sleep(5)
recom()
