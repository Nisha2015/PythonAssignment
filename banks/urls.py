from django.urls import include, path, re_path
from django.conf.urls import url
from . import views


urlpatterns = [
    re_path(r'^api/v1/banks/(?P<pk>[0-9]+)$',
        views.get_delete_update_bank.as_view(),
        name='get_delete_update_bank'
    ),
    path('api/v1/banks/', # urls list all and create new one
        views.get_post_bank.as_view(),
        name='get_post_bank'
    ),
    re_path(r'^api/v1/branches/(?P<pk>[0-9]+)$',
        views.get_delete_update_branches.as_view(),
        name='get_delete_update_branches'
    ),
    path('api/v1/branches/', # urls list all and create new one
        views.get_post_branches.as_view(),
        name='get_post_branches'
    ),
    url('^api/v1/branches/(?P<name>.+)/(?P<city>.+)/$', # urls list all and create new one
        views.get_branches_with_bank_name.as_view(),
        name='get_branches_with_bank_name')
]