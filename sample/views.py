import time
from django.http import JsonResponse
from sample.pystone_delta_blue import delta_blue

def pystones_view(request):
    time.sleep(1.0)
    time_one = time.time()
    delta_blue(25000)
    time_two = time.time()
    return JsonResponse("Benchmark done: %.02f seconds" % (time_two - time_one), safe=False)
