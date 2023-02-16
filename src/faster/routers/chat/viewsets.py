# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 16:16
# @Author  : Tuffy
# @Description :
import datetime
from typing import List

from fastapi import APIRouter

from src.my_tools.Gpt.chatgpt import ChatGPT
from src.my_tools.fastapi_tools import Action, BaseViewSet
from . import app_name
from .pydantics import *
from ...database.models import ChatRecord, User
from ...exceptions import APIValidationError

chat_routers = APIRouter(prefix=f"/{app_name}")


class ChatViewSet(BaseViewSet):
    model = ChatRecord
    schema = ChatRecordSchema
    pk_type = int
    views = {}

    @Action.post("", summary="发送聊天")
    async def chat(self, body: ChatContentSchema):
        user = await User.get(pk=1)
        gtp3 = ChatGPT()
        record = await ChatRecord.create(question=body.content, user=user)
        # asyncio.create_task(gtp3.call_completion_create(prompt=body.content))
        print(datetime.datetime.now())
        code, answer = await gtp3.call_completion_create(prompt=body.content)
        if code == 401:
            raise APIValidationError(msg=answer)
        print(datetime.datetime.now())
        record.answer = answer
        await record.save()
        return ChatRecordSimpleSchema(**{
            "question": record.question,
            "answer": record.answer,
        })

    @Action.get("/list", response_model=List[ChatRecordSchema], summary="获取列表")
    async def list(self):
        user = await User.get(pk=1)
        records = ChatRecord.filter(user=user)
        return await ChatRecordSchema.from_queryset(records)


ChatViewSet.register(chat_routers)
