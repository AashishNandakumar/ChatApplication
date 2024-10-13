from django.shortcuts import render


# Create your views here.
def chat_box(request, chat_box_name):
    # each name is a different chat room
    return render(request, "chatbox.html", {"chat_box_name": chat_box_name})
