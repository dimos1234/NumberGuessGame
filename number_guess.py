import random

def algorithm(user,guess):
	
	num=0

	if user.split()[-1]=='h':
		numlis=[12]
		while True:
			num=random.randint(guess+1,25)
			if num in numlis:
				continue
			else:
				numlis.append(num)
				break
		print(f'\n\ni guess {num}')
		return num
	elif user.split()[-1]=='l':
		numlis=[12]
		while True:
			num=random.randint(1,guess-1)
			if num in numlis:
				continue
			else:
				numlis.append(num)
				break
		print(f'\n\ni guess {num}')
		return num
	elif user.split()[-1] in ['y','w','c']:
		print(f'\n\nhaha! the number was {guess}')
		return False

def guessing():
	while True:
		try:
			guess=input('shold i go lower (l), higher (h), or did i win (w)?\n')
		except:
			continue
		else:
			if not(guess.split()[-1][0] in ['h','H','l','L','y','w','c']):
				continue
			else:
				break
	return guess



if __name__=='__main__':
	print('\nwelcome to guess 2!\n')

	while True:
		game=input('please think of a number between 1 and 25!\nwhen you are ready, type yes!\n')
		if game[0] in ['y','Y']:
			break
		else:
			print('not ready yet? do not worry, im not going anywhere!\n')
			continue
	print('\n\ni guess 12\n')
	playing=12
	guesses=0
	while True:
		guess=guessing()
		playing=algorithm(guess,playing)
		guesses+=1
		if playing==False:
			break
	print('\n\nthanks for playing!')
	print(f'it took me {guesses} guesses!')
