from rest_framework.views import exception_handler
from utils.response import response_message


def custom_exception_handler(exc, context):
    exception_class = exc.__class__.__name__
    response = exception_handler(exc, context)

    if response is not None:
        if exception_class == "ValidationError":
            response.data = response_message(
                message=response.data, content="", success=False
            )
        else:
            response.data = response_message(
                message=response.data["detail"], content="", success=False
            )

    return response
