from django.urls import path, include

foo = "hxjjdjdjdjxjxjxjxhsjxhdjdjjdjdjdjfjfjjfjfjfjfjfjfjfjjcjfjfjjfjfjfjfjjfjfjhfjfjfjfjjfjfjdhdhfhdhfhdhdjbjjdjjddjbd"

urlpatterns = [
    path(
        "api/",
        include("api.docs.urls"),
    ),
    path(
        "api/",
        include("api.authentication.urls"),
    ),
    path(
        "api/",
        include("api.accounts.urls"),
    ),
    path(
        "api/",
        include("api.users.urls"),
    ),
]
