from rest_framework import serializers,exceptions
import django.contrib.auth.password_validation as validator 
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'first_name',
            'last_name',
            'student_id',
            'staff_id',
            'course',
            'department',
        ]
        extra_kwargs = {"password":{'write_only':True}}



    def validate(self,data):
        user = User(**data)

        password = data.get('password')

        errors = dict()

        try:
            validator.validate_password(password=password,user=user)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
        
        if errors:
            serializers.ValidationError(errors)

        return super(RegisterSerializer,self).validate(data)



    def save(self):
        if (self.validated_data['student_id']):
            user = User.objects.create_user(
                email=self.validated_data['email'],
                password=self.validated_data['password'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name'],
                student_id=self.validated_data['student_id'],
                course=self.validated_data['course'],
            )
            return user

        elif (self.validated_data['staff_id']):
            admin = User.objects.create_superuser(
                email=self.validated_data['email'],
                password=self.validated_data['password'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name'],
                staff_id=self.validated_data['staff_id'],
                department=self.validated_data['department'],
            )
            return admin



