import random

from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ReservationForm
from .models import DishCategory, Gallery
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = DishCategory.objects.filter(is_visible=True)
        context['gallery'] = Gallery.objects.filter(is_visible=True)
        context['booking_form'] = ReservationForm()
        return context

    def post(self, request, *args, **kwargs):
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            messages.success(request, 'Сообщение о бронировании столика отправлено администратору!')
            redirect('cafe:home')
        messages.error(request, 'Сообщение о бронировании столика НЕ отправлено администратору!')
        context = super().get_context_data(**kwargs)
        context['booking_form'] = reservation_form
        return render(request, self.template_name, context=context)