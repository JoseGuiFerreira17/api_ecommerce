from django.urls import path, include


urlpatterns = [
    # DOCS
    path("", include("apps.doc_urls")),
    # API
    path("", include("apps.product.api.routers")),
    path("", include("apps.accounts.api.routers")),
    path("", include("apps.purchase.api.routers")),
]
