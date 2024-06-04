from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from drf_yasg.utils import swagger_auto_schema
from account.api.serializers import UserApiDocProfileSerializer

class UserTokenObtainPairView(TokenObtainPairView):

    @swagger_auto_schema(responses={200: UserApiDocProfileSerializer(many=True)})
    def post(self, request: Request, *args, **kwargs) -> Response:
        return super().post(request, *args, **kwargs)
    

