from django.shortcuts import render


def operation(num1, num2, sign):
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '&times;':
        return num1 * num2
    else:
        return num1 / num2


def calculator_view(request):
    if request.GET:
        if request.GET != "" or request.GET == int:
            num1 = int(request.GET['num1'])
            num2 = int(request.GET['num2'])
            sign = request.GET['sign']
    else:
        num1 = 0
        num2 = 0
        sign = 'add'
        print(request.GET)
    context = {
        'n1': num1,
        'n2': num2,
        'sign': sign,
        'solution': operation(num1, num2, sign),

    }
    return render(request, 'calculator.html', context)
