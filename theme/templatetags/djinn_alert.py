from django import template
from django.template.base import token_kwargs
from djinn.core.cva import cva

register = template.Library()

alert_cva = cva(
    base="relative w-full rounded-lg border p-4 [&>svg+div]:translate-y-[-3px] [&>svg]:absolute [&>svg]:left-4 [&>svg]:top-4 [&>svg]:text-foreground [&>svg~*]:pl-7",
    variants={
        "variant": {
            "default": "bg-background text-foreground border-input",
            "destructive": "border-destructive/50 text-destructive dark:border-destructive [&>svg]:text-destructive",
            "success": "border-emerald-500/50 text-emerald-700 dark:border-emerald-400 [&>svg]:text-emerald-400",
            "warning": "border-amber-500/50 text-amber-700 dark:border-amber-400 [&>svg]:text-amber-400",
        },
    },
    default_variants={
        "variant": "default",
    }
)

class AlertNode(template.Node):
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
        final_class = alert_cva(**resolved_kwargs)

        # Separate extra attributes
        known_args = ["variant", "icon", "title", "class", "class_name", "slot"]
        attrs = {k: v for k, v in resolved_kwargs.items() if k not in known_args}

        # Render body
        slot = self.nodelist.render(context) if self.nodelist else ""
        icon = resolved_kwargs.get("icon", "")
        title = resolved_kwargs.get("title", "")

        t = context.template.engine.get_template('components/alert.html')
        new_context = context.new({
            "class": final_class,
            "slot": slot,
            "icon": icon,
            "title": title,
            "attrs": attrs,
            **resolved_kwargs
        })
        return t.render(new_context)

@register.tag('djinn_alert')
def djinn_alert(parser, token):
    bits = token.split_contents()
    kwargs = token_kwargs(bits[1:], parser)
    nodelist = parser.parse(('enddjinn_alert',))
    parser.delete_first_token()
    return AlertNode(nodelist, kwargs)