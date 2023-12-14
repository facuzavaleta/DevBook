from django.shortcuts import render, get_object_or_404, redirect
from .models import notification

# Create your views here.
def notifications_index(request, username):
    notifications = notification.objects.filter(user=request.user)
    unread_notifications = notifications.filter(is_read=False)
    unread_notifications.update(is_read=True)
    
    return render(request, 'notifications/notifications_index.html', {'notifications': notifications, 'unread_notifications': unread_notifications,})

def send_notification(request):
    notification.objects.create()

def mark_as_read(request, notification_id):
    notification = get_object_or_404(notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('home', username=request.user.username)

def send_notification_test(username):
    message = f"notificacion enviada a {username}"
    return message