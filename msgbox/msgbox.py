import pymsgbox, sys

adult = pymsgbox.confirm('Are you above 18 years of age?', 'Age', ['Yes', 'No'])
if adult == 'No':
    sys.exit()

name = pymsgbox.prompt('Enter your name', 'Name')
username = pymsgbox.prompt('Pick a username', 'Username')
password = pymsgbox.password('Enter a password: ', 'Password')
user_info = [name, username, password]
pymsgbox.alert(user_info, 'User info')