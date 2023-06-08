from django import template
from django.utils.html import format_html

register = template.Library()

# @register.simple_tag
# def row(extra_classes=""):
#     return format_html('<div class="row {}">', extra_classes)
#
#
# @register.simple_tag
# def endrow():
#     return format_html("</div>")
#
# @register.simple_tag
# def col(extra_classes=""):
#     return format_html('<div class="col {}">', extra_classes)
#
# @register.simple_tag
# def endcol():
#     return format_html("</div>")

@register.simple_tag
def para(extra_classes=""):
    return format_html('<p class="{}">', extra_classes)

@register.simple_tag
def endpara():
    return format_html("</p>")

@register.simple_tag
def link(href="", extra_classes=""):
    return format_html('<a href="{}" class="{}">', href, extra_classes)

@register.simple_tag
def endlink():
    return format_html("</a>")

@register.simple_tag
def table(default_id, extra_classes=""):
    return format_html('<table id="{}" class="{}" style="90%;">', default_id, extra_classes)

@register.simple_tag
def endtable():
    return format_html("</table>")

@register.simple_tag
def tbody(extra_classes=""):
    return format_html('<tbody class="{}">', extra_classes)

@register.simple_tag
def endtbody():
    return format_html("</tbody>")

@register.simple_tag
def table_row(extra_classes=""):
    return format_html('<tr class="{}">', extra_classes)

@register.simple_tag
def endtable_row():
    return format_html("</tr>")

@register.simple_tag
def table_col(extra_classes=""):
    return format_html('<td class="{}">', extra_classes)

@register.simple_tag
def endtable_col():
    return format_html("</td>")
