from django.shortcuts import render, redirect
from .models import TodoList

def todo_manager(request):
   
    if request.method == 'POST':
        req_title = request.POST.get('title')
        req_content = request.POST.get('content')
        
        
        
        print(req_title, req_content)
        print("------------------------------")
        
        
        TodoList.objects.create(title=req_title, content=req_content)
        
        
        return redirect('todo_view')

    
    elif request.method == 'GET':
        all_todos = TodoList.objects.all()
        
        
        return render(request, 'note.html', {'todos': all_todos})







# 3. UPDATE OPERATION: Marks a task as Complete (True)
def update_todo(request, pk):
    # Fetch the specific task using its ID number (pk)
    todo = TodoList.objects.get(id=pk)
    # Switch its status to True
    todo.status = True
    todo.save()
    return redirect('todo_view')

# 4. DELETE OPERATION: Removes the task from the database
def delete_todo(request, pk):
    todo = TodoList.objects.get(id=pk)
    todo.delete()
    return redirect('todo_view')


    # get request
# Here is exactly what happens when a user visits your website:
# 1. The user's browser sends a GET request asking to see the page.
# 2. Django triggers your todo_list function.
# 3. TodoList.objects.all() looks into your database and grabs all your saved notes.
# 4. render(request, 'note.html', {'todos': all_todos}) sends those notes to your note.html file so they show up on the screen.