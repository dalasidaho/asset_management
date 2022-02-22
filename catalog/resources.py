from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget, DateWidget
from .models import Device, Customer, Model, Type, Inventory, Location

class DevicelistResource(resources.ModelResource):
    """
        Import Device
    """

    hostname = Field(attribute='hostname', column_name='Hostname')
    customer = Field(attribute='customer', column_name='Customer', widget=ForeignKeyWidget(Customer, 'last_name'))
    model = Field(attribute='model', column_name='Model', widget=ForeignKeyWidget(Model, 'name'))
    serialn = Field(attribute='serialn', column_name='S/N')
    tag = Field(attribute='tag', column_name='Tag')
    type = Field(column_name='Type', attribute='type', widget=ForeignKeyWidget(Type, 'type'))
    location = Field(attribute='location', column_name='Location', widget=ForeignKeyWidget(Location, 'name'))
    buydate = Field(attribute='buydate', column_name='Buy date', widget=DateWidget('%d/%m/%Y'))
    status = Field(attribute='status_verbose', column_name='Status')
    substatus = Field(attribute='substatus_verbose', column_name='SubStatus')
    warranty = Field(attribute='warranty', column_name='Warranty', widget=DateWidget('%d/%m/%Y'))
    cost = Field(attribute='cost', column_name='Cost')



    class Meta:
        model = Device
        fields = ('buydate')
        exclude = ('id', )
        import_id_fields = ('title', 'customer', 'model', 'serialn', 'tag', 'type', 'location', 'buydate', 'status', 'substatus',
                            'warranty', 'cost', )

    def dehydrate_customer(self, device):
        return '%s' % (device.customer)


class AssettagResource(resources.ModelResource):
    """
       Import Asset tag and Serial Number
    """

    num = Field(attribute='num', column_name='AssetTag')
    snum = Field(attribute='snum', column_name='SN')

    class Meta:
        model = Inventory
        exclude = ('id', )
        import_id_fields = ('num', 'snum', )
