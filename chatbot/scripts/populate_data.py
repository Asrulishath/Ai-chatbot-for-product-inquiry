from chatbot.models import Supplier, Product

def run():
    supplier1 = Supplier.objects.create(
        name="Tech Suppliers Inc.",
        contact_info="123 Main Street, tech@example.com",
        product_categories_offered="laptops, monitors"
    )

    Product.objects.create(
        name="Laptop Pro X",
        brand="Brand X",
        price=1200.00,
        category="laptops",
        description="A high-end laptop with excellent performance.",
        supplier=supplier1
    )

    print("Data populated successfully.")

if __name__ == "__main__":
    run()
