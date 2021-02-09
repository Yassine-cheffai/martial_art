from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from grappelli.dashboard import modules, Dashboard

class CustomIndexDashboard(Dashboard):
    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)

        self.children.append(modules.ModelList(
            title='Tournaments',
            column=1,
            models=('tournament.models.Tournament',)
        ))

        self.children.append(modules.ModelList(
            title='Your Team',
            column=1,
            models=('team.models.Team',)
        ))

        self.children.append(modules.ModelList(
            title='Your Participations',
            column=1,
            models=('team.models.Participation',)
        ))

        # append an app list module for "Administration"
        self.children.append(modules.AppList(
            title=_('Administration'),
            column=1,
            collapsible=True,
            models=('django.contrib.*',),
        ))
