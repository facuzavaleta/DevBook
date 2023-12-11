from django.shortcuts import render, get_object_or_404, redirect
from .models import notification

# Create your views here.
def notifications_index(request, username):
    return render(request, 'notifications/notifications_index.html')

def send_notification(user, message, content_object=None):
    notification.objects.create(user=user, message=message, content_object=content_object)

def mark_as_read(request, notification_id):
    notification = get_object_or_404(notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('home', username=request.user.username)