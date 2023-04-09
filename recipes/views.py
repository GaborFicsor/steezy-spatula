from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm


class HomeView(generic.TemplateView):
    template_name = 'home.html'

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 9

class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "commented": False,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "commented": True,
                "comment_form": CommentForm()
            },
        )


class RecipeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Recipe
    template_name = 'recipe_form.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipes')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.recipe_name)
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Recipe
    template_name = 'recipe_form.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipes')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.recipe_name)
        return super().form_valid(form)


class RecipeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('recipes')

class CommentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Comment
    template_name = 'comment_form.html'
    form_class = CommentForm
    success_url = reverse_lazy('recipes')

    def form_valid(self, form):

        return super().form_valid(form)

class CommentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Comment
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('recipes')
