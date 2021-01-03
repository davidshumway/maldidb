""" soMedia URL Configuration """

from django.urls import path
from . import views
from .views import SearchResultsView, LibrariesListView, SpectraListView, MetadataListView, LabgroupsListView
from .views import FilteredSpectraListView

app_name = 'chat'
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/add', views.add_post, name='add_post'),
    path('posts/add_metadata', views.add_metadata, name='add_metadata'),
    path('posts/add_sqlite', views.add_sqlite, name='add_sqlite'),
    path('posts/add_lib', views.add_lib, name='add_lib'),
    path('posts/add_labgroup', views.add_labgroup, name='add_labgroup'),
    path('comments/add/<post_id>', views.add_comment, name='add_comment'),
    
    # ~ path('search/', views.search, name='search'),
    # ~ path('search/', SearchResultsView.as_view(), name='search_results'),
    
    
    # ...
    path('search/', FilteredSpectraListView.as_view(), name='search_results'),
    
    path('libraries/', LibrariesListView.as_view(), name='libraries_results'),
    
    # ~ path('spectra/', SpectraListView.as_view(), name='spectra_results'),
    path('spectra/', FilteredSpectraListView.as_view(), name='spectra_results'),
    
    # All spectra from a library / filter
    # ~ path('spectra/<library_id/', FilteredSpectraLibListView.as_view(), name='spectra_library_results'),
    
    path('metadata/', MetadataListView.as_view(), name='metadata_results'),
    path('labgroups/', LabgroupsListView.as_view(), name='labgroups_results'),
    #test
    
    path('library/<library_id>/', views.library_profile, name='view_library'),
    path('library/edit/<library_id>/', views.edit_libprofile, name='edit_libprofile'),
    
    path('labs/<lab_id>/', views.lab_profile, name='view_lab'),
    path('labs/edit/<lab_id>/', views.edit_labprofile, name='edit_labprofile'),
]
