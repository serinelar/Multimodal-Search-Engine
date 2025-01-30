from django.shortcuts import render   
from django.db.models import Q                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
from .forms import SearchForm
from .models import SearchItem
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

def home(request):
    return HttpResponse("Welcome to the Multimodal Search App!")

def search(request):
    results = []
    query = None
    data_type = None

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            data_type = form.cleaned_data['data_type']

            # Base query
            results = SearchItem.objects.all()

            # Apply search query
            if query:
                results = results.filter(
                    Q(title__icontains=query) | Q(description__icontains=query)
                )

            # Apply data type filter
            if data_type and data_type != 'all':
                if data_type == 'text_content':
                    # Filter for non-empty text_content
                    results = results.filter(text_content__isnull=False)
                else:
                    # Filter for non-empty image, audio, or video
                    results = results.filter(**{f"{data_type}__isnull": False})

            # Paginate results
            paginator = Paginator(results, 10)  # Show 10 results per page
            page_number = request.GET.get('page')
            results = paginator.get_page(page_number)
    else:
        form = SearchForm()

    return render(request, 'search/search.html', {
        'form': form,
        'query': query,
        'data_type': data_type,
        'results': results,
    })

def detail(request, item_id):
    item = get_object_or_404(SearchItem, id=item_id)
    return render(request, 'search/detail.html', {'item': item})