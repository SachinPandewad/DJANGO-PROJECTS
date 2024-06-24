from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'calculator/home.html')

def result(request):
    num1 = int(request.GET.get('number1'))
    num2 = int(request.GET.get('number2'))
    
    if request.GET.get('add') == "":
        ans = num1 + num2
    elif request.GET.get('subtract') == "":    
        ans = num1 - num2
    elif request.GET.get('multiply') == "":    
        ans = num1 * num2
    else:
        ans = num1 / num2

    return render(request, 'calculator/result.html', {'ans': ans})