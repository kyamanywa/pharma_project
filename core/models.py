from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('editor', 'Editor'),
        ('readonly', 'Read-only'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='readonly')

    def __str__(self):
        return f"{self.username} ({self.role})"

class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)
    received_date = models.DateField()
    quantity_kg = models.DecimalField(max_digits=10, decimal_places=2)
    quality_check_passed = models.BooleanField(default=False)
    inspection_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} from {self.supplier} on {self.received_date}"

class ManufacturingAndProduction(models.Model):
    batch_number = models.CharField(max_length=100, unique=True)
    product_name = models.CharField(max_length=100)
    production_date = models.DateField()
    quality_check_passed = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Batch {self.batch_number} - {self.product_name} produced on {self.production_date}"

# Phase 1: Packaging and Labeling
class PackagingAndLabeling(models.Model):
    medicine_name = models.CharField(max_length=100)
    batch_number = models.CharField(max_length=100, unique=True)
    package_date = models.DateField()
    package_time = models.TimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.medicine_name} packaged on {self.package_date} at {self.package_time} (Batch: {self.batch_number})"

# Phase 2: Quality Control and Testing
class QualityControlAndTesting(models.Model):
    product_name = models.CharField(max_length=100)
    batch_number = models.CharField(max_length=100)
    test_date = models.DateField()
    passed_tests = models.BooleanField(default=False)
    certifications = models.TextField(blank=True, null=True)
    test_results_summary = models.TextField(blank=True, null=True)
    tested_by = models.CharField(max_length=100)

    def __str__(self):
        return f"Quality Control for {self.product_name} - Batch {self.batch_number} on {self.test_date} - Passed: {self.passed_tests}"

# Phase 3: Shipping and Distribution
class ShippingAndDistribution(models.Model):
    product_name = models.CharField(max_length=100)
    batch_number = models.CharField(max_length=100)
    destination = models.CharField(
        max_length=100,
        choices=[
            ("Hospital", "Hospital"),
            ("School", "School"),
            ("Pharmacy", "Pharmacy"),
            ("Clinic", "Clinic"),
            ("Industry", "Industry"),
        ],
    )
    delivery_date = models.DateField()
    tracking_info = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("In Transit", "In Transit"),
            ("Delivered", "Delivered"),
        ],
        default="Pending",
    )
    received_by = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product_name} - Batch {self.batch_number} shipped to {self.destination} on {self.delivery_date} (Status: {self.status})"

class ReportAndAlertSystem:
    @staticmethod
    def generate_quality_control_report(qc_objects):
        report = "Quality Control Report\n"
        report += "-" * 50 + "\n"
        for qc in qc_objects:
            report += f"Product: {qc.product_name} (Batch: {qc.batch_number})\n"
            report += f"Test Date: {qc.test_date}\n"
            report += f"Passed Tests: {qc.passed_tests}\n"
            report += f"Certifications: {qc.certifications}\n"
            report += f"Tested By: {qc.tested_by}\n"
            report += "-" * 50 + "\n\n"
        return report

    @staticmethod
    def alert_for_non_compliance(qc_objects):
        alerts = []
        for qc in qc_objects:
            if not qc.passed_tests:
                alerts.append(
                    f"⚠️ ALERT: {qc.product_name} (Batch: {qc.batch_number}) failed quality control on {qc.test_date}!"
                )
        return alerts

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Batch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    batch_number = models.CharField(max_length=100, unique=True)
    manufacture_date = models.DateField()
    expiry_date = models.DateField()
    quantity = models.PositiveIntegerField()
    quality_check_passed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} - {self.batch_number}"
