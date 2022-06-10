from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id','name','ric','rank', 'esgscore',
                  'environmental', 'social', 'governance')
        
