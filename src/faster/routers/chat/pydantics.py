# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 16:10
# @Author  : Tuffy
# @Description :
from pydantic.main import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.faster.database.models import ChatRecord


class ChatRecordSchema(pydantic_model_creator(ChatRecord, name="ChatRecordSchema", exclude=())):
    pass


class ChatContentSchema(BaseModel):
    content: str


class ChatRecordSimpleSchema(BaseModel):
    question: str
    answer: str
