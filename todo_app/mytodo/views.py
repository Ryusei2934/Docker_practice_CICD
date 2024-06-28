from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm

# Create your views here.
class IndexView(View):
    def get(self, request):
        # todoリストを取得
        todo_list = Task.objects.all()
        context = {
            "todo_list": todo_list
        }
        # テンプレートをレンダリング
        return render(request, "mytodo/index.html", context)

class AddView(View):
    def get(self, request):
        form = TaskForm()
        # テンプレートのレンダリング処理
        return render(request, "mytodo/add.html", {'form': form})

    def post(self, request, *args, **kwargs):
        # 登録処理
        # 入力データをフォームに戻す
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        # データが正常ではない
        return render(request, 'mytodo/add.html', {'form': form})

class Update_task_complete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id=task_id)
        task.complete = not task.complete
        task.save()
        return redirect('/')

class TaskUpdate(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        form = TaskForm(instance=task)
        context = {
            "form": form,
            "task": task
        }
        return render(request, "mytodo/taskupdate.html", context)

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")
        context = {
            "form": form,
            "task": task
        }
        return render(request, "mytodo/taskupdate.html", context)

class DeleteView(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('/')

# ビュークラスをインスタンス化
index = IndexView.as_view()
add = AddView.as_view()
taskupdate = TaskUpdate.as_view()
delete = DeleteView.as_view()
