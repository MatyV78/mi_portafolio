from django.shortcuts import render, redirect, get_object_or_404
from Proyecto_Vehiculos.forms import VehiculoForm, Vehiculo, VehiculoElecForm, VehiculoUsadoForm, MarcaForm, ModeloForm, ComentarioForm, ComentarioUsoForm, ComentarioElecForm
from Proyecto_Vehiculos.models import VehiculoElec, VehiculoUsado, Vehiculo, Marca, Modelo, Comentario, ComentarioUso, ComentarioElec
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required 

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.




#Login

def signup(request):
    if request.method == 'GET':
        return render(request, 'login/signup.html', {'form': UserCreationForm()})
    else:
        form = UserCreationForm(request.POST) # Crea el formulario con los datos POST
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login/signup.html', {'form': form, 'error': 'Por favor, corrige los errores.'})

def user_logout(request):
    logout(request)
    return redirect('login')



@login_required
def home(request):
    return render(request, 'home.html')


def contacto(request):
    return render(request, 'contacto.html')

@login_required
def add_vehiculo(request):
    return render(request, "add_vehiculo.html")

@login_required
def add_nuevos(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_vNuevos")
    else:
        form = VehiculoForm()
    return render(request, "Agregar/add_nuevos.html", {"form": form})

@login_required
def editar_nuevos(request, id):
    vehiculo = get_object_or_404(Vehiculo, pk=id)
    if request.method == "POST":
        form = VehiculoForm(request.POST, instance= vehiculo)
        if form.is_valid():
            form.save()
            return redirect("lista_vNuevos")
    else:
        form = VehiculoForm(instance= vehiculo)
    return render(request, "Agregar/add_nuevos.html", {"form": form, "vehiculo": Vehiculo})

@login_required
def eliminar_nuevos(request, id):
    vehiculo = get_object_or_404(Vehiculo, pk=id)
    if request.method == "POST":
        vehiculo.delete()
        return redirect("lista_vNuevos")
    return render(request, "conf_elm_nuevo.html", {"vehiculo": vehiculo})

@login_required
def lista_vNuevos(request):    
    vehiculos = Vehiculo.objects.all()
    return render(request, "listados/lista_vNuevos.html", {"vehiculos": vehiculos})


#Vehiculo Electricos

@login_required
def add_elec(request):
    if request.method == "POST":
        form = VehiculoElecForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_vElec")
    else:
        form = VehiculoElecForm()
    return render(request, "Agregar/add_elec.html", {"form": form})

@login_required
def lista_vElec(request):
    vehiculos = VehiculoElec.objects.all()
    return render(request, "listados/lista_vElec.html", {"vehiculos": vehiculos})

@login_required
def eliminar_elec(request, id):
    vehiculo = get_object_or_404(VehiculoElec, pk=id)
    if request.method == "POST":
        vehiculo.delete()
        return redirect("lista_vElec")
    return render(request, "conf_elm_ele.html", {"vehiculo": vehiculo})

@login_required
def editar_elec(request, id):
    vehiculo = get_object_or_404(VehiculoElec, pk=id)
    if request.method == "POST":
        form = VehiculoElecForm(request.POST, instance= vehiculo)
        if form.is_valid():
            form.save()
            return redirect("lista_vElec")
    else:
        form = VehiculoElecForm(instance= vehiculo)
    return render(request, "Agregar/add_elec.html", {"form": form, "vehiculo": VehiculoElec})


#Autos Usados

@login_required
def add_usado(request):
    if request.method == "POST":
        form = VehiculoUsadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_vUsados")
    else:
        form = VehiculoUsadoForm()
    return render(request, "Agregar/add_usados.html", {"form": form})

@login_required
def lista_vUsados(request):    
    vehiculos = VehiculoUsado.objects.all()
    return render(request, "listados/lista_vUsados.html", {"vehiculos": vehiculos})

@login_required
def eliminar_usado(request, id):
    vehiculo = get_object_or_404(VehiculoUsado, pk=id)
    if request.method == "POST":
        vehiculo.delete()
        return redirect("lista_vUsados")
    return render(request, "conf_elm_usado.html", {"vehiculo": vehiculo})

@login_required
def editar_usado(request, id):
    vehiculo = get_object_or_404(VehiculoUsado, pk=id)
    if request.method == "POST":
        form = VehiculoUsadoForm(request.POST, instance= vehiculo)
        if form.is_valid():
            form.save()
            return redirect("lista_vUsados")
    else:
        form = VehiculoUsadoForm(instance= vehiculo)
    return render(request, "Agregar/add_usados.html", {"form": form, "vehiculo": VehiculoUsado})


#Marcas y Modelos

@login_required
def marcas_modelos(request):
    marca = Marca.objects.all()
    return render(request, "marcas_modelos/marcas_modelos.html", {"marca": marca})

@login_required
def agregar_marca(request):
    if request.method == "POST":
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("marcas_modelos")
    else:
        form = MarcaForm()
    return render(request, "marcas_modelos/add_marca.html", {"form": form})

@login_required
def eliminar_marca(request, id):
    marca = get_object_or_404(Marca, pk=id)
    if request.method == "POST":
        marca.delete()
        return redirect("marcas_modelos")
    return render(request, "marcas_modelos/conf_elm_marcas.html", {"marca": marca})

@login_required
def editar_marca(request, id):
    marca = get_object_or_404(Marca, pk=id)
    if request.method == "POST":
        form = MarcaForm(request.POST, instance= marca)
        if form.is_valid():
            form.save()
            return redirect("marcas_modelos")
    else:
        form = MarcaForm(instance= marca)
    return render(request, "marcas_modelos/add_marca.html", {"form": form, "marca": Marca})


######################
@login_required
def lista_modelos(request, marca_id):
    marca = get_object_or_404(Marca, pk=marca_id)
    modelos = marca.modelos.all()
    
    if request.method == "POST":
        form = ModeloForm(request.POST)
        if form.is_valid():
            nuevo_modelo = form.save(commit=False)
            nuevo_modelo.marca = marca
            nuevo_modelo.save()
            return redirect("marcas_modelos", marca_id)
    else:
        form = ModeloForm()
        
    return render(request, "marcas_modelos/lista_modelos.html", {"modelos": modelos, "marca": marca, "form": form})

@login_required
def agregar_modelo(request):
    if request.method == "POST":
        form = ModeloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("marcas_modelos")
    else:
        form = ModeloForm()
    return render(request, "marcas_modelos/add_modelos.html", {"form": form})

@login_required
def eliminar_modelo(request, id):
    modelo = get_object_or_404(Modelo, pk=id)
    if request.method == "POST":
        modelo.delete()
        return redirect("marcas_modelos")
    return render(request, "marcas_modelos/conf_elm_modelo.html", {"modelo": modelo})

@login_required
def editar_modelo(request, id):
    modelo = get_object_or_404(Modelo, pk=id)
    if request.method == "POST":
        form = ModeloForm(request.POST, instance= modelo)
        if form.is_valid():
            form.save()
            return redirect("marcas_modelos")
    else:
        form = ModeloForm(instance= modelo)
    return render(request, "marcas_modelos/add_modelos.html", {"form": form, "modelo": Modelo})



# Comentarios de Vehiculo Nuevos ########

def ver_comentarios(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    comentarios = vehiculo.comentarios.all().order_by('-fecha') 

    return render(request, 'comentarios/ver_comentarios.html', {
        'vehiculo': vehiculo,
        'comentarios': comentarios
    })
    
    
def agregar_comentario(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.vehiculo = vehiculo
            comentario.save()
            return redirect('ver_comentarios', vehiculo_id=vehiculo.id)
    else:
        form = ComentarioForm()

    return render(request, 'comentarios/agregar_comentario.html', {
        'vehiculo': vehiculo,
        'form': form
    })
    
    
def editar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    vehiculo_id = comentario.vehiculo.id  # guardamos antes para el redirect

    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('ver_comentarios', vehiculo_id=vehiculo_id)
    else:
        form = ComentarioForm(instance=comentario)

    return render(request, 'comentarios/agregar_comentario.html', {'vehiculo': comentario.vehiculo,'form': form,'comentario': comentario})


 
def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    vehiculo_id = comentario.vehiculo.id

    if request.method == 'POST':
        comentario.delete()
        return redirect('ver_comentarios', vehiculo_id=vehiculo_id)

    return render(request, 'comentarios/eliminar_comentario.html', {'comentario': comentario})



# Comentarios de Vehiculo Usado ######

def ver_comentarios_usados(request, vehiculo_id):
    vehiculo = get_object_or_404(VehiculoUsado, id=vehiculo_id)
    comentarios_usados = vehiculo.comentarios.all().order_by('-fecha') 

    return render(request, 'comentarios/ver_comen_usados.html', {
        'vehiculo': vehiculo,
        'comentarios_usados': comentarios_usados
    })
    
def agregar_comentario_usados(request, vehiculo_id):   
    vehiculo = get_object_or_404(VehiculoUsado, id=vehiculo_id)
    
    if request.method == 'POST':
        form = ComentarioUsoForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.vehiculo = get_object_or_404(VehiculoUsado, id=vehiculo_id)
            comentario.save()
            return redirect('ver_comentarios_usados', vehiculo_id=comentario.vehiculo.id)
    else:
        form = ComentarioUsoForm()

    return render(request, 'comentarios/agregar_comen_usado.html', {
        'vehiculo': vehiculo,
        'form': form
    })

  
def eliminar_comentario_usados(request, comentario_id):
    comentario = get_object_or_404(ComentarioUso, id=comentario_id)
    vehiculo_id = comentario.vehiculo.id

    if request.method == 'POST':
        comentario.delete()
        return redirect('ver_comentarios_usados', vehiculo_id=vehiculo_id)

    return render(request, 'comentarios/eliminar_comen_usado.html', {'comentario': comentario})


def editar_comentario_usados(request, comentario_id):
    comentario = get_object_or_404(ComentarioUso, pk=comentario_id)
    vehiculo_id = comentario.vehiculo.id  # guardamos antes para el redirect

    if request.method == 'POST':
        form = ComentarioUsoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('ver_comentarios_usados', vehiculo_id=vehiculo_id)
    else:
        form = ComentarioUsoForm(instance=comentario)

    return render(request, 'comentarios/agregar_comentario.html', {'vehiculo': comentario.vehiculo,'form': form,'comentario': comentario})



# Comentarios de Vehiculo Electricos ######

def ver_comentarios_elec(request, vehiculo_id):
    vehiculo = get_object_or_404(VehiculoElec, id=vehiculo_id)
    comentarios_elec = vehiculo.comentarios.all().order_by('-fecha') 

    return render(request, 'comentarios/ver_comen_ele.html', {
        'vehiculo': vehiculo,
        'comentarios_elec': comentarios_elec
    })


def agregar_comentario_elec(request, vehiculo_id):
    vehiculo = get_object_or_404(VehiculoElec, id=vehiculo_id)

    if request.method == 'POST':
        form = ComentarioElecForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.vehiculo = vehiculo
            comentario.save()
            return redirect('ver_comentarios_elec', vehiculo_id=vehiculo_id)
    else:
        form = ComentarioElecForm()

    return render(request, 'comentarios/agregar_comen_ele.html', {
        'vehiculo': vehiculo,
        'form': form
    })
    
def editar_comentario_elec(request, comentario_id):
    comentario = get_object_or_404(ComentarioElec, pk=comentario_id)
    vehiculo_id = comentario.vehiculo.id  # guardamos antes para el redirect

    if request.method == 'POST':
        form = ComentarioElecForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('ver_comentarios_elec', vehiculo_id=vehiculo_id)
    else:
        form = ComentarioElecForm(instance=comentario)

    return render(request, 'comentarios/agregar_comen_ele.html', {'vehiculo': comentario.vehiculo,'form': form,'comentario': comentario})

def eliminar_comentario_elec(request, comentario_id):
    comentario = get_object_or_404(ComentarioElec, id=comentario_id)
    vehiculo_id = comentario.vehiculo.id

    if request.method == 'POST':
        comentario.delete()
        return redirect('ver_comentarios_elec', vehiculo_id=vehiculo_id)

    return render(request, 'comentarios/eliminar_comen_ele.html', {'comentario': comentario})