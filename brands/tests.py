from django.test import TestCase
from time import sleep
from brands.models import Brand


class TestBrandModel(TestCase):
    """
    Classe de testes para o modelo Brand.
    """
    def setUp(self):
        self.brand = Brand.objects.create(
            name="Test Brand",
            description="Description for test brand"
        )

    def test_created_at_and_updated_at(self):
        """
        Testa os campos `created_at` e `update_at` para confirmar se foram populados corretamente.
        """
        self.assertIsNotNone(self.brand.created_at)
        self.assertIsNotNone(self.brand.update_at)
        self.assertLessEqual(self.brand.created_at, self.brand.update_at)

    def test_blank_and_null_description(self):
        """
        Testa se a descrição aceita valores nulos e vazios.
        """
        brand_with_no_description = Brand.objects.create(name="No Description Brand")
        self.assertIsNone(brand_with_no_description.description)

    def test_updating_brand_updates_update_at_field(self):
        """
        Testa se o campo `update_at` é atualizado após uma modificação no modelo.
        """
        old_update_at = self.brand.update_at
        sleep(1)
        self.brand.name = "Updated Brand Name"
        self.brand.save()
        self.assertNotEqual(self.brand.update_at, old_update_at)
