from django.shortcuts import render, get_object_or_404

from advertise.models import User


def retrieve(request, username):
    users = User.objects.prefetch_related('interests')
    user = get_object_or_404(users, username=username)

    full_name = user.get_full_name() or "-"
    birthday = user.birthday or "-"
    gender = user.get_gender_display() or "-"
    marital_status = user.get_marital_status_display() or "-"
    educational_status = user.get_educational_status_display() or "-"
    profession = user.get_profession_display() or "-"
    interests = ", ".join([interest.name for interest in user.interests.all()]) or "-"
    phone_number = user.phone_number or "-"

    context = {
        'username': user.username,
        'full_name': full_name,
        'birthday': birthday,
        'gender': gender,
        'marital_status': marital_status,
        'educational_status': educational_status,
        'profession': profession,
        'interests': interests,
        'phone_number': phone_number
    }

    return render(request, 'user/retrieve.html', context=context)
