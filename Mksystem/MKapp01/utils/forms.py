from MKapp01.utils.bootstrap import BootStrapModelForm
from MKapp01 import models

class SpiderModelFrom(BootStrapModelForm):
    class Meta:
        model =models.c_data
        fields = '__all__'