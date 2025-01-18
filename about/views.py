from django.shortcuts import render, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import About
from .forms import ContactForm
from crypto.models import Channel


# Create your views here.
def about_me(request):
    """
    Renders the most recent information on the website author
    and allows user collaboration requests
    Displays an individual instance of :model:`about.About`.
    **Context**

    **Template:**
    :template:`about/about.html`
    """
    channel_list = Channel.objects.filter(approved=True)

    return render(
            request,
            "about/about.html",
            {
                "channel_list": channel_list,
            },  # context
        )


def contact_me(request):
    """
    Allows user to make a contact requests
    **Context**

    **Template:**
    :template:`about/contact.html`
    """

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                    request, messages.SUCCESS,
                    'Message sent'
                )
            return HttpResponseRedirect(reverse('contact'))
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error message did not send!')

    # to initiate contact form data fields for authenticated user
    contact_form = ContactForm(
        initial={
            'name': request.user
            if request.user.is_authenticated else '',
            'email': request.user.email
            if request.user.is_authenticated else '',
            'message': '',
            })

    channel_list = Channel.objects.filter(approved=True)

    return render(
            request,
            "about/contact.html",
            {
                "channel_list": channel_list,
                "contact_form": contact_form,
            },  # context
        )
