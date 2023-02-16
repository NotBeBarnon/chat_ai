## 2.10.0-sample (2022-09-08)

### Feat

- 添加pystruct_tools工具包

### Fix

- 添加特殊的事务使用示例
- 修复generate_delete无法触发删除信号的问题
- 添加一些使用示例

## 2.9.0-sample (2022-08-10)

### Feat

- 添加信令构建工具

### Fix

- 修复Kafka生产者客户端的问题

## 2.8.1-sample (2022-07-29)

### Fix

- 修复Kafka和Redis客户端async with上下文管理报错的问题

## 2.8.0-sample (2022-07-27)

### Fix

- 合并批量删除缓存的能力
- Redis的哨兵客户端优化
- 添加Tortoise-orm的xa事务工具

### Feat

- 增加了redis_client批量清除缓存的功能

## 2.7.5-sample (2022-07-22)

### Fix

- 修复DTM提交的问题

## 2.7.4-sample (2022-07-22)

### Fix

- 修复DTM生成GID时的问题

## 2.7.3-sample (2022-07-22)

### Fix

- 优化
- 将子事务body填充至payloads中

## 2.7.2-sample (2022-07-19)

### Fix

- 针对kakfa和fastapi工具的优化
- 添加对外键关联导入的优化

## 2.7.1-sample (2022-07-14)

### Fix

- 修复数据库读写分离导致的UPDATE后查询数据错误的问题
- 添加对warnings模块的告警日志捕获

## 2.7.0-sample (2022-07-11)

### Feat

- 更新Redis常规客户端和哨兵客户端的无缝切换

## 2.6.5-sample (2022-07-08)

### Fix

- 添加对cx_freeze打包时packages的配置

## 2.6.4-sample (2022-07-07)

### Fix

- kafkaClient添加记录已存在的topic的能力

## 2.6.3-sample (2022-07-06)

### Fix

- 修复DTM插入barrier的sql语句执行错误的问题

## 2.6.2-sample (2022-07-06)

### Fix

- 修复setting.py配置的问题

## 2.6.1-sample (2022-07-06)

### Fix

- 添加DTM的配置可以从环境变量获取

## 2.6.0-sample (2022-07-06)

### Fix

- 优化dtm工具 httpx更换为aiohttp
- dtm部分bug修复
- 修复dtm工具插入表名称错误问题

### Refactor

- redis工具的import变更

### Feat

- **dtm_tools**: orjson replace json

## 2.5.0-sample (2022-06-27)

### Feat

- 更新了dtm_client

## 2.4.0-sample (2022-06-14)

### Feat

- orm的读写分离以及cache中间件的优化

## 2.3.0-sample (2022-06-14)

### Feat

- 完善cache中间件

## 2.2.0-sample (2022-06-11)

### Fix

- 修改默认dev模式不开启
- 完善Redis缓存装饰器
- 完善Redis哨兵Client的使用
- 修改RedisClient使用with而不是async with
- 添加Redis哨兵客户端
- 为ObjectManager添加__call__魔法方法
- 王多鱼投500万给脚手架提提速

### Feat

- 添加KafkaClient对Topic的各种操作

### Refactor

- 删除无用注释

### Perf

- 删除冗余的拖累性能部分

## 2.1.0-sample (2022-05-30)

### Feat

- 合并feat/event_client事件驱动Client的功能

### Fix

- 完善事件驱动的Client
- 事件驱动型RedisClient

### Refactor

- 修改包名

## 2.0.0-sample (2022-05-27)

### Fix

- 修复定制的Pydantic外键关联信息导致的问题
- 为Position添加level字段
- Pydantic抽离及递归尝试
- 完善示例
- 添加使用示例Test的ViewSet接口
- 添加QuerySet实验性接口
- 修改schema为pydantic
- Tortoise-orm外键初始化变更
- 调整logger配置接口

### Feat

- FastSample2.0初始化

## 1.10.2-sample (2022-05-10)

### Fix

- 增加Kafka consumer的callbasks异步控制开关

## 1.10.1-sample (2022-05-10)

### Fix

- bug修复及优化

## 1.10.0-sample (2022-05-05)

### Fix

- 完善RedisClient使用示例，添加Redis名称空间的使用
- 删除ordering参数，修改为使用path自动排序

### Feat

- 添加Redis客户端工具

## 1.9.4-sample (2022-04-27)

### Fix

- 新增fast_tools的ordering参数
- 修改debug模块为system_config模块
- 添加在开发模式下修改日志输出的能力
- 调整日志输出配置
- 修改fast_tools的路由生成规则
- fastapi_tools更新自动为路由添加Viewset名称
- 使用单独的Task来执行Kafka的Consumer的回调
- 优化kafka客户端

## 1.9.3-sample (2022-04-21)

### Fix

- 修复Consumer启动失败的bug

## 1.9.2-sample (2022-04-21)

### Fix

- 修复kafka创建topic没有添加请求头的问题

## 1.9.1-sample (2022-04-21)

### Fix

- 修复kafka的producer发送数据的错误，修改项目基础配置

## 1.9.0-sample (2022-04-19)

### Feat

- 更新dtm功能

## 1.8.0-sample (2022-04-19)

### Refactor

- 合并feat/kafka
- toml配置文件头添加utf-8标记

### Fix

- 完善Kafka客户端工具
- 修改VERSION从settings.py导入
- 更新项目配置与README的各种说明
- 修改CBV转发器继承对应的ViewSet
- 项目结构与配置变更
- Kafka客户端修改
- 项目结构与配置变更

### Feat

- 添加kafka工具包

## 1.7.0-sample (2022-03-16)

### Fix

- 修复DTM屏障问题
- 变更数据库配置

### Refactor

- 记录loguru创建的logger对象的id

### Feat

- 变更项目配置: 日志、数据库

## 1.6.0-sample (2022-03-09)

### Feat

- 合并DTM工具

### Fix

- 重构DTM

## 1.0.0-feat-dtm (2022-02-24)

### Feat

- 更新dtm模块

## 1.5.0-sample (2022-03-08)

### Feat

- 添加自动构建docker镜像脚本

## 1.4.0-sample (2022-03-08)

### Fix

- 合并logger
- 日志输出变更
- 完善访问日志的配置与使用

### Feat

- 修改logger日志输出格式到loguru

## 1.0.0-feat-logger (2022-02-24)

### Feat

- **application.py**: 拦截所有的logging日志模块输出的日志，使用loguru输出

## 1.3.0-sample (2022-03-08)

### Feat

- 添加外键关联示例
## 1.0.0-feat-logger (2022-02-24)

### Feat

- **application.py**: 拦截所有的logging日志模块输出的日志，使用loguru输出

## 1.2.3-sample (2022-02-16)

### Fix

- 添加FastAPI自动生成基础方法

## 1.0.0-feat-dtm (2022-02-24)

### Feat

- 更新dtm模块


## 1.2.2-sample (2022-02-14)

### Fix

- 补充例子
- 修改toml文件中关于database的配置

## 1.2.1-sample (2022-02-14)

### Fix

- 修复预编译时忽略pyproject.toml的问题
- 修改配置从toml中提取
- 修复setup.py中不能自动适配version的问题

## 1.2.0-sample (2022-02-14)

### Fix

- 新增settings中读取toml项目配置
- 添加例子

### Feat

- 添加单元测试目录结构

## 1.1.1-sample (2021-12-16)

### Fix

- 变更version配置
- 删除toml包

### Refactor

- 变更settings文件的编码格式

## 1.1.0-sample (2021-12-16)

### Refactor

- FastAPI文档自动适配version

### Feat

- 添加version配置，添加工具包

## 1.0.0-sample (2021-12-15)

### Fix

- 修改字段验证器错误提示
- 重构项目结构
- 添加Linux系统下打包uvloop
- 修复部分写法问题
- 更改项目结构
- 完善CBV调度
- 修改ShortUIDField
- 添加序列化示例代码
- 修复setup打包时site-packages扫描不全的问题
- 修复site-packages在Linux下不能正确匹配的问题
- 修复FastAPI缺少依赖的问题

### Refactor

- 修改tag规则
- 修改all参数，添加uvloop依赖

### Perf

- 响应使用orjson

### Feat

- 添加FastAPI的CBV实现
- 添加数据库迁移能力
- 搭建数据库连接与setup编译框架
- FastAPI基本架构
- Init
