from django.test import TestCase
from categories.models import Category
from time import sleep


class TestCategoryModel(TestCase):
    """
    Classe de testes para o modelo Category
    """
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
            description="Test Category Description"
        )

    def test_create_category(self):
        """
        Testa a criação de uma categoria
        """
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(self.category.description, "Test Category Description")

    def test_update_category_updates_update_at_field(self):
        """
        Testa se o campo `update_at` é atualizado após uma modificação no modelo.
        """
        old_update_at = self.category.update_at
        sleep(1)
        self.category.name = "Updated Test Category"
        self.category.save()
        self.assertNotEqual(self.category.update_at, old_update_at)

    def test_edit_category(self):
        """
        Testa a edição de uma categoria
        """
        self.category.name = "Updated Category Name"
        self.category.description = "Updated Category Description"
        self.category.save()

        updated_category = Category.objects.get(pk=self.category.pk)
        self.assertEqual(updated_category.name, "Updated Category Name")
        self.assertEqual(updated_category.description, "Updated Category Description")

    def test_delete_category(self):
        """
        Testa a exclusão de uma categoria
        """
        category_id = self.category.pk
        self.category.delete()

        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(pk=category_id)
