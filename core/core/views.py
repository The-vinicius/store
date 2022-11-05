from django.shortcuts import render

def home(request):
    svg = []
    # list with logo svg (name 1 to 10 .svg)
    for i in range(1,11):
        svg.append(f'logo/{i}.svg')
    context = {
        'listsvg': svg,
    }
    return render(request, 'home.html', context)
