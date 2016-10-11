from django.shortcuts import render


def calculator_view(request):
    print(request.GET)
    # num1 = request.GET['num1']
    # num2 = request.POST['num2']
    return render(request, 'calculator.html')
