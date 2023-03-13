from django.shortcuts import render


def handle_not_found(request, exception):
    """ Handles unrecognised URLS """

    return render(request, 'not-found.html')
