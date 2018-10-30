from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from bokaforlag.baekur.views import baekur_forsida
from django.contrib.flatpages import views as flatpages_views

from bokaforlag.pantanir.views import admin_pontun_lysing

from django.views.generic import RedirectView

urlpatterns = [
    path("forsida", baekur_forsida, name="baekur_forsida"),

    # path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("", RedirectView.as_view(url="forsida")),
    # NB tmp tók út
    # path(
    #     "about/",
    #     TemplateView.as_view(template_name="pages/about.html"),
    #     name="about",
    # ),
    # Django Admin, use {% url "admin:index" %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    # NB tmp tók út
    # path(
    #     "users/",
    #     include("bokaforlag.users.urls", namespace="users"),
    # ),
    # path("accounts/", include("allauth.urls")),

    # Your stuff: custom urls includes go here
    path("baekur/", include("bokaforlag.baekur.urls")),
    path("pantanir/", include("bokaforlag.pantanir.urls")),
    path("frettir/", include("bokaforlag.frettir.urls")),

    # flatpages
    path(
        "um-am-forlag/",
        flatpages_views.flatpage,
        {"url": "/um-am-forlag/"},
        name="um_am_forlag"
    ),
    path(
        "english/",
        flatpages_views.flatpage,
        {"url": "/english/"},
        name="english"
    ),

    path("admin/pantanir/pontun/<int:pk>/lysing", admin_pontun_lysing, name="admin_pontun_lysing"),

] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
