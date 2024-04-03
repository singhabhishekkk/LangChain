from django.shortcuts import render,redirect
from django.views import View
from masterchefapp.forms import RecipeForm
from masterchefapp.langchain import askMasterChef


# Create your views here.
class Home(View):
    def get(self,request):
        ai_recipe = request.session_get('ai_recipe',"")
        return render(request,"masterchefapp/home.html",{'form':RecipeForm,"ai_recipe":ai_recipe} )
    
    
    
    def post(self,request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe_message = form.cleaned_data['recipe_message']
            ai_response = askMasterChef(recipe_message)
            # store in session
            request.session['ai_recipe'] = ai_response
            
        form = RecipeForm()
        return redirect('/')
    