from django.test import TestCase
from suppliers.models import Supplier
from time import sleep


class TestSupplierModel(TestCase):
    """
    Classe de testes para o modelo Supplier
    """
    def setUp(self):
        self.supplier = Supplier.objects.create(
            name="Test Supplier",
            description="Test Supplier Description"
        )

    def test_create_supplier(self):
        """
        Testa a criação de um fornecedor
        """
        self.assertEqual(self.supplier.name, "Test Supplier")
        self.assertEqual(self.supplier.description, "Test Supplier Description")

    def test_update_supplier_updates_update_at_field(self):
        """
        Testa se o campo `update_at` é atualizado após uma modificação no modelo.
        """
        old_update_at = self.supplier.update_at
        sleep(1)
        self.supplier.name = "Updated Test Supplier"
        self.supplier.save()
        self.assertNotEqual(self.supplier.update_at, old_update_at)

    def test_edit_supplier(self):
        """
        Testa a edição de um fornecedor
        """
        self.supplier.name = "Updated Supplier Name"
        self.supplier.description = "Updated Supplier Description"
        self.supplier.save()

        updated_supplier = Supplier.objects.get(pk=self.supplier.pk)
        self.assertEqual(updated_supplier.name, "Updated Supplier Name")
        self.assertEqual(updated_supplier.description, "Updated Supplier Description")

    def test_delete_supplier(self):
        """
        Testa a exclusão de um fornecedor
        """
        supplier_id = self.supplier.pk
        self.supplier.delete()

        with self.assertRaises(Supplier.DoesNotExist):
            Supplier.objects.get(pk=supplier_id)
