#!/usr/bin/env python
"""
Run this script to seed the database with sample data.
Usage: python seed_data.py
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.contrib.auth.models import User
from store.models import Category, Product, UserProfile

# Categories
categories_data = [
    {'name': 'Electronics', 'slug': 'electronics'},
    {'name': 'Clothing', 'slug': 'clothing'},
    {'name': 'Books', 'slug': 'books'},
    {'name': 'Home & Garden', 'slug': 'home-garden'},
    {'name': 'Sports', 'slug': 'sports'},
]

categories = {}
for c in categories_data:
    cat, _ = Category.objects.get_or_create(slug=c['slug'], defaults={'name': c['name']})
    categories[c['slug']] = cat
    print(f"✓ Category: {cat.name}")

# Products
products_data = [
    {'name': 'Wireless Headphones', 'slug': 'wireless-headphones', 'category': 'electronics',
     'description': 'Premium noise-cancelling wireless headphones with 30-hour battery life and crystal-clear audio. Features Bluetooth 5.0, foldable design, and a comfortable over-ear fit perfect for long listening sessions.',
     'price': '89.99', 'stock': 50},
    {'name': 'Mechanical Keyboard', 'slug': 'mechanical-keyboard', 'category': 'electronics',
     'description': 'Compact TKL mechanical keyboard with tactile switches, RGB backlighting, and a durable aluminum frame. N-key rollover for precise gaming and typing performance.',
     'price': '129.99', 'stock': 30},
    {'name': 'USB-C Hub 7-in-1', 'slug': 'usb-c-hub', 'category': 'electronics',
     'description': 'Expand your laptop\'s connectivity with this compact 7-in-1 USB-C hub. Includes 4K HDMI, 3× USB-A, SD card reader, and 100W PD charging.',
     'price': '49.99', 'stock': 75},
    {'name': 'Classic Cotton T-Shirt', 'slug': 'classic-tshirt', 'category': 'clothing',
     'description': '100% organic cotton crew-neck T-shirt. Pre-shrunk, lightweight, and available in a range of modern colours. A wardrobe staple.',
     'price': '24.99', 'stock': 200},
    {'name': 'Slim Fit Chinos', 'slug': 'slim-chinos', 'category': 'clothing',
     'description': 'Versatile slim-fit chino trousers made from stretch-cotton blend. Perfect for both casual and smart-casual occasions.',
     'price': '59.99', 'stock': 80},
    {'name': 'Lightweight Running Jacket', 'slug': 'running-jacket', 'category': 'clothing',
     'description': 'Breathable, wind-resistant running jacket with reflective details and a packable design. Keeps you comfortable during outdoor workouts in any weather.',
     'price': '79.99', 'stock': 45},
    {'name': 'Python Programming Mastery', 'slug': 'python-book', 'category': 'books',
     'description': 'A comprehensive guide to Python from beginner to advanced. Covers data structures, OOP, web development with Django, and data science fundamentals. Over 600 pages with hands-on projects.',
     'price': '39.99', 'stock': 120},
    {'name': 'The Art of Deep Work', 'slug': 'deep-work-book', 'category': 'books',
     'description': 'A practical guide to cultivating focused, distraction-free work habits in an age of constant digital noise. Essential reading for knowledge workers.',
     'price': '18.99', 'stock': 90},
    {'name': 'Stainless Steel Water Bottle', 'slug': 'water-bottle', 'category': 'home-garden',
     'description': 'Double-walled vacuum-insulated 750ml water bottle. Keeps drinks cold 24 hours, hot 12 hours. BPA-free, leak-proof lid, and dishwasher-safe base.',
     'price': '34.99', 'stock': 150},
    {'name': 'Bamboo Desk Organiser', 'slug': 'desk-organiser', 'category': 'home-garden',
     'description': 'Stylish and sustainable bamboo desk organiser with multiple compartments for pens, notebooks, and accessories. Keeps your workspace tidy and eco-friendly.',
     'price': '29.99', 'stock': 60},
    {'name': 'Adjustable Dumbbell Set', 'slug': 'dumbbell-set', 'category': 'sports',
     'description': 'Space-saving adjustable dumbbell pair — 2.5 kg to 25 kg per hand in seconds. Quick-lock dial mechanism with non-slip grip. Perfect for home gym workouts.',
     'price': '199.99', 'stock': 25},
    {'name': 'Yoga Mat Pro', 'slug': 'yoga-mat', 'category': 'sports',
     'description': 'Extra-thick 6mm non-slip yoga mat made from eco-friendly TPE foam. Includes alignment lines, carrying strap, and is sweat-resistant for intense sessions.',
     'price': '44.99', 'stock': 100},
]

for p in products_data:
    cat = categories[p['category']]
    prod, created = Product.objects.get_or_create(
        slug=p['slug'],
        defaults={
            'name': p['name'],
            'category': cat,
            'description': p['description'],
            'price': p['price'],
            'stock': p['stock'],
            'is_active': True,
        }
    )
    print(f"{'✓ Created' if created else '— Exists'}: {prod.name}")

# Admin user
if not User.objects.filter(username='admin').exists():
    admin = User.objects.create_superuser('admin', 'admin@shopease.com', 'admin123')
    UserProfile.objects.create(user=admin)
    print("\n✓ Admin user created: admin / admin123")
else:
    print("\n— Admin user already exists")

print(f"\n✅ Seed complete! {Product.objects.count()} products, {Category.objects.count()} categories.")
