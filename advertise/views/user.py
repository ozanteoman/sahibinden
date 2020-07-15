from django.shortcuts import render


def retrieve(request):
    return render(request, 'user/retrieve.html', context={})
