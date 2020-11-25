from django.shortcuts import render
import random


def home(request):
    lotto_list = []
    for i in range(0, 5):
        lotto_number = random.sample(range(1, 46), 6)
        lotto_number.sort()
        lotto_list.append(lotto_number)
    return render(
        request,
        'lotto/home.html',
        context={
            "lotto_list": lotto_list,
        }
    )
