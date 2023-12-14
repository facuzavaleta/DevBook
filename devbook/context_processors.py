from datetime import datetime

def current_datetime(request):
    return {'current_datetime': datetime.now()}

def show_name(request):
    return {'show_name': datetime.now()}
