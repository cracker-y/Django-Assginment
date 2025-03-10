from django.shortcuts import render, get_object_or_404
from django.http import Http404
from todo.models import TodoList


def todo_list(request):
    ctodo_list = TodoList.objects.all().values_list('id', 'title')
    result = [{'id': todo[0], 'title': todo[1]} for todo in ctodo_list]
    context = {'data': result}
    return render(request, 'ctodo_list.html', context)


def todo_info(request, todo_id):
    ctodo_info = get_object_or_404(TodoList, id=todo_id)
    info = {
        '제목': ctodo_info.title,
        '설명': ctodo_info.description,
        '시작일': ctodo_info.start_date,
        '마감일': ctodo_info.end_date,
        '완료 여부': ctodo_info.is_completed,

    }
    context = {'data': info}
    return render(request, 'ctodo_info.html', context)
