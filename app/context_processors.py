from django.conf import settings


def selected_settings(request):
    r = {
        'SECUREFLOW_VERSION': settings.SECUREFLOW_VERSION,
        'SECUREFLOW_REFRESH_ENGINE': settings.SECUREFLOW_REFRESH_ENGINE,
        'PRO_EDITION': settings.PRO_EDITION,
        'LOGOUT_URL': settings.LOGOUT_URL
    }

    if hasattr(settings, 'LOGIN_SSO_URL'):
        r.update({'LOGIN_SSO_URL': settings.LOGIN_SSO_URL})

    return r
