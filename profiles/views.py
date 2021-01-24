from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_protect

from users.models import CustomUser

post_page_size = 5


# Profiles Home View
class ProfilesHomeView:

    def get_page_data(self, context, owner):
        # Home Page Owner
        context['owner'] = owner
        # Posts List
        # context['post_list'] = self.get_posts(owner, 1)
        # Friends List
        # Discussions List
        # Friendship Requests List
        return context




@method_decorator(login_required, name='dispatch')
class MyHomeView(ProfilesHomeView, generic.TemplateView):
    template_name = 'profiles/profile_home.html'

    def get_context_data(self, **kwargs):
        context = super(MyHomeView, self).get_context_data(**kwargs)
        owner = self.request.user
        return self.get_page_data(context, owner)


@method_decorator(login_required, name='dispatch')
class VisitingHomeView(ProfilesHomeView, generic.TemplateView):
    template_name = 'profiles/profile_home.html'
    pk_url_kwarg = 'user_id'

    def get_context_data(self, **kwargs):
        user = self.request.user

        context = super(VisitingHomeView, self).get_context_data(**kwargs)
        owner = CustomUser.objects.get(pk=kwargs[self.pk_url_kwarg])

        # Permission Authentication
        return self.get_page_data(context, owner)