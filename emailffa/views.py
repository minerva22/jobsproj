import json

from django.views import generic
from django.http import JsonResponse

from .models import Job
#from .models import Email
#from .models import Cron
#from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class IndexView(generic.ListView):
    template_name = 'emailffa/index.html'
    context_object_name = 'latest_job_list'
    paginate_by = 15
    def get_queryset(self):
        """Return the  jobs by order alphabetic."""
        return Job.objects.order_by('job_text')

class DetailView(generic.DetailView):
      model = Job
      template_name = 'emailffa/detail.html'


      def get(self, *args, **kwargs):

          #url="http://localhost:8000/emailffa/1/?asjson=true"
       
          #http://programtalk.com/vs2/python/2464/django-completion/completion/views.py/
          asjson = self.request.GET.get('asjson', "false")
          asjson=asjson.lower()=="true"
	  
          if not asjson:
              return super(DetailView, self).get(*args, **kwargs)
<<<<<<< HEAD

	  #https://stackoverflow.com/questions/34460708/checkoutview-object-has-no-attribute-object
          self.object = self.get_object()
          context = super(DetailView, self).get_context_data(**kwargs)
          job = context["job"]
          output = {
            "job_text": job.job_text,
            "pub_date": job.pub_date.strftime("%Y-%m-%d"),
            "job_cron": job.job_cron,
            "email_set": [x.email_text for x in job.email_set.all()]
          }
          return JsonResponse(output)


#def detail(request, job_id):
    #job = get_object_or_404(Job, pk=job_id)
    #return render(request, 'emailffa/detail.html', {'job': job})
=======
>>>>>>> oldversion

	  #https://stackoverflow.com/questions/34460708/checkoutview-object-has-no-attribute-object
          self.object = self.get_object()
          context = super(DetailView, self).get_context_data(**kwargs)
          job = context["job"]
          output = {
            "job_text": job.job_text,
            "pub_date": job.pub_date.strftime("%Y-%m-%d"),
            "job_cron": job.job_cron,
            "email_set": [x.email_text for x in job.email_set.all()]
          }
          return JsonResponse(output)


#def detail(request, job_id):
    #job = get_object_or_404(Job, pk=job_id)
    #return render(request, 'emailffa/detail.html', {'job': job})


