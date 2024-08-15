from rest_framework import APIException


class CantFollowYourself(APIException):
    statu_code = 403
    default_detail = "You can't follow yourself"
    default_code = "forbidden"
