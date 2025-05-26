from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError, AuthenticationFailed


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        # Add status code to response data
        response.data["status_code"] = response.status_code
        error_data = {"code": response.status_code, "errors": []}
        match exc.detail:
            case dict() as detail:
                error_data["errors"] = [
                    {"detail": str(error), "source": field}
                    for field, errors in detail.items()
                    if field != "status_code"
                    for error in (errors if isinstance(errors, list) else [errors])
                ]
            case list() as detail:
                error_data["errors"] = [{"message": str(error)} for error in detail]
            case _:
                error_data["errors"] = [{"message": str(exc.detail)}]

        response.data = error_data

    return response
