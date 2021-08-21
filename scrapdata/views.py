from django.shortcuts import render
from .models import products
from .forms import ProductForm

def product_data(request):
	form = ProductForm(request.GET)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context = {
		'form' : form
	}
	return render(request, "datadump.html",context)


def search(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            name= Q(title__icontains=query) | Q(content__icontains=query)

            results= Post.objects.filter(name).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')