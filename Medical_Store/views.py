from django.shortcuts import render,redirect,get_object_or_404
from .forms import MedicineForm
from .models import Medicine
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q





def home_page(request):
    return render(request,'image_included.html')


@login_required
def list_medicine(request):
    query = request.GET.get('q', '')
    medicines = Medicine.objects.all()

    if query:
        medicines = medicines.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'list_medicine.html', {'medicines': medicines, 'query': query})



@login_required
def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicinelist')  # Redirect to the medicine list page
    else:
        form = MedicineForm()
    return render(request, 'add_medicine.html', {'form': form})


@login_required
def edit_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, pk=medicine_id)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicinelist')
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'edit_medicine.html', {'form': form, 'medicine': medicine})

@login_required
def delete_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, pk=medicine_id)
    if request.method == 'POST':
        medicine.delete()
        return redirect('medicinelist')
    return render(request, 'delete_medicine.html', {'medicine': medicine})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('home_page')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid form data')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    return render(request, 'logout.html')  # Redirect to your desired page after logout
