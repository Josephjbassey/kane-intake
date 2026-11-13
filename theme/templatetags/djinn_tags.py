from django import template
try:
    from tailwind_merge import TailwindMerge
    tw_merge = TailwindMerge().merge
except ImportError:
    tw_merge = lambda *args: " ".join(args)

register = template.Library()

@register.simple_tag
def cn(*args):
    """
    Merges tailwind classes intelligently.
    Usage: {% cn "base-class" dynamic_class %}
    """
    classes = [str(arg) for arg in args if arg]
    return tw_merge(*classes)
