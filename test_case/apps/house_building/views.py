from django.views.generic import ListView, CreateView
from .models import House, BrickworkTask
from django.shortcuts import get_object_or_404
import datetime


class AddNewHouse(CreateView):
    model = House
    fields = ['address', 'year']
    template_name = 'house_building/new_house.html'
    success_url = '/stats/'


class AddBrickworkTask(CreateView):
    model = BrickworkTask
    fields = ['bricks_count', 'date']
    template_name = 'house_building/new_house.html'
    success_url = '/stats/'

    def form_valid (self, form):
        obj = form.save(commit=False)
        # add house to form from id in url
        obj.house = get_object_or_404(House, id=self.kwargs['id'])
        # If date lover then now, return form_invalid
        if obj.date.date() < datetime.date.today():
            return super(AddBrickworkTask, self).form_invalid(form)
        return super(AddBrickworkTask, self).form_valid(form)


class AllStatistics(ListView):
    template_name = 'house_building/stats.html'
    queryset = House.objects.all()
