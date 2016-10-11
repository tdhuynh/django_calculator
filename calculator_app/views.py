from django.shortcuts import render


def operation(num1, num2, sign):
    if sign == 'add':
        return num1 + num2
    elif sign == 'sub':
        return num1 - num2
    elif sign == 'mult':
        return num1 * num2
    else:
        return num1 / num2


def calculator_view(request):
    if request.GET != "" or request.GET == int:
        if request.GET:
            num1 = int(request.GET['num1'])
            num2 = int(request.GET['num2'])
            sign = request.GET['sign']
        else:
            num1 = 0
            num2 = 0
            sign = 'add'
        print(request.GET)
    context = {
        "solution": operation(num1, num2, sign),
    }
    return render(request, 'calculator.html', context)
