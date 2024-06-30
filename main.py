# Define necessary classes (example using basic Python classes)

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class Invoice:
    def __init__(self, invoice_id, customer, products):
        self.invoice_id = invoice_id
        self.customer = customer
        self.products = products
        self.total = sum(product.price for product in products)

    def generate_invoice(self):
        invoice_str = f"Invoice ID: {self.invoice_id}\n"
        invoice_str += f"Customer: {self.customer.name}\n"
        invoice_str += "Products:\n"
        for product in self.products:
            invoice_str += f"- {product.name}: ${product.price}\n"
        invoice_str += f"Total: ${self.total}\n"
        return invoice_str

# Example usage:
if __name__ == "__main__":
    # Create customers
    customer1 = Customer("John Doe", "john@example.com", "123 Main St, City")

    # Create products
    product1 = Product("P001", "Laptop", 1200)
    product2 = Product("P002", "Mouse", 20)
    product3 = Product("P003", "Keyboard", 100)

    # Create an invoice
    invoice1 = Invoice("INV001", customer1, [product1, product2, product3])

    # Generate and print the invoice
    print(invoice1.generate_invoice())