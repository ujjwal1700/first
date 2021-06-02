from django.shortcuts import render,redirect




def login_excluded(redirect_to):
    """ This decorator kicks authenticated users out of a view """
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
