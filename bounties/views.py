from django.shortcuts import render
from .forms import NewBountyForm
from .models import Bounty

from django.http import HttpResponse  # obsolete

# Hello, I'm changing this comment again to see that it show up in the repo ok

# Create new bounty
def create_bounty(request):
    #return HttpResponse("This creates a bounty")
    
    # arguments to be passed to template
    arguments = dict()
    
    if request.method == 'POST':
        '''Try to create a new bounty'''
        form = NewBountyForm(request.POST)
        if form.is_valid():
            
            # form data
            company = None  # TODO: Add the selected company          
            title = request.POST['title']
            description = request.POST['description']
            size = request.POST['size']
            
            # create new bounty
            bounty = Bounty(company=company, 
                            title=title,
                            description=description,
                            size=size)  #user_id=user.id            
            bounty.save()
            request.session['selected_bounty'] = bounty.id
            
            arguments['status'] = 'New bounty created'
        else:
            arguments['status'] = 'Invalid form'
    else:
        '''Use an empty form'''
        form = NewBountyForm()
        arguments['status'] = ''
    

    arguments['form'] = form
    
    return render(request, 'bounties/create_bounty.html', arguments)    
