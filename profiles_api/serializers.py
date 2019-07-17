from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    # input with characters length less than 10
    name = serializers.CharField(max_length=10)

    
