from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('inicio')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users(allowed_roles = []):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group = None
            if request.user.rol != None:
                group = request.user.rol
            
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                print(group)
                return HttpResponse('No estás autorizado para entrar a esta dirección')
        return wrapper_func
    return decorator
