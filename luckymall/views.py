from django.shortcuts import render



def luckymall(request):
    return render(request, 'luckymall/lucky.html')
