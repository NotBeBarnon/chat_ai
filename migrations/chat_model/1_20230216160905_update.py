from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `chat_chat_record` MODIFY COLUMN `answer` LONGTEXT   COMMENT '聊天回答内容';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `chat_chat_record` MODIFY COLUMN `answer` LONGTEXT NOT NULL  COMMENT '聊天回答内容';"""
