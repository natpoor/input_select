def choose_cat():
	chosen = False

	print 'Which category?'
	print '  1. Film'
	print '  2. Music'
	print '  3. Publishing'
	print '  4. Games'
	print '  0. To just end the program.\n'

	while not chosen:
		the_choice = raw_input('Enter number of your choice: ')
		chosen = True
		if the_choice == '1':
			print 'You selected FILM.'
			the_cat = 'film'
		elif the_choice == '2':
			print 'You selected MUSIC.'
			the_cat = 'music'
		elif the_choice == '3':
			print 'You selected PUBLISHING.'
			the_cat = 'publishing'
		elif the_choice == '4':
			print 'You selected GAMES.'
			the_cat = 'games'
		elif the_choice == '0':
			the_cat = 'none'
		else:
			print 'Very funny that was not a valid input, try again plz.'
			chosen = False

	return the_cat
# End of choose_cat
