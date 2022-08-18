from typing import TypedDict


def response_message(message: str, content: str, success: str) -> TypedDict:
    return {"message": message, "content": content, "success": success}
