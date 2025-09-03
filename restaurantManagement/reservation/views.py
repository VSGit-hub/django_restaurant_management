from django.shortcuts import render, redirect
from .forms import TableReservationForm
from django.http import HttpResponse
from  .models import Tables

def reserve_table(request):
    if request.method == "POST":
        form = TableReservationForm(request.POST)
        if form.is_valid():
            guests = form.cleaned_data["no_of_guests"]
            table = Tables.get_available_table(guests)

            if table:
                reservation = form.save(commit=False)
                reservation.alloted_table = table
                reservation.save()

                table.status = 'B'
                table.save()

                return redirect('reservationApp:booking_success')
            
            else:
                form.add_error(None, 'No table for requested party size.')

    else:
        form = TableReservationForm()

    return render(request, 'reservation/book_table_form.html', {'form':form})

def booking_success(request):
    return render(request, 'reservation/booking_success.html')                                      