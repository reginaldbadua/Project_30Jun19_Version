from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import tank, style

# Create your views here.


def index(request):
    # Tank.objects.all()  read all the table
    # Tank.objects.filter(release_year = 2004)
    # Tank.objects.get(id=1)

    catalog = tank.objects.all()
    return render(request, 'views/index.html',
                  {'catalog': catalog, 'tank_type': 'This is the page tank_type'})


# /tank/detail/1
# find the object with id = 1
def detail(request, tank_id):
    try:
        the_tank = tank.objects.get(id=tank_id)
        return render(request, 'views/detail.html', {'tank': the_tank})
    except tank.DoesNotExist:
        # raise a 404 error
        raise Http404()


def test(request):
    return HttpResponse("<h1>I'm a test</h1>")


def contact(request):
    return HttpResponse("<h1>Page under construction</h1>")


def styles(request):
    all = Style.objects.all()
    print(all)
    return render(request, "views/styles.html", {"styles": all})

# def history(request):
#     return render(request, 'views/history.html')

# def order(request):
#     return render(request, 'views/order.html')

# /tanks/styles
# display the list of generes

# need:
#   register the path /url
#   register the view function
#   create the html file (generes.html)
