from django.shortcuts import render
from .forms import DateForm, BookingForm
from django.shortcuts import redirect


def home(request):
    return render(request, 'home.html', {})


def DateView(request):
    form = DateForm(request.POST or None)
    if form.is_valid():
        request.session["dateSelected"] = str(
            form.cleaned_data["booking_date"])
        print(form.cleaned_data)

        return redirect('book')

    context = {
        'form': form
    }
    return render(request, "date_form.html", context)


def BookingView(request):
    form = BookingForm(request.POST or None)

    context = {
        'form': form
    }
    return render(request, "booking_form.html", context)
