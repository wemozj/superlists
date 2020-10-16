from django.shortcuts import render

# Create your views here.
def home_page(request):
    content = {
        'new_item_text' : request.POST.get('item_text', ''),
    }

    return render(request, 'home.html', context=content)
