# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 16:11
# @Author  : Tuffy
# @Description : FastAPI 的异常捕获
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel, ValidationError as PydanticValidationError
from starlette import status
from tortoise.exceptions import DoesNotExist, IntegrityError, ValidationError as TortoiseValidationError, \
    ValidationError

from .apps import fast_app

__all__ = ("HTTPError",)


class HTTPError(BaseModel):
    detail: str

class APIValidationError(ValidationError):
    """自定义http status code"""

    def __init__(self, msg=None, code=None, status_code=status.HTTP_400_BAD_REQUEST):
        if status_code is not None:
            self.status_code = status_code
            self.msg = msg

    def __str__(self) -> str:
        return self.msg


@fast_app.exception_handler(APIValidationError)
async def http_exception_handler(request: Request, exc: APIValidationError):
    """
    业务逻辑中的error
    """
    return ORJSONResponse(
        status_code=exc.status_code,
        content={"detail": [{"loc": [], "msg": str(exc), "type": "APIValidationError"}]},
    )


@fast_app.exception_handler(DoesNotExist)
async def doesnotexist_exception_handler(request: Request, exc: DoesNotExist):
    """
    捕获获取数据库数据失败的异常
    """
    return ORJSONResponse(status_code=404, content={"detail": str(exc)})


@fast_app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    捕获请求体数据的验证错误（FastAPI封装的验证错误）
    """
    return ORJSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )


@fast_app.exception_handler(PydanticValidationError)
async def pydantic_validation_exception_handler(request: Request, exc: PydanticValidationError):
    """
    捕获请求体数据的验证错误（FastAPI未封装的验证错误）
    """
    return ORJSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )


@fast_app.exception_handler(TortoiseValidationError)
async def tortoise_validation_exception_handler(request: Request, exc: TortoiseValidationError):
    """
    捕获数据库更新数据时的验证错误（model中验证器抛出）
    """
    return ORJSONResponse(
        status_code=422,
        content={"detail": [{"loc": [], "msg": str(exc), "type": "ValidationError"}]},
    )


@fast_app.exception_handler(IntegrityError)
async def integrityerror_exception_handler(request: Request, exc: IntegrityError):
    """
    捕获数据库更新数据时的完整性错误（model的数据不完整）
    """
    return ORJSONResponse(
        status_code=422,
        content={"detail": [{"loc": [], "msg": str(exc), "type": "IntegrityError"}]},
    )


@fast_app.exception_handler(ValueError)
async def database_validation_exception_handler(request: Request, exc: ValueError):
    """
    捕获数据库更新数据时的验证错误（数据库写入错误抛出）
    """
    return ORJSONResponse(
        status_code=422,
        content={"detail": [{"loc": [], "msg": str(exc), "type": "ValueError"}]},
    )
