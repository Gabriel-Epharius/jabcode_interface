from django.shortcuts import render
import subprocess
import os

# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    return render(request, 'result.html')

def process_textbox(request):
    if request.method == "POST":
        
        textbox_content = request.POST['textbox']
        project_dir = os.path.dirname(os.path.abspath(__file__))

        output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
        output_file = os.path.join(output_dir, 'images/test.png')

        subprocess.run(f'{os.path.join(project_dir, "jabcode_writer")} --input "{textbox_content}" --output "{output_file}"', shell=True)

        return render(request, 'result.html', {'my_string': textbox_content})
    else:
        pass
        return render(request, 'index.html')

