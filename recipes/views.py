from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm, SaveForm, RecipeFilterForm
from .filters import RecipeFilter
from django.contrib.auth import get_user_model
import django_filters


class HomeView(generic.TemplateView):
    """
    render landing page
    """
    template_name = 'home.html'


class RecipeList(generic.ListView):
    """
    List 9 recipes per page with the ability to filter by:
        -recipe name that contains entered characters
        -meal type
        -difficulty
    """
    model = Recipe
    queryset = Recipe.objects.all().order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 9
    form_class = RecipeFilterForm
    context_object_name = 'recipes'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = RecipeFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context


class RecipeDetail(generic.DetailView):
    """
    Render a detailed page of a recipe
    with existing comments
    also in this view:
        -crud functionality for recipes
        -crud functionality for comments
    """
    model = Recipe
    template_name = "recipe_detail.html"
    context_object_name = "recipe"
    slug = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments \
            .all().order_by("created_on")
        context["deleted_comment"] = False
        context["comment_form"] = CommentForm()
        context["date_added"] = self.object.created_on.strftime('%B %d, %Y')
        if self.object.saves.filter(id=self.request.user.id).exists():
            context["saved"] = True
        return context

    def post(self, request, slug, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        saved = context.get("saved", False)

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = self.object
            comment.save()
            context["comment_form"] = CommentForm()
            messages.success(
                self.request, 'You added a comment'
            )
        else:
            context["comment_form"] = comment_form

        return self.render_to_response(context)


class RecipeCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Rendering the form for creating a recipe
    """
    model = Recipe
    template_name = 'recipe_form.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipes')
    success_message = 'Your recipe has been created successfully!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.recipe_name)
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, generic.UpdateView):
    """
    Rendering the form of a selected recipe with prepopulated fields
    for editing purposes
    """
    model = Recipe
    template_name = 'recipe_form_edit.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipes')
    success_message = 'Your recipe has been updated successfully!'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.recipe_name)
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class RecipeDeleteView(LoginRequiredMixin, generic.DeleteView):
    """
    Delete functionality for recipe objects
    """
    model = Recipe
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('recipes')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Recipe has been deleted successfully.")
        return super().delete(request, *args, **kwargs)


class CommentUpdateView(LoginRequiredMixin, generic.UpdateView):
    """
    Rendering the form of a selected comment with prepopulated fields
    for editing purposes
    """
    model = Comment
    template_name = 'comment_form.html'
    form_class = CommentForm
    success_url = reverse_lazy('recipes')
    success_message = 'Your comment has been updated successfully!'

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class CommentDeleteView(LoginRequiredMixin, generic.DeleteView):
    """
    Delete functionality for recipe objects
    """
    model = Comment
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('recipes')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Comment has been deleted successfully.")
        return super().delete(request, *args, **kwargs)


class UserProfileView(LoginRequiredMixin, generic.ListView):
    """
    Rendering the user's created and saved recipes in a table
    credit:
    https://stackoverflow.com/questions/48872380/display-multiple-queryset-in-list-view
    """
    template_name = 'profile.html'
    context_object_name = 'my_recipes'

    def get_queryset(self):
        queryset = {
            'created': Recipe.objects.filter(author=self.request.user),
            'saved': Recipe.objects.filter(saves=self.request.user)
        }
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_user_model().objects.get(id=self.request.user.id)
        context['date_joined'] = user.date_joined.strftime('%B %d, %Y')
        return context


class SaveRecipe(View):

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.saves.filter(id=request.user.id).exists():
            success_message = '''
            {recipe_name} has been removed from your saved recipes!
            '''
            recipe.saves.remove(request.user)
            message = success_message.format(recipe_name=recipe.recipe_name)
            messages.success(request, message)
        else:
            success_message = '''
            {recipe_name} has been added to your saved recipes!
            '''
            recipe.saves.add(request.user)
            message = success_message.format(recipe_name=recipe.recipe_name)
            messages.success(request, message)
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
