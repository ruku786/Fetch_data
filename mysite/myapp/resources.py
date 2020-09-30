from import_export import resources
from.models import employee

class EmployeeResources(resources.ModelResource):
    class meta:
        model = employee