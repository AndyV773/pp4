from django.shortcuts import render

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

    return render(
            request,
            "about/about.html",
            {
               
            },  # context
        )
