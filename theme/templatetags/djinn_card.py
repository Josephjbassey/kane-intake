from django import template
from django.template.base import token_kwargs
from djinn.core.cva import cva

register = template.Library()

card_cva = cva(
    base="rounded-lg border bg-card text-card-foreground shadow-sm",
    variants={
        "variant": {
            "default": "border",
            "bordered": "border-2",
            "elevated": "shadow-lg",
        },
    },
    default_variants={
        "variant": "default",
    }
)

class CardNode(template.Node):
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

        # Evaluate cva
        final_class = card_cva(**resolved_kwargs)

        # Separate extra attributes
        known_args = ["variant", "title", "description", "footer", "class", "class_name", "slot"]
        attrs = {k: v for k, v in resolved_kwargs.items() if k not in known_args}

        # Render body
        slot = self.nodelist.render(context) if self.nodelist else ""
        title = resolved_kwargs.get("title", "")
        description = resolved_kwargs.get("description", "")
        footer = resolved_kwargs.get("footer", "")

        t = context.template.engine.get_template('components/card.html')
        new_context = context.new({
            "class": final_class,
            "slot": slot,
            "title": title,
            "description": description,
            "footer": footer,
            "attrs": attrs,
            **resolved_kwargs
        })
        return t.render(new_context)

@register.tag('djinn_card')
def djinn_card(parser, token):
    bits = token.split_contents()
    kwargs = token_kwargs(bits[1:], parser)
    nodelist = parser.parse(('enddjinn_card',))
    parser.delete_first_token()
    return CardNode(nodelist, kwargs)