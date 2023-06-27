from django.shortcuts import render, get_object_or_404
from .models import Student
from .forms import ContatoForm

def index(request):
    students = Student.objects.all()
    context = { "students": students }
    return render(request, 'index.html', context)

def matricula(request, id):
    student = get_object_or_404(Student, pk=1)
    context = { "student": student }
    return render(request, 'matricula.html', context)

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)

        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            print(("#==" * 7) + "#" + (7 * "==#"))
            print(f'\tNome Completo: {full_name}')
            print(f'\tEmail: {email}')
            print(f'\tMessage: {message}')
            print(("##==" * 5) + "###" + (5 * "==##"))
    else:
        form = ContatoForm()

    context = { "form": form }
    return render(request, 'contato.html', context)