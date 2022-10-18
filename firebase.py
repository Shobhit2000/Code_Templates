from firebase import firebase
firebase = firebase.FirebaseApplication('https://xxxxx.firebaseio.com/', None)

data = {'Name': 'Vivek',
        'RollNo': 1,
        'Percentage': 76.02
        }
result = firebase.post('/python-sample-ed7f7/Students/', data)
print(result)

firebase.put('/python-sample-ed7f7/Students/-LAgstkF0DT5l0IRucvm',
             'Percentage', 79)
print('updated')

firebase.delete('/python-sample-ed7f7/Students/', '-LAgt5rGRlPovwNhOsWK')
print('deleted')
