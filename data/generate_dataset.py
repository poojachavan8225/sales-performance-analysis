from faker import Faker
import pandas as pd
import random

fake = Faker('en_IN')

# ------------------
# Customers
# ------------------
customers = []

for i in range(1, 1001):
    customers.append({
        "Customer_ID": i,
        "Name": fake.name(),
        "Email": fake.email(),
        "City": fake.city(),
        "State": fake.state(),
        "Registration_Date": fake.date_between(
            start_date='-3y',
            end_date='today'
        )
    })

customers_df = pd.DataFrame(customers)

# ------------------
# Products
# ------------------
categories = {
    "Electronics": [
        "Laptop",
        "Mobile",
        "Tablet",
        "Headphones"
    ],
    "Fashion": [
        "T-Shirt",
        "Jeans",
        "Shoes"
    ],
    "Home": [
        "Chair",
        "Table",
        "Lamp"
    ]
}

products = []
pid = 1

for category, items in categories.items():
    for item in items:
        products.append({
            "Product_ID": pid,
            "Product_Name": item,
            "Category": category,
            "Price": random.randint(500, 50000)
        })
        pid += 1

products_df = pd.DataFrame(products)

# ------------------
# Orders
# ------------------
orders = []

for oid in range(1, 5001):
    orders.append({
        "Order_ID": oid,
        "Customer_ID": random.randint(1, 1000),
        "Order_Date": fake.date_between(
            start_date='-2y',
            end_date='today'
        ),
        "Order_Status": random.choice([
            "Delivered",
            "Cancelled",
            "Returned",
            "Shipped"
        ])
    })

orders_df = pd.DataFrame(orders)

# ------------------
# Order Items
# ------------------
order_items = []

for oid in orders_df["Order_ID"]:

    for _ in range(random.randint(1, 4)):

        product = products_df.sample(1).iloc[0]

        qty = random.randint(1, 5)

        order_items.append({
            "Order_ID": oid,
            "Product_ID": product["Product_ID"],
            "Quantity": qty,
            "Revenue": qty * product["Price"]
        })

order_items_df = pd.DataFrame(order_items)

# ------------------
# Save CSV Files
# ------------------

customers_df.to_csv(
    "customers.csv",
    index=False
)

products_df.to_csv(
    "products.csv",
    index=False
)

orders_df.to_csv(
    "orders.csv",
    index=False
)

order_items_df.to_csv(
    "order_items.csv",
    index=False
)

print("Dataset Generated Successfully!")