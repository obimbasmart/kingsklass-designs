FOOTER_QUICK_LINKS = [

    {"name": "Home", "link": "/", "is_protected": False},
    {"name": "Products", "link": "/products", "is_protected": False},
    {"name": "Orders", "link": "/orders", "is_protected": True},
    {"name": "About Us", "link": "/aboutus", "is_protected": False},
    # Add more links as needed
]

FOOTER_SUPPORT_LINKS = [

    {"name": "Privacy Policy", "link": "/privacyPolicy"},
    {"name": "Return & Refund Policy", "link": "/refund"},
    {"name": "FAQ", "link": "/faq"},
    # Add more "link"s as needed
]


USER_NAV_LINKS = [

    {"name": "Home", "link": "/", "is_protected": 0},
    {"name": "Products", "link": "/products", "is_protected": 0},
    {"name": "Orders", "link": "/orders", "is_protected": 1},
    {"name": "About Us", "link": "/aboutus", "is_protected": 0},
    # Add more "link"s as needed
]

ADMIN_NAV_LINKS = [

    {"name": "Privacy Policy", "link": "/privacyPolicy"},
    {"name": "Return & Refund Policy", "link": "/refund"},
    {"name": "FAQ", "link": "/faq"},
    # Add more "link"s as needed
]

AdminNavLinks = [
    {"name": "Dashboard", "link": "/dashboard"},
    {"name": "Upload product", "link": "/uploadProduct"},
    {"name": "Manage orders", "link": "/adminOrders"},
    {"name": "Contacts", "link": "/#contactUs"},
]


measurement_names = [
    "chest_burst", "stomach", "top_length", "shoulder",
    "sleeve_length", "neck", "muscle", "waist", "laps", "knee"
]


default_measurement = {
    name: 0.0 for name in measurement_names
}
