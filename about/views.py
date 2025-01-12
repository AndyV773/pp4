from django.shortcuts import render
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
    channel_list = Channel.objects.all()

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
    contact_form = ContactForm(data=request.POST)
    if contact_form.is_valid():
        contact_form.save()

    channel_list = Channel.objects.all()
    contact_form = ContactForm()        

    return render(
            request,
            "about/contact.html",
            {
                "channel_list": channel_list,
                "contact_form": contact_form,
            },  # context
        )
