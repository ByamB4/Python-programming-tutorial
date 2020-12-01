name = 'ByamB4'
logged_in = False

if not logged_in:
    print('Please login first')

elif logged_in and name == 'admin':
    print('Welcome Admin')

elif logged_in and name != 'admin':
    print(f'Welcome {name}')

else:
    print('Something is wrong')
