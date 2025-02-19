from rest_framework import serializers

from vehicle.models import Car, Moto, Milage
from vehicle.validators import TitleValidator


class MilageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Milage
        fields = "__all__"


class CarSerializers(serializers.ModelSerializer):
    last_milage = serializers.IntegerField(source='milage.all.first.milage', read_only=True)
    milage = MilageSerializers(many=True, read_only=True)

    class Meta:
        model = Car
        fields = "__all__"


class MotoSerializers(serializers.ModelSerializer):
    last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields = "__all__"

    def get_last_milage(self, instance):
        if instance.milage.all().first():
            return instance.milage.all().first().milage
        return 0


class MotoMilageSerializers(serializers.ModelSerializer):
    moto = MotoSerializers()

    class Meta:
        model = Milage
        fields = "__all__"


class MotoCreateSerializers(serializers.ModelSerializer):
    milage = MilageSerializers(many=True)

    class Meta:
        model = Moto
        fields = "__all__"
        validators = [
            TitleValidator(field='title'),
            serializers.UniqueTogetherValidator(fields=["title", "description"], queryset=Moto.objects.all())
        ]

    def create(self, validated_data):
        milage = validated_data.pop('milage')

        moto_item = Moto.objects.create(**validated_data)

        for m in milage:
            Milage.objects.create(moto=moto_item, **m)

        return moto_item
