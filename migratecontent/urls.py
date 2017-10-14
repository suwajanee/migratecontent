from django.conf.urls import url

from views.dashboard_view import DashboardView
from views.page_export_view import PageExportView
from views.page_import_view import PageImportView
from views.blog_export_view import BlogExportView
from views.blog_import_view import BlogImportView
from views.decompose_view	 import DecomposeView


urlpatterns = [
	url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^page-export/$', PageExportView.as_view(), name='page_export'),
    url(r'^page-import/$', PageImportView.as_view(), name='page_import'),
    url(r'^blog-export/$', BlogExportView.as_view(), name='blog_export'),
    url(r'^blog-import/$', BlogImportView.as_view(), name='blog_import'),
    url(r'^decompose/$', DecomposeView.as_view(), name='decompose'),
]