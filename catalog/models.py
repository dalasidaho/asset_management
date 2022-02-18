from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Type(models.Model):
    """
    Model representing a devices type
    """

    type = models.CharField(max_length=200, help_text="Laptop / desktop etc")

    def __str__(self):

        return self.type


class Model(models.Model):
    """
    Model representing a devices model
    """
    name = models.CharField(max_length=200, help_text="Enter a hw Model")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Device(models.Model):
    """
    Model representing a devices (details).
    """
    hostname = models.CharField(max_length=20, null=False, blank=False, verbose_name="Hostname")
    serialn = models.CharField(max_length=30, null=True,  verbose_name="S/N", blank=True)
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey('Model', on_delete=models.SET_NULL, null=True)
    LOAN_STATUS = (
        ('0', 'Received'),
        ('1', 'Deployed'),
        ('2', 'Inactive'),
        ('3', 'In Stock'),
        ('4', 'Decommission'),
        ('5', 'Disposed'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='0',
                                 help_text='Asset Status')
    LOAN_SUBSTATUS = (
        ('0', 'Completed Shipment'),
        ('1', 'Functional'),
        ('2', 'Not In use'),
        ('3', 'In Inventory'),
        ('4', 'Decommissioned'),
        ('5', 'Disposed'),
    )

    substatus = models.CharField(max_length=1, choices=LOAN_SUBSTATUS, blank=True, default='0',
                                 help_text='Asset Sub Status')

    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    tag = models.CharField(max_length=10, null=True, blank=True)
    buydate = models.DateField(null=True, blank=True, verbose_name="Purchase date")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    notes = models.TextField(max_length=1000, null=True, blank=True, help_text="Enter a job description of the Device")
    warranty = models.DateField(null=True, blank=True, verbose_name="Warranty End")
    cost = models.FloatField(null=True, blank=True)


    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.hostname

    def display_customer(self):
        """
        Creates a string for the Customer. This is required to display model in Admin.
        """
        return ', '.join([model.name for model in self.model.all()[:3]])

    display_customer.short_description = 'Customer'

    def display_model(self):
        """
        Creates a string for the Model. This is required to display model in Admin.
        """
        return ', '.join([model.name for model in self.model.all()[:3]])

    display_model.short_description = 'Model'

    def status_verbose(self):
        return dict(Device.LOAN_STATUS)[self.status]

    def substatus_verbose(self):
        return dict(Device.LOAN_SUBSTATUS)[self.substatus]


    def get_absolute_url(self):
        """
        Returns the url to access a particular device.
        """
        return reverse('catalog:device-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-modified']
        
class Archive(models.Model):
    """
    Model representing a divice (copy of Device model for Archive if need).
    """
    hostname = models.CharField(max_length=20, verbose_name="Hostname")
    serialn = models.CharField(max_length=30, null=True,  verbose_name="S/N", blank=True)
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey('Model', on_delete=models.SET_NULL, null=True)
    LOAN_STATUS = (
        ('0', 'Received'),
        ('1', 'Deployed'),
        ('2', 'Inactive'),
        ('3', 'In Stock'),
        ('4', 'Decommission'),
        ('5', 'Disposed'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='0',
                                 help_text='Asset Status')
    LOAN_SUBSTATUS = (
        ('0', 'Completed Shipment'),
        ('1', 'Functional'),
        ('2', 'Not In use'),
        ('3', 'In Inventory'),
        ('4', 'Decommissioned'),
        ('5', 'Disposed'),
    )

    substatus = models.CharField(max_length=1, choices=LOAN_SUBSTATUS, blank=True, default='0',
                                 help_text='Asset Sub Status')

    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    tag = models.CharField(max_length=10, null=True, blank=True)
    buydate = models.DateField(null=True, blank=True, verbose_name="Purchase date")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    notes = models.TextField(max_length=1000, null=True, blank=True, help_text="Enter a job description of the Device")
    warranty = models.DateField(null=True, blank=True, verbose_name="Warranty End")
    cost = models.FloatField(null=True, blank=True)


    def __str__(self):
        """
        String for representing the Device object.
        """
        return self.hostname

    def display_customer(self):
        """
        Creates a string for the Customer. This is required to display model in Admin.
        """
        return ', '.join([model.name for model in self.model.all()[:3]])

    display_customer.short_description = 'Customer'

    def display_model(self):
        """
        Creates a string for the Model. This is required to display model in Admin.
        """
        return ', '.join([model.name for model in self.model.all()[:3]])

    display_model.short_description = 'Model'

    def status_verbose(self):
        return dict(Archive.LOAN_STATUS)[self.status]

    def substatus_verbose(self):
        return dict(Archive.LOAN_SUBSTATUS)[self.substatus]


    def get_absolute_url(self):
        """
        Returns the url to access a particular Archive.
        """
        return reverse('catalog:archive-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-modified']


class Customer(models.Model):
    """
    Model representing an Customer.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)



    def get_absolute_url(self):
        """
        Returns the url to access a particular Customer.
        """
        return reverse('catalog:customer_detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Customer object.
        """
        return '%s, %s' % (self.last_name, self.first_name)

    class Meta:
        ordering = ['last_name']


class Tracker(models.Model):
    """
        Model representing assigned or reassigned device to customer
    """

    deptout = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, verbose_name="Out", related_name='+') #out dept
    deptin = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, verbose_name="Get", related_name='+') #out dept
    LOAN_TYPE = (
        ('1', 'Deploy'),
        ('2', 'Stock'),
        ('3', 'Refresh'),
        ('4', 'Stolen'),
     )
    notes = models.CharField(max_length=10, choices=LOAN_TYPE, blank=False, default='1',
                             verbose_name="Reason")
    name = models.CharField(max_length=50, blank=False)
    credate = models.DateField(null=False, blank=False) #date
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, verbose_name='From')
    cus2 = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, verbose_name='To', related_name='+')
    equip = models.ForeignKey('Device', on_delete=models.SET_NULL, null=True, verbose_name='Device')
    equip1 = models.ForeignKey('Device', on_delete=models.SET_NULL, null=True, blank=True, related_name='+', verbose_name='Device 2')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)


    def __str__(self):

        return self.name

    def deptout_verbose(self):
        return dict(Tracker.LOAN_DEPT)[self.deptout]

    def deptin_verbose(self):
        return dict(Tracker.LOAN_DEPT)[self.deptin]

    def notes_verbose(self):
        return dict(Tracker.LOAN_TYPE)[self.notes]


    def get_absolute_url(self):

        return reverse('catalog:tracker_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-id']
        

class Inventory(models.Model):
    """
       Model representing print assets tag
    """

    num = models.CharField(max_length=15, blank=True, null=True)
    snum = models.TextField(max_length=15, blank=True, null=True)

    class Meta:
        ordering = ['id']

class Location(models.Model):
    """
      Model representing set location/site for customer or device
    """

    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        """
        String for representing the Location object (in Admin site etc.)
        """
        return self.name

class Department(models.Model):
    """
        Model representing set department for customer or Tracker
    """
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        """
        String for representing the Department object (in Admin site etc.)
        """
        return self.name