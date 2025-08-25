from django import template

register = template.Library()

@register.filter
def stars(value):
    """Return a star string based on average rating"""
    try:
        value = float(value)
    except (TypeError, ValueError):
        return "☆☆☆☆☆"

    full_stars = int(value)
    half_star = 1 if value - full_stars >= 0.5 else 0
    empty_stars = 5 - full_stars - half_star

    return "★" * full_stars + "½" * half_star + "☆" * empty_stars
