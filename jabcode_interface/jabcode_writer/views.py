from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    return render(request, 'result.html')

def process_textbox(request):
    if request.method == "POST":
        textbox_content = request.POST['textbox']
        print(textbox_content)
        return render(request, 'result.html', {'my_string': textbox_content})
    else:
        pass
        return render(request, 'index.html')

