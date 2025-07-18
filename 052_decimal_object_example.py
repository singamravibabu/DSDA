from decimal import Decimal

order_total = Decimal('100.05')
discount_percent = Decimal('0.10')
discount = order_total * discount_percent
subtotal = order_total - discount
tax_percent = Decimal('0.05')
sales_tax = subtotal * tax_percent
invoice_total = subtotal + sales_tax
print("Invoice Total:", invoice_total)