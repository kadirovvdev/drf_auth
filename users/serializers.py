from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    def validate_name(self, name):
        if name.isalpha():
            return name
        raise serializers.ValidationError('Name must be alphabets')
    
    def validate_surname(self, surname):
        if surname.isalpha():
            return surname
        raise serializers.ValidationError('Surname must be alphabets')
    
    def validate_age(self, age):
        if str(age).isnumeric():
            return age
        raise serializers.ValidationError('Age must be digits')

    def validate_phone(self, phone):
        if str(phone).isnumeric():
            return phone
        raise serializers.ValidationError('Phone must be digits')
    
    def validate_email(self, email):
        if  '@' in email and '.' in email:
            return email
        raise serializers.ValidationError('The email you entered is invalid')