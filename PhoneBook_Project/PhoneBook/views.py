from django.http import HttpResponse
from django.template import loader
from .models import Book

# Create your views here.
# index Page
def index(request):
  phoneBooks = Book.objects.all().values()
  template = loader.get_template('index.html')
  contex = {
    'PhoneBooks': phoneBooks,
  }
  return HttpResponse(template.render(contex,request))
