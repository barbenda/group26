import os
import pymongo
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# get your uri from .env file
load_dotenv()
uri = os.getenv('DB_URI')

# create cluster
cluster = MongoClient(uri, server_api=ServerApi('1'))

# get all dbs and collestions that needed
db = cluster['mydatabase']
customers_col = db['customers']
products_col = db["products"]   # טבלת מוצרים
orders_col = db["orders"]       # טבלת הזמנות
favorites_col = db["favorites"] # טבלת מועדפים
cart_col = db["cart"]           # טבלת עגלת קניות

# customers_col.insert_many([
#     {"_id": 1, "name": "John Doe", "email": "john@example.com", "password": "hashedpassword123"},
#     {"_id": 2, "name": "Jane Smith", "email": "jane@example.com", "password": "hashedpassword456"}
# ])
#
# products_col.insert_many([
# {"_id": 114, "name": "Black Casual Shirt", "category": "TOPS", "price": 200, "image": "images/top4.jpg",
#      "sizes": {"S": 8, "M": 10, "L": 6, "XL": 3}, "description": "A casual black shirt.", "size_fit": "Runs small",
#      "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 115, "name": "Royal Blue Ruffle Top", "category": "TOPS", "price": 250, "image": "images/top5.png",
#      "sizes": {"S": 10, "M": 15, "L": 10, "XL": 5}, "description": "Stylish blue ruffle top.", "size_fit": "True to size",
#      "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 116, "name": "Gray Elegant Top", "category": "TOPS", "price": 190, "image": "images/top6.png",
#      "sizes": {"S": 7, "M": 12, "L": 9, "XL": 6}, "description": "A chic gray top.", "size_fit": "True to size",
#      "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 117, "name": "Navy Blue Striped Shirt", "category": "TOPS", "price": 220, "image": "images/top7.jpg",
#      "sizes": {"S": 8, "M": 14, "L": 10, "XL": 6}, "description": "Classic navy striped shirt.", "size_fit": "Runs large",
#      "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 118, "name": "Sky Blue Relaxed Shirt", "category": "TOPS", "price": 160, "image": "images/top8.jpg",
#      "sizes": {"S": 5, "M": 9, "L": 7, "XL": 4}, "description": "Casual sky blue shirt.", "size_fit": "True to size",
#      "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 119, "name": "White Sleek Blouse", "category": "TOPS", "price": 210, "image": "images/top9.jpg",
#      "sizes": {"S": 6, "M": 12, "L": 8, "XL": 5}, "description": "Elegant white blouse.", "size_fit": "True to size",
#      "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 1110, "name": "Green Satin Shirt", "category": "TOPS", "price": 300, "image": "images/top10.jpg",
#      "sizes": {"S": 4, "M": 8, "L": 6, "XL": 3}, "description": "Luxury satin shirt.", "size_fit": "Runs small",
#      "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 1111, "name": "Peach Button-Up Top", "category": "TOPS", "price": 240, "image": "images/top11.jpg",
#      "sizes": {"S": 5, "M": 9, "L": 7, "XL": 4}, "description": "Soft peach button-up.", "size_fit": "True to size",
#      "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 1112, "name": "Pink Casual Shirt", "category": "TOPS", "price": 170, "image": "images/top12.jpg",
#      "sizes": {"S": 6, "M": 10, "L": 8, "XL": 5}, "description": "Casual pink shirt.", "size_fit": "True to size",
#      "fast_shipping": True, "easy_returns": True},
#
# # 🔹 DRESSES
#
#
#  {"_id": 224, "name": "Pink Floral Maxi Dress", "category": "DRESSES", "price": 200, "image": "images/dress4.jpg",
#      "sizes": {"S": 7, "M": 10, "L": 9, "XL": 5}, "description": "A gorgeous pink floral maxi dress.",
#      "size_fit": "Fits loosely", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 225, "name": "Yellow Floral Wrap Dress", "category": "DRESSES", "price": 240, "image": "images/dress5.jpg",
#      "sizes": {"S": 6, "M": 8, "L": 6, "XL": 4}, "description": "Bright yellow wrap dress for any occasion.",
#      "size_fit": "True to size", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 226, "name": "Mint Green Tie Dress", "category": "DRESSES", "price": 210, "image": "images/dress6.jpg",
#      "sizes": {"S": 8, "M": 12, "L": 10, "XL": 6}, "description": "A soft mint green dress with tie detail.",
#      "size_fit": "Runs small", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 227, "name": "Burgundy Velvet Gown", "category": "DRESSES", "price": 280, "image": "images/dress7.jpg",
#      "sizes": {"S": 5, "M": 9, "L": 8, "XL": 4}, "description": "A luxurious burgundy velvet evening gown.",
#      "size_fit": "True to size", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 228, "name": "Classic Black Dress", "category": "DRESSES", "price": 230, "image": "images/dress8.jpg",
#      "sizes": {"S": 6, "M": 11, "L": 9, "XL": 5}, "description": "A timeless little black dress.",
#      "size_fit": "Runs small", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 229, "name": "Vintage Floral Dress", "category": "DRESSES", "price": 260, "image": "images/dress9.jpg",
#      "sizes": {"S": 7, "M": 12, "L": 10, "XL": 6}, "description": "A retro-style floral dress.",
#      "size_fit": "Fits loosely", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 2210, "name": "Pastel Green Dress", "category": "DRESSES", "price": 190, "image": "images/dress10.jpg",
#      "sizes": {"S": 5, "M": 10, "L": 8, "XL": 5}, "description": "A soft pastel green dress.",
#      "size_fit": "True to size", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 2211, "name": "Coral Party Dress", "category": "DRESSES", "price": 170, "image": "images/dress11.jpg",
#      "sizes": {"S": 6, "M": 9, "L": 7, "XL": 4}, "description": "A vibrant coral dress for parties.",
#      "size_fit": "Runs large", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 2212, "name": "Red Layered Dress", "category": "DRESSES", "price": 300, "image": "images/dress12.jpg",
#      "sizes": {"S": 5, "M": 8, "L": 6, "XL": 4}, "description": "Elegant layered red dress.",
#      "size_fit": "True to size", "fast_shipping": True, "easy_returns": True},
#
#
# # 🔹 NEW ARRIVALS
#
# {"_id": 333, "name": "Beige Faux Fur Jacket", "category": "NEW ARRIVALS", "price": 320, "image": "images/newArrivals3.jpg",
#      "sizes": {"S": 4, "M": 6, "L": 5, "XL": 3}, "description": "Stylish faux fur jacket in beige.",
#      "size_fit": "True to size", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 334, "name": "Denim Jacket", "category": "NEW ARRIVALS", "price": 270, "image": "images/newArrivals4.jpg",
#      "sizes": {"S": 7, "M": 12, "L": 9, "XL": 5}, "description": "A classic denim jacket for everyday wear.",
#      "size_fit": "True to size", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 335, "name": "Camel Wool Coat", "category": "NEW ARRIVALS", "price": 350, "image": "images/newArrivals5.jpg",
#      "sizes": {"S": 6, "M": 8, "L": 6, "XL": 4}, "description": "Elegant camel wool coat for cold days.",
#      "size_fit": "Runs large", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 336, "name": "Navy Peacoat", "category": "NEW ARRIVALS", "price": 300, "image": "images/newArrivals6.jpg",
#      "sizes": {"S": 5, "M": 9, "L": 7, "XL": 4}, "description": "A warm navy blue peacoat with a modern cut.",
#      "size_fit": "True to size", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 337, "name": "White Casual Tee", "category": "NEW ARRIVALS", "price": 120, "image": "images/newArrivals7.jpg",
#      "sizes": {"S": 8, "M": 12, "L": 10, "XL": 6}, "description": "Basic white casual t-shirt for everyday wear.",
#      "size_fit": "True to size", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 338, "name": "Black Relaxed Tee", "category": "NEW ARRIVALS", "price": 110, "image": "images/newArrivals8.jpg",
#      "sizes": {"S": 5, "M": 8, "L": 6, "XL": 4}, "description": "Relaxed fit black t-shirt.",
#      "size_fit": "Runs large", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 339, "name": "Coral T-Shirt", "category": "NEW ARRIVALS", "price": 140, "image": "images/newArrivals9.jpg",
#      "sizes": {"S": 6, "M": 10, "L": 8, "XL": 5}, "description": "Soft coral t-shirt for a fresh look.",
#      "size_fit": "True to size", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 3310, "name": "Beige Casual Top", "category": "NEW ARRIVALS", "price": 130, "image": "images/newArrivals10.jpg",
#      "sizes": {"S": 7, "M": 9, "L": 6, "XL": 4}, "description": "A lightweight beige casual top.",
#      "size_fit": "Runs small", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 3311, "name": "Floral Blouse", "category": "NEW ARRIVALS", "price": 200, "image": "images/newArrivals11.jpg",
#      "sizes": {"S": 8, "M": 11, "L": 9, "XL": 5}, "description": "A floral blouse with beautiful print.",
#      "size_fit": "True to size", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 3312, "name": "White Floral Tee", "category": "NEW ARRIVALS", "price": 150, "image": "images/newArrivals12.jpg",
#      "sizes": {"S": 6, "M": 10, "L": 8, "XL": 5}, "description": "A cute white tee with floral details.",
#      "size_fit": "True to size", "fast_shipping": True, "easy_returns": True},
#
# # 🔹 DENIM
# {"_id": 5, "name": "Sienna KanCan Jeans - Medium Wash", "category": "DENIM", "price": 255, "image": "images/jeans5.jpg",
#      "sizes": {"26": 9, "28": 11, "30": 6, "32": 5}, "description": "Classic medium wash jeans with stretch fabric.",
#      "size_fit": "Runs small", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 6, "name": "Gemma Risen Denim Jacket - Dusty Mauve", "category": "DENIM", "price": 218, "image": "images/jeans6.jpg",
#      "sizes": {"S": 5, "M": 8, "L": 6, "XL": 3}, "description": "A unique dusty mauve denim jacket.",
#      "size_fit": "True to size", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 7, "name": "Sienna KanCan Jeans - Dark Wash", "category": "DENIM", "price": 255, "image": "images/jeans2.jpg",
#      "sizes": {"26": 10, "28": 13, "30": 7, "32": 6}, "description": "Dark wash jeans for a sleek look.",
#      "size_fit": "Runs large", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 8, "name": "Drake KanCan Jeans", "category": "DENIM", "price": 237, "image": "images/jeans8.jpg",
#      "sizes": {"26": 6, "28": 8, "30": 5, "32": 4}, "description": "Comfortable and stylish jeans with a modern cut.",
#      "size_fit": "True to size", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 9, "name": "Maben Vervet Jeans - Medium Wash", "category": "DENIM", "price": 255, "image": "images/jeans9.jpg",
#      "sizes": {"26": 7, "28": 9, "30": 6, "32": 5}, "description": "Premium medium wash jeans with high durability.",
#      "size_fit": "True to size", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 10, "name": "Khloe Flying Monkey Jeans", "category": "DENIM", "price": 237, "image": "images/jeans10.jpg",
#      "sizes": {"26": 8, "28": 10, "30": 7, "32": 5}, "description": "High-rise Flying Monkey jeans for ultimate comfort.",
#      "size_fit": "Runs small", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 11, "name": "Olivia Vervet Jeans", "category": "DENIM", "price": 255, "image": "images/jeans11.jpg",
#      "sizes": {"26": 9, "28": 12, "30": 8, "32": 6}, "description": "A classic style for any occasion.",
#      "size_fit": "True to size", "fast_shipping": True, "easy_returns": True},
#
#     {"_id": 12, "name": "Jovie Risen Jeans", "category": "DENIM", "price": 229, "image": "images/jeans12.jpg",
#      "sizes": {"26": 5, "28": 8, "30": 6, "32": 4}, "description": "Stretch fit jeans with a modern touch.",
#      "size_fit": "Runs large", "fast_shipping": True, "easy_returns": True}
#  ])
# orders_col.insert_many([
#     {"_id": 1001, "user_id": 1, "order_date": "2025-02-20", "total": 447, "items": [{"product_id": 101, "quantity": 1}, {"product_id": 102, "quantity": 1}]},
#     {"_id": 1002, "user_id": 2, "order_date": "2025-02-18", "total": 99, "items": [{"product_id": 103, "quantity":1}]}
# ])
# favorites_col.insert_many([
#     {"_id": 2001, "user_id": 1, "product_id": 101},
#     {"_id": 2002, "user_id": 2, "product_id":103}
# ])
# cart_col.insert_many([
#     {"_id": 3001, "user_id": 1, "product_id": 102, "quantity": 1},
#     {"_id": 3002, "user_id": 2, "product_id": 103, "quantity":2}
# ])

# create all necessary functions
# def get_list_of_customers():
#     return list(customers_col.find())
#
#
# def insert_customer(customer_dict):
#     customers_col.insert_one(customer_dict)




