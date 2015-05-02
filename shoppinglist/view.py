from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from shoppinglist.models import ShoppingList, Ingredient

shoppinglists = Blueprint('shoppinglists', __name__, template_folder='templates')


class ListView(MethodView):

    def get(self):
        shoppinglists = ShoppingList.objects.all()
        return render_template('posts/list.html', shoppinglists=shoppinglists)


class DetailView(MethodView):

    def get(self, slug):
        shoppinglist = ShoppingList.objects.get_or_404(slug=slug)
        return render_template('posts/detail.html', shoppinglist=shoppinglist)


# Register the urls
shoppinglists.add_url_rule('/', view_func=ListView.as_view('list'))
shoppinglists.add_url_rule('/<slug>/', view_func=DetailView.as_view('detail'))

