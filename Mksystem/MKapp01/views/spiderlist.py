from django.shortcuts import render

# Create your views here.
from MKapp01 import models
from MKapp01.utils.pagingtion import Pagingtion


def spiderlist(request):
    data_dict = {}
    search_data = request.GET.get('search', '')
    if search_data:
        data_dict['title__iregex'] = search_data
    queryset = models.c_data.objects.filter(**data_dict).order_by('-mark')
    page_objecct = Pagingtion(request, queryset, page_size=10)
    context = {
        'queryset': page_objecct.page_queryset,
        'page_string': page_objecct.html()
    }
    return render(request, 'spiderlist.html', context)
