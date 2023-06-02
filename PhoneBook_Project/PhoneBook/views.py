''' Import section '''
from django.http import HttpResponse
from django.template import loader
from .models import Book

# Create your views here.
# index Page
def index(request):
    '''
    first page of phone book, index view
    '''
    phone_books = Book.objects.all().values()
    template = loader.get_template('phonebook.html')
    contex = {
      'PhoneBooks': phone_books,
    }
    return HttpResponse(template.render(contex,request))
