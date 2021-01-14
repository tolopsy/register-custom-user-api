from allauth.account.adapter import get_adapter

from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from .models import Citizen

class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(max_value=None, min_value=1)
    occupation = serializers.CharField(max_length=50)
    date_of_birth = serializers.DateField()

    class Meta:
        model = Citizen
        fields = ('username', 'email', 'password', 'age', 'occupation', 'date_of_birth',)
    
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'age': self.validated_data.get('age'),
            'occupation': self.validated_data.get('occupation'),
            'date_of_birth': self.validated_data.get('date_of_birth'),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.age = self.cleaned_data.get('age')
        user.occupation = self.cleaned_data.get('occupation')
        user.date_of_birth = self.cleaned_data.get('date_of_birth')
        user.save()
        adapter.save_user(request, user, self)
        return user