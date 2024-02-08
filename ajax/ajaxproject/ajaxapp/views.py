from django.shortcuts import render

def index(request):
    if request.method == 'POST':  # Use 'POST' instead of 'post'
        username = request.POST.get('username')  # Use 'get' instead of 'post' and fix the attribute name
        password = request.POST.get('password')  # Use 'get' instead of 'post' and fix the attribute name

        print(username, password)

        # Check if the provided credentials are correct
        if username == 'testuser' and password == 'testpass':
            # Authentication successful, you can redirect or do something else here
            return render(request, 'login.html')  # Replace 'success.html' with the actual success template
        else:
            # Authentication failed, you can render the login page with an error message
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'login.html')
