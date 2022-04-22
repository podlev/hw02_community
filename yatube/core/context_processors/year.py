import datetime


def year(request):
    """Добавляет переменную с текущим годом."""
    y = datetime.datetime.now().year
    return {
        'year': y
    }
