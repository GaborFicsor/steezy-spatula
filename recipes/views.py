from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Comment, UserProfile
from .forms import CommentForm, RecipeForm, SaveForm, RecipeFilterForm
from .filters import RecipeFilter
from django.contrib.auth import get_user_model
import django_filters


class HomeView(generic.TemplateView):
    template_name = 'home.html'

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 9
    form_class = RecipeFilterForm

    queryset = Recipe.objects.all()
    context_object_name = 'recipes'

    def get_queryset(self):
        queryset = super().get_queryset()
        # self.filterset = RecipeFilter(self.request.GET, queryset=queryset)
        self.filterset = RecipeFilter(self.request.GET, queryset=queryset)
        # return self.filterset.qs
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context


class RecipeDetail(generic.DetailView):
    model = Recipe
    template_name = "recipe_detail.html"
    context_object_name = "recipe"
    slug = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.filter(approved=True).order_by("created_on")
        context["commented"] = False
        context["comment_form"] = CommentForm()
        if self.object.likes.filter(id=self.request.user.id).exists():
            context["liked"] = True
        if self.object.saves.filter(id=self.request.user.id).exists():
            context["saved"] = True
        return context

    def post(self, request, slug, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        liked = context.get("liked", False)
        saved = context.get("saved", False)

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = self.object
            comment.save()
            context["commented"] = True
            context["comment_form"] = CommentForm()
        else:
            context["comment_form"] = comment_form

        return self.render_to_response(context)


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

class UserProfileView(LoginRequiredMixin, generic.ListView):

    # https://stackoverflow.com/questions/48872380/display-multiple-queryset-in-list-view
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

class DashBoardView(LoginRequiredMixin, generic.ListView):
    template_name = 'dashboard.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['approved_comments'] = Comment.objects.filter(approved=True)
        context['not_approved_comments'] = Comment.objects.filter(approved=False)
        return context


    def get_queryset(self):
        queryset = {
            'approved': Recipe.objects.filter(status=1),
            'not_approved': Recipe.objects.filter(status=0)
        }
        return queryset


class SaveRecipe(View):

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.saves.filter(id=request.user.id).exists():
            recipe.saves.remove(request.user)
        else:
            recipe.saves.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


