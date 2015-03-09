#! -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from models import Computer
from models import Message
from forms import MessageForm

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
# from django.core.mail import send_mail
# from django.conf import settings
# from django.core.mail import EmailMessage
# from django.template import Context
# from django.template.loader import render_to_string, get_template
from django.contrib import messages
# from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

import random


def index(request):

    responseContext = {'lang':request.LANGUAGE_CODE,}
    return render(request, 'moneymany/index.html',responseContext)

def joinnow(request):
    return render(request, 'moneymany/joinnow.html')

def result(request):
    return render(request, 'moneymany/result.html')




def computer(request):
    result =  Computer.objects.order_by('?')[:1]
    for r in result:
        print r.name
        request.session['name'] =r.name
        request.session['image'] =r.image_urls
    return redirect('moneymany:result' )
    # return HttpResponseRedirect(reverse('moneymany:result', args=(result,)))
    # return render(request, 'moneymany/result.html',{'result':result})
    #如果用render to response 圖片的路徑會錯誤，他會從現在的位置去找圖而不是從static url去找



def create_post(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.ip = request.META['REMOTE_ADDR']
            obj.save()

            # #寄信給管理員
            # subject = "有人跟你說Hi"
            # to =['xxx@gmail.tw']
            # from_email = settings.EMAIL_HOST_USER
            # #讀取寄信的模板
            # ctx = { 'name': obj.name ,'email':obj.email,'message':obj.message}
            # message = get_template('email.html').render(Context(ctx))
            # msg = EmailMessage(subject, message, to=to, from_email=from_email)
            # msg.content_subtype = 'html'
            # msg.send()

            messages.success(request,'留言成功')
            return HttpResponseRedirect('/')
            # return redirect(reverse("maininfo"), {"alert":'留言成功'})
        return render(request, "moneymany/index.html",{'form': form,'anchor':'#contact'})





# randomPhotos = [random.choice(Computer.name.objects.all()) for name in Computer.objects.all()]
# albumObj.random_photo()


