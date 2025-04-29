from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from SkinVisionApp.models import Annotation, CustomUser
from .models import Annotation, UserImage
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from .userEditForm import UserEditForm




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login was successful!')
            return redirect('dashboard')  # Redirect to dashboard
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'login.html')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        # Extracting form data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'register.html')

        # Check if username or email already exists
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return render(request, 'register.html')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return render(request, 'register.html')

        # Create and save a new user
        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Registration was successful!')
        return redirect('login')

    # If not POST, render the registration form
    return render(request, 'register.html')

def role_required(required_role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.role != required_role:
                return HttpResponseForbidden("You do not have permission to access this page.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

@login_required
def dashboard_view(request):
    user_images = UserImage.objects.filter(user=request.user)
    # Pass user's images and other details to the template
    return render(request, 'dashboard.html', {
        'username': request.user.username,
        'email': request.user.email,
        'user_images': user_images,
    })

@login_required
def profile_view(request):
    user_images = UserImage.objects.filter(user=request.user)  # Assuming a UserImage model with a user field
    return render(request, 'profile.html', {'user_images': user_images})

@login_required
def annotation_view(request):
    # Loading image data to annotate directly from the Annotation model
    annotation = Annotation.objects.first()  # Or filter/select as needed
    if annotation is not None:
        context = {'image_data': annotation.image_data}
    else:
        context = {'message': 'No images available for annotation'}

    # Render the HTML template with the context
    return render(request, 'annotate.html', context)


@csrf_exempt
@login_required
def save_annotation(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        image_data = data['image_data']

        # Create annotation linked to the request user
        annotation = Annotation.objects.create(
            user=request.user,
            image_data=image_data
        )
        return JsonResponse({'id': annotation.id}, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

@login_required
@role_required('admin')
def registered_users_view(request):
    users = CustomUser.objects.all()
    return render(request, 'registered_users.html', {'users': users})


@login_required
def upload_image_view(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        # Save the image to UserImage model
        UserImage.objects.create(user=request.user, image=filename)
        return render(request, 'uploadImage.html', {'uploaded_image_url': uploaded_file_url})
    return render(request, 'uploadImage.html')

@login_required
def delete_image(request, image_id):
    image = UserImage.objects.filter(pk=image_id, user=request.user).first()  # Ensure the image belongs to the user
    if image:
        image.delete()  # Delete the image
        messages.success(request, 'Image successfully deleted')
        return render(request, 'profile.html')  # Redirect to the profile page

@login_required    
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated!')
            return redirect('profile')  # Redirect to the profile page after update
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})