import time

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from fib_api.models import FibonacciResults


def fibonacci_calculation(num):
    if num < 2:
        result = num
    else:
        result = fibonacci_calculation(
            num - 1) + fibonacci_calculation(num - 2)
    return result


def fib_number(request):
    num = 0
    result = 0
    time_taken = 0

    if request.GET.get('number'):
        start_time = time.clock()
        number = request.GET.get('number')
        num = int(number)
        result = fibonacci_calculation(num)
        time_taken = time.clock() - start_time

        obj = FibonacciResults.objects.create(
            number=num, result=result, time_taken=time_taken)
        obj.save()

    return render(
        request,
        'index.html',
        {
            'number': num,
            'result': result,
            'time_taken': time_taken
        }
    )
