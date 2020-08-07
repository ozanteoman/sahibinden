from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods

from advertise.forms import UpdateUserForm
from advertise.models import User


@require_http_methods(["GET", "POST"])
def edit_user(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == "POST":
        form = UpdateUserForm(instance=user, data=request.POST or None)
        if form.is_valid():
            user = form.save(commit=True)
            user_retrieve = render_to_string('user/includes/retrieve.html', context=user.info, request=request)
            return JsonResponse(data={'user_retrieve': user_retrieve})

    form = UpdateUserForm(instance=user)
    string_form = render_to_string('user/includes/edit-form.html', context={'form': form}, request=request)
    return JsonResponse(data={'string_form': string_form})


@require_http_methods(["GET"])
def retrieve(request, username):
    users = User.objects.prefetch_related('interests')
    user = get_object_or_404(users, username=username)

    if request.is_ajax():
        user_retrieve = render_to_string('user/includes/retrieve.html', context=user.info, request=request)
        return JsonResponse(data={'user_retrieve': user_retrieve})

    return render(request, 'user/retrieve.html', context=user.info)
