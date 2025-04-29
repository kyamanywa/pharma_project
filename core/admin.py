from django.contrib import admin
from .models import RawMaterial, User, ManufacturingAndProduction, PackagingAndLabeling, QualityControlAndTesting
from .models import ShippingAndDistribution 
admin.site.site_header = "Kampala Pharmaceutical Industry Management System (KPIM)"
admin.site.site_title = "KPIM Admin"
admin.site.index_title = "Welcome to KPIM Dashboard"


admin.site.register(RawMaterial)
admin.site.register(User)
admin.site.register( ManufacturingAndProduction)
admin.site.register(PackagingAndLabeling)
admin.site.register(QualityControlAndTesting)
admin.site.register(ShippingAndDistribution)
# To get a system dashboard, you can use Django's built-in admin interface.
# Ensure you have created a superuser to access the admin dashboard.
# Run the following command in your terminal to create a superuser:
# python manage.py createsuperuser

# After creating the superuser, run the development server:
# python manage.py runserver

# Access the admin dashboard by navigating to http://127.0.0.1:8000/admin in your browser.