from django.shortcuts import render, get_object_or_404
from .models import Student

def home(request):
    return render(request, 'exam/home.html')

def result(request):
    hall_ticket = request.GET.get('hall_ticket')

    # Only check the hall ticket if it is provided
    if hall_ticket:
        try:
            student = Student.objects.get(hall_ticket=hall_ticket)
            return render(request, 'exam/result.html', {'student': student})
        except Student.DoesNotExist:
            # Only pass the error if the hall ticket was not found
            error_message = 'Hall ticket not found. Please check the number and try again.'
            return render(request, 'exam/home.html', {'error': error_message})

    # If the hall ticket is not provided, redirect to the home page without error
    return render(request, 'exam/home.html')
