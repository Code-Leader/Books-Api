from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
    
    def validate(self, data):
        title = data.get('title', None)
        auther = data.get('auther', None)

        # check title if it contains only alphabetical characters
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitobni sarlavhashi hariflardan tashkil topgan bo'lishi kerak"
                }
            )
        
        # chack title and auther from database existence
        if Book.objects.filter(title=title, auther=auther).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "kitob sarlovhasi va muallifi bir bo'lgan kitobni yuklay olmaysiz"
                }
            )


        return data
    
    def validate_price(self, price):
        if price < 0 or price > 10000:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx notogri kiritilgan"
                }
            )
        return price