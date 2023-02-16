# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 16:00
# @Author  : Tuffy
# @Description :
from tortoise import fields, models


class AbstractDefaultColumn(models.Model):
    create_date = fields.DatetimeField(auto_now_add=True, null=True)  # 使用auto_now_add
    write_date = fields.DatetimeField(auto_now=True, null=True)  # 使用auto_now

    class Meta:
        abstract = True


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=64)
    open_id = fields.CharField(max_length=32, default="", null=True, blank=True)
    score = fields.IntField(default=0)  # 积分,目前一次一条

    class Meta:
        table = "chat_user"


class ScoreRecord(AbstractDefaultColumn):
    """积分记录表"""
    id = fields.IntField(pk=True)
    score = fields.IntField(default=0)  # 积分,目前一次一条
    score_add = fields.BooleanField(description="增加或者减少")
    user = fields.ForeignKeyField("chat_model.User", related_name="user_score_records")

    class Meta:
        table = "chat_score_record"


class ChatRecord(AbstractDefaultColumn):
    """聊天记录"""
    question = fields.TextField(description="聊天问题内容")
    answer = fields.TextField(description="聊天回答内容", null=True)
    user = fields.ForeignKeyField("chat_model.User", related_name="user_chat_records")

    class Meta:
        table = "chat_chat_record"
