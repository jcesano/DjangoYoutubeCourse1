# scripts/create_products_dataset.py

from products.models import Product

def run():
    # Fetch all questions
    
    Product.objects.all().delete()
    # Delete one product from databaset
    products = Product.objects.all()
    products.create(title = "automated test case 1", description = "test case added from created_products_dataset script", price = 123.23, summary = "avoiding leaving this field blank")
    products.create(title = "automated test case 2", description = "test case added from created_products_dataset script", price = 124.23, summary = "avoiding leaving this field blank")
    products.create(title = "automated test case 3", description = "test case added from created_products_dataset script", price = 125.23, summary = "avoiding leaving this field blank")
    products.create(title = "automated test case 4", description = "test case added from created_products_dataset script", price = 126.23, summary = "avoiding leaving this field blank")
    for item in products:
        item.save()