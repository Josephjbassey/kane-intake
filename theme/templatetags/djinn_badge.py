from django import template
from django.template.base import token_kwargs
from djinn.core.cva import cva

register = template.Library()

badge_cva = cva(
    base="inline-flex items-center rounded-md border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2",
    variants={
        "variant": {
            "default": "border-transparent bg-primary text-primary-foreground hover:bg-primary/80",
            "secondary": "border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80",
            "destructive": "border-transparent bg-destructive text-destructive-foreground hover:bg-destructive/90",
            "outline": "border-input bg-background hover:bg-accent hover:text-accent-foreground",
            "ghost": "hover:bg-accent hover:text-accent-foreground",
            "success": "border-transparent bg-emerald-500/10 text-emerald-700",
            "warning": "border-transparent bg-amber-500/10 text-amber-700",
        },
    },
    default_variants={
        "variant": "default",
    }
)

class BadgeNode(template.Node):
    def __init__(self, nodelist, kwargs):
        self.nodelist = nodelist
        self.kwargs = kwargs

    def render(self, context):
        resolved_kwargs = {}
        for k, v in self.kwargs.items():
            try:
                resolved_kwargs[k] = v.resolve(context)
            except template.VariableDoesNotExist:
                resolved_kwargs[k] = ""

        final_class = badge_cva(**resolved_kwargs)

        known_args = ["variant", "class", "class_name", "slot"]
        attrs = {k: v for k, v in resolved_kwargs.items() if k not in known_args}

        slot = self.nodelist.render(context) if self.nodelist else ""
        t = context.template.engine.get_template('components/badge.html')
        new_context = context.new({
            "class": final_class,
            "slot": slot,
            "attrs": attrs,
            **resolved_kwargs
        })
        return t.render(new_context)

@register.tag('djinn_badge')
def djinn_badge(parser, token):
    bits = token.split_contents()
    kwargs = token_kwargs(bits[1:], parser)
    nodelist = parser.parse(('enddjinn_badge',))
    parser.delete_first_token()
    return BadgeNode(nodelist, kwargs)