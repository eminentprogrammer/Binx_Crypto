import datetime
from django import template
from django.shortcuts import reverse
from django.utils.html import format_html
from .. import settings
from django.utils.crypto import get_random_string
from apps.paystack.utils import get_js_script


register = template.Library()

# from store.models import Payment

@register.inclusion_tag('paystack_button.html', takes_context=True)
def paystack_button(context, button_id="django-paystack-button", button_class="", amount=None, ref=None, email=None, redirect_url=None):

    # print("calling Paystack button")
    new_ref = ref
    # print("Paystack Button Ref: ", new_ref)

    # obj = Payment.objects.get(ref=ref)
    new_redirect_url = redirect_url
    new_amount = int(amount) * 100 
    
    # Pass    
    if not new_ref:
        new_ref = get_random_string(length=12, allowed_chars="01234567899abcdef").upper()
    
    if not new_redirect_url:
        new_redirect_url = "{}?amount={}".format(
            reverse('paystack:verify_payment', args=[new_ref]), new_amount)

    return {
        'button_class': button_class,
        'button_id': button_id,
        'key': settings.PAYSTACK_PUBLIC_KEY,
        'ref': new_ref,
        'email': email,
        'amount': new_amount,
        'redirect_url': new_redirect_url,
        'js_url': get_js_script()
    }
