from django.http import HttpResponse
from models import Student
from django.views.generic.edit import  UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import View
from .forms import StudentForm

class IndexView(View):
    form_class = StudentForm
    template_name = 'studentapp/index.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        students = Student.objects.all()
        try:
            data = [{"name": i.name, "maths_score": i.maths_score, "science_score": i.science_score,
                     "history_score": i.history_score,
                     "social_score": i.social_score, "id": i.id} for i in students]
            context = {
                'data': data,
                'form':form
            }
        except Exception as e:
            print e
            return HttpResponse("Something went wrong")
        return render(request, self.template_name,context )

    def post(self, request, *args, **kwargs):

        try:
            form = StudentForm(request.POST)
            if form.is_valid():
                student = form.save(commit=False)
                student.save()
        except Exception as e:
            print  e
            return HttpResponse("Something went wrong")
        return HttpResponse(self.get(request))

class MyDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('index')

class MyUpdatateView(UpdateView):
    model = Student
    success_url = reverse_lazy('index')
    fields = ['name', 'maths_score', 'science_score','history_score','social_score']

class MyListView(View):
    form_class = StudentForm
    queryset = Student.objects.all()
    template_name = 'studentapp/index.html'
    def post(self, request, *args, **kwargs):
        form = self.form_class()
        try:
            sum_s = 0
            student = Student.objects.filter(name=request.POST.get('text'))
            for i in student:
                sum_s += i.maths_score + i.science_score + i.history_score + i.social_score
            from django.db.models import F
            students =  Student.objects.annotate(
                i_sum=F('maths_score') + F('science_score') + F('history_score') + F('social_score')).filter(
                i_sum=sum_s)
            data = [{"name": i.name, "maths_score": i.maths_score, "science_score": i.science_score,
                     "history_score": i.history_score,
                     "social_score": i.social_score, "id": i.id} for i in self.queryset]

            filter_data = [{"name": i.name, "maths_score": i.maths_score, "science_score": i.science_score,
                     "history_score": i.history_score,
                     "social_score": i.social_score, "id": i.id} for i in students]
            context = {
                'data':data,
                'filter_data': filter_data,
                'form': form,
                'filter':True, #check
            }
            return render(request, self.template_name, context)
        except Exception as e:
            return HttpResponse("Something went wrong")
