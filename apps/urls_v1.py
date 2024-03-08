from django.urls import path, include


urlpatterns = [
    #DOCS
    path("", include("apps.doc_urls")),
    #API
    path("", include("apps.product.urls")),
    path("", include("apps.accounts.urls")),
]