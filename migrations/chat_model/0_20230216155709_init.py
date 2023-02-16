from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `chat_user` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(64) NOT NULL,
    `open_id` VARCHAR(32)   DEFAULT '',
    `score` INT NOT NULL  DEFAULT 0
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `chat_chat_record` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `create_date` DATETIME(6)   DEFAULT CURRENT_TIMESTAMP(6),
    `write_date` DATETIME(6)   DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `question` LONGTEXT NOT NULL  COMMENT '聊天问题内容',
    `answer` LONGTEXT NOT NULL  COMMENT '聊天回答内容',
    `user_id` INT NOT NULL,
    CONSTRAINT `fk_chat_cha_chat_use_81e7abe7` FOREIGN KEY (`user_id`) REFERENCES `chat_user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='聊天记录';
CREATE TABLE IF NOT EXISTS `chat_score_record` (
    `create_date` DATETIME(6)   DEFAULT CURRENT_TIMESTAMP(6),
    `write_date` DATETIME(6)   DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `score` INT NOT NULL  DEFAULT 0,
    `score_add` BOOL NOT NULL  COMMENT '增加或者减少',
    `user_id` INT NOT NULL,
    CONSTRAINT `fk_chat_sco_chat_use_091e6b8f` FOREIGN KEY (`user_id`) REFERENCES `chat_user` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4 COMMENT='积分记录表';
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
