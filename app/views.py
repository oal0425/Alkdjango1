from django.http import HttpResponse
#from PersonFrom import



def index(request):
    return HttpResponse("<h1> PAGINA PRINCIPAL </h1>")


def home(request):
    return HttpResponse("<h1> HOLA MUNDITO </h1>")


"""
class PersonForm(ModelForm):
    
    class Meta:
        model = Person
        fields = ['firstname','lastname','birth']
        labels = {
            'firstname': 'Ingrese el nombre'
        }
        

class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = ['firstname', 'lastname', 'birth']
        labels = {
            'firstname': 'Ingrese el nombre'
        }


def form(request):
    if request.method == "POST":
        name = request.POST.get("name")

    return render(request, 'form.html')
    
    
    
    
    
    
otro ejemplo
def form(request):
    return render(request, 'form.html')


def form_submitted(request):
    name = request.POST.get("name")
    return HttpResponse(f"Nombre: {name}")


def person_create(request):
    form = PersonForm()
    if request.method = 'POST':
        
    return render(request, 'create_update_form
    
def person_delete(request, person_id):
    person = Person.objects.filter(id=person_id)


if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person-all')

"""