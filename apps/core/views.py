from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Основная страница"""

    template_name: str = "core/index.html"


class PolicyView(TemplateView):
    """Политика конфиденциальности"""

    template_name: str = "core/policy.html"
