# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 16:16
# @Author  : Tuffy
# @Description :
import asyncio
import contextlib

import arrow
import orjson
from fastapi import APIRouter, Depends, HTTPException, Response, Request
from fastapi.responses import ORJSONResponse
from loguru import logger
from starlette import status
from tortoise import connections
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.functions import Count
from tortoise.transactions import in_transaction

from src.my_tools.fastapi_tools import Action, BaseViewSet
from src.my_tools.object_manager_tools import global_om
from src.my_tools.password_tools import make_password

from src.settings import LOCAL_TIMEZONE
from .pydantics import *

# user_routers = APIRouter(prefix=f"/{app_name}")



