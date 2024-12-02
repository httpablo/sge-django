from django.test import TestCase
from products.models import Product
from categories.models import Category
from brands.models import Brand
from datetime import datetime
from time import sleep

class TestProductModel(TestCase):
    """
    Classe de testes para o modelo Product
    """
    def setUp(self):
        self.category = Category.objects.create(name="Category Test", description="Test Category Description")
        self.brand = Brand.objects.create(name="Brand Test", description="Test Brand Description")
        self.product = Product.objects.create(
            title="Test Product",
            category=self.category,
            brand=self.brand,
            description="Test Product Description",
            serie_number="12345",
            cost_price=100.00,
            selling_price=150.00,
            quantity=10,
        )

    def test_create_product(self):
        """
        Testa a criação de um produto
        """
        self.assertEqual(self.product.title, "Test Product")
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.brand, self.brand)
        self.assertEqual(self.product.cost_price, 100.00)
        self.assertEqual(self.product.selling_price, 150.00)
        self.assertEqual(self.product.quantity, 10)

    def test_update_product_updates_update_at_field(self):
        """
        Testa se o campo `update_at` é atualizado após uma modificação no modelo.
        """
        old_update_at = self.product.update_at
        sleep(1)
        self.product.title = "Updated Test Product"
        self.product.save()
        self.assertNotEqual(self.product.update_at, old_update_at)

    def test_edit_product(self):
        """
        Testa a edição de um produto
        """
        self.product.title = "Updated Product Title"
        self.product.selling_price = 200.00
        self.product.save()
        
        updated_product = Product.objects.get(pk=self.product.pk)
        self.assertEqual(updated_product.title, "Updated Product Title")
        self.assertEqual(updated_product.selling_price, 200.00)

    def test_delete_product(self):
        """
        Testa a exclusão de um produto
        """
        product_id = self.product.pk
        self.product.delete()

        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(pk=product_id)
