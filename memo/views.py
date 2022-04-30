from django.shortcuts import render


# Create your views here.
def personal_memo(request):
    print("trying to get ")
    return render(request, 'memo/memo.html')