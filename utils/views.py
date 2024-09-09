from django.shortcuts import render
from typing import Any
from django import http
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin,
)

from django.http.response import HttpResponse
from django.views import View
from django.http import HttpRequest


class StaffMemberCheckMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = "/login/"

    def test_func(self):
        return self.request.user.is_staff


class BaseView(View):
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.check_permissions(request)
        return super().dispatch(request, *args, **kwargs)

    def check_permissions(self, request: HttpRequest) -> None:
        pass


class BaseLoginRequiredView(LoginRequiredMixin, View):
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.check_permissions(request)
        return super().dispatch(request, *args, **kwargs)

    def check_permissions(self, request: HttpRequest) -> None:
        pass

