from django.shortcuts import render
from .models import Post

posts = [
    {
        'catname': 'Samsung',
        'catcontact': 'MOBILE: 24 HOURS, 7 DAYS A WEEK'
    },
    {
        'catname': 'Toshiba ',
        'catcontact': 'call 1-800-GO-TOSHIBA (1-800-468-6744)'
    },
    {
        'catname': 'Panasonic',
        'catcontact': 'Be the first to know about new products, promotions, technology and more!'
    },


]
def home(request):
    context = {'title': 'category',
               'posts': Post.objects.all()

               }
    return render(request, 'cat/index.html', context)
