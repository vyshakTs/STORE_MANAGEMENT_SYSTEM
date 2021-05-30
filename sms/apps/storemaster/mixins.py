from django.contrib.auth.mixins import AccessMixin


class IsStoreOwnerMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_SO:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)