from datetime import timezone, datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Room, Image, Booking, Review


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['url']


class ImageListSerializer(serializers.ListSerializer):
    child = ImageSerializer()

    def create(self, validated_data):
        return [self.child.create(item) for item in validated_data]


class RoomDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, source='image_set')

    class Meta:
        model = Room
        fields = ['id', 'number', 'description', 'status', 'is_cottage', 'images']

    def create(self, validated_data):
        images = validated_data.pop('image_set')
        room = Room.objects.create(**validated_data)
        if images:
            for image in images:
                Image.objects.create(room=room, url=image['url'])
        return room


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ['price']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        exclude = ['total_price']

    def create(self, validated_data):
        room = validated_data['room']
        validated_data.pop('status')
        now = datetime.now()
        if room and room.status != 1:
            if now <= Booking.objects.filter(room=room).order_by('-id')[0].checkout_time:
                raise ValidationError('Room already booked in that period')
        return Booking.objects.create(**validated_data)

    def update(self, instance, validated_data):
        room = instance.room
        status = validated_data['status']
        if status == 'confirmed':
            room.status = 0
            room.save()
        elif status == 'canceled':
            instance.delete()
        return super().update(instance, validated_data)


class BookingListSerializer(serializers.ListSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'rating']
