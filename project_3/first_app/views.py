from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author': 'Rahim', 'age': 5 , 'list' : ['python','is','best'],'birthday' : datetime.datetime.now(), 'val': 'amar sonar bangla', 'courses': [
        {
            'id': 1,
            'name':' pyhton',
            'Fee' : 5000,
        },
                {
            'id': 2,
            'name': 'java',
            'Fee' : 3000,
        },
                {
            'id': 3,
            'name': 'C++',
            'Fee' : 4000,
        },
    ]}
    return render(request,'home.html', d)