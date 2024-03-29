from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='cat_logo/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class subCategory(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subCategories')

    def __str__(self):
        return self.title

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='product_images/')
    image2 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image6 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    code = models.CharField(max_length=20, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_percent = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.TextField()
    warranty_year = models.PositiveSmallIntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)
    SKU = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    available_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title
