import datetime
from flask import url_for
from shoppinglist import db


class Ingredient(db.EmbeddedDocument):
    ingredient = db.StringField(max_length=255, required=True)
    quantity = db.StringField(max_length=255)
    category = db.StringField(max_length=255, required=True)

class ShoppingList(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True)
    ingredients = db.ListField(db.EmbeddedDocumentField('Ingredient'))

    def get_absolute_url(self):
        return url_for('post', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True
    }
