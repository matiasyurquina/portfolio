from django.shortcuts import render, redirect, HttpResponse
from django.utils.translation import activate

from django.shortcuts import render
from contact_app.forms import contact_form


def home(request):
    lang='en'
    activate(lang)
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'base.html' , {'msg':'Message was sent successfully!'})
        
    else:
        form = contact_form()

    return render (request, 'base.html', {'lang': lang, 'form': form} )

def homeES(request):
    lang='es'
    activate(lang)
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'base.html' , {'msg':'Mensaje enviado correctamente!'})
    else:
        form = contact_form()

    return render (request, 'base.html', {'lang': lang, 'form': form} )

def homePT(request):
    lang='pt'
    activate(lang)
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'base.html' , {'msg':'Mensagem enviada com sucesso!'})
    else:
        form = contact_form()

    return render (request, 'base.html', {'lang': lang, 'form': form} )

def contact(request):
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Redirige a una página exitosa si el formulario es valido
    else:
        form = contact_form()

    return render(request, 'contact.html', {'form': form})

def error_404(request, exception):

    return redirect('home')

def error_500(request):
    return render(request, '500.html', status=500)
