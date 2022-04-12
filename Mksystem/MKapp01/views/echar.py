import json

from django.shortcuts import *
from django.http import JsonResponse
from MKapp01 import models
from MKapp01.utils.pagingtion import Pagingtion
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def chart_list(request):
    return render(request, 'dataechar.html')


@csrf_exempt
def chart_bar(request):
    data_dict = {}
    search_data = request.GET.get('search')
    if not search_data:
        return render(request, 'dataechar.html')
    data_dict['title__iregex'] = search_data
    queryset = models.c_data.objects.filter(**data_dict).order_by('-mark')
    title = [ti.title for ti in queryset]
    mark = [ti.mark for ti in queryset]
    people = [ti.people for ti in queryset]
    dict = {}
    with open('./chart_data.txt', mode='w', encoding='utf-8')as f:
        data_title = title
        data_mark = mark
        data_people = people
        dict = {
            'data_title': data_title,
            'data_mark': data_mark,
            'data_people': data_people}
        dict = json.dumps(dict)
        f.write(dict)
    xAxis = title
    series_list = [
        {
            'name': '评分',
            'type': 'bar',
            'data': mark
        },
        {
            'name': '人数',
            'type': 'bar',
            'data': people
        }
    ]
    result = {
        'status': True,
        'data': {
            'legent': ['评分', '人数'],
            'xAxis': xAxis,
            'series_list': series_list,
        }
    }
    return JsonResponse(result)


def chart_change(request):
    with open('./chart_data.txt', mode='r', encoding='utf-8')as f:
        f = json.loads(f.read())
    title = f['data_title']
    mark = f['data_mark']
    people = f['data_people']
    xAxis = title
    series_list = [
        {
            'name': '评分',
            'type': 'bar',
            'data': mark
        },
        {
            'name': '人数',
            'type': 'bar',
            'data': people
        }
    ]
    result = {
        'status': True,
        'data': {
            'legent': ['评分', '人数'],
            'xAxis': xAxis,
            'series_list': series_list,
        }
    }
    return JsonResponse(result)
