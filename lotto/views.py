from django.shortcuts import render
import random
# Create your views here.

number = int(input())

for idx in range(number):
    lotto_number = random.sample(range(1, 46), 6)
    lotto_number.sort()
    print("["+str((idx+1))+"번째"+"]", lotto_number)


def home(request):
    return render(request, 'lotto/home.html', lotto_number)
