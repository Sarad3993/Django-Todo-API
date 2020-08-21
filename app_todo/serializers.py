from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','body',)

# Django REST Framework will now magically transform our data into JSON exposing the fields for id, title, and body from our Todo_model


