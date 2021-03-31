from django.conf import settings


def settings_context_processor(request):
    return {'settings': settings}
