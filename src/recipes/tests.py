from django.test import TestCase
from .models import Recipes

class RecipesModelTest(TestCase):

  def setUpTestData():
    Recipes.objects.create(name='cookies', ingredients='sugar, butter, flour, chocolate chips, eggs', cooking_time=15)

  def test_recipes_name(self):
    recipe = Recipes.objects.get(id=1)
    field_label = recipe._meta.get_field('name').verbose_name
    self.assertEqual(field_label, 'name')

  def test_recipe_name_max_length(self):
    recipe = Recipes.objects.get(id=1)
    max_length = recipe._meta.get_field('name').max_length
    self.assertEqual(max_length, 80)

  def test_recipe_cooking_time(self):
    recipe = Recipes.objects.get(id=1)
    field_label = recipe._meta.get_field('cooking_time').verbose_name
    self.assertEqual(field_label, 'cooking time')

  def test_get_absolute_url(self):
    recipe = Recipes.objects.get(id=1)
    self.assertEqual(recipe.get_absolute_url(), '/list/1')
  
  def test_difficulty_calculation(self):
    recipe = Recipes.objects.get( id=1)
    self.assertEqual(recipe.calculate_difficulty(), 'Hard')