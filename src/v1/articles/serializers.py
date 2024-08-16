from rest_framework import serializers

from v1.articles.models import Article, ArticleView
from v1.profiles.serializers import ProfileSerializer


class TagListField(serializers.Field):
    def to_representation(self, value):  # noqa
        return [tag.name for tag in value.all()]

    def to_internal_value(self, data):  # noqa
        if not isinstance(data, list):
            raise serializers.ValidationError("Expected a list of tags")

        tag_objects = []
        for tag_name in data:
            tag_name_striped = tag_name.strip()

            if not tag_name_striped:
                continue
            tag_objects.append(tag_name_striped)
        return tag_objects


class ArticleSerializer(serializers.ModelSerializer):
    author_info = ProfileSerializer(source="author.profile", read_only=True)
    banner_image = serializers.SerializerMethodField()
    estimated_reading_time = serializers.ReadOnlyField()
    tags = TagListField()
    views = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_views(self, obj):  # noqa
        return ArticleView.objects.filter(article=obj).count()

    def get_banner_image(self, obj):  # noqa
        return obj.banner_image.url

    def get_created_at(self, obj):  # noqa
        now = obj.created_at
        formatted_date = now.strftime("%m/%d/%Y %H:%M:%S")
        return formatted_date

    def get_updated_at(self, obj):  # noqa
        then = obj.created_at
        formatted_date = then.strftime("%m/%d/%Y %H:%M:%S")
        return formatted_date

    def create(self, validadeted_data):  # noqa
        tags = validadeted_data.pop("tags")
        article = Article.objects.create(**validadeted_data)
        article.tags.set(tags)
        return article

    def update(self, instance, validated_data):  # noqa
        instance.author = validated_data.get("author", instance.author)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.body = validated_data.get("body", instance.body)
        instance.banner_image = validated_data.get("banner_image", instance.banner_image)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)

        if "tags" in validated_data:
            instance.tags.set(validated_data["tags"])

        instance.save()
        return instance

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "slug",
            "tags",
            "estimated_reading_time",
            "author_info",
            "views",
            "description",
            "body",
            "banner_image",
            "created_at",
            "updated_at",
        ]
