## 2.10.0-sample (2022-09-08)

### Feat

- ���pystruct_tools���߰�

### Fix

- ������������ʹ��ʾ��
- �޸�generate_delete�޷�����ɾ���źŵ�����
- ���һЩʹ��ʾ��

## 2.9.0-sample (2022-08-10)

### Feat

- ������������

### Fix

- �޸�Kafka�����߿ͻ��˵�����

## 2.8.1-sample (2022-07-29)

### Fix

- �޸�Kafka��Redis�ͻ���async with�����Ĺ����������

## 2.8.0-sample (2022-07-27)

### Fix

- �ϲ�����ɾ�����������
- Redis���ڱ��ͻ����Ż�
- ���Tortoise-orm��xa���񹤾�

### Feat

- ������redis_client�����������Ĺ���

## 2.7.5-sample (2022-07-22)

### Fix

- �޸�DTM�ύ������

## 2.7.4-sample (2022-07-22)

### Fix

- �޸�DTM����GIDʱ������

## 2.7.3-sample (2022-07-22)

### Fix

- �Ż�
- ��������body�����payloads��

## 2.7.2-sample (2022-07-19)

### Fix

- ���kakfa��fastapi���ߵ��Ż�
- ��Ӷ��������������Ż�

## 2.7.1-sample (2022-07-14)

### Fix

- �޸����ݿ��д���뵼�µ�UPDATE���ѯ���ݴ��������
- ��Ӷ�warningsģ��ĸ澯��־����

## 2.7.0-sample (2022-07-11)

### Feat

- ����Redis����ͻ��˺��ڱ��ͻ��˵��޷��л�

## 2.6.5-sample (2022-07-08)

### Fix

- ��Ӷ�cx_freeze���ʱpackages������

## 2.6.4-sample (2022-07-07)

### Fix

- kafkaClient��Ӽ�¼�Ѵ��ڵ�topic������

## 2.6.3-sample (2022-07-06)

### Fix

- �޸�DTM����barrier��sql���ִ�д��������

## 2.6.2-sample (2022-07-06)

### Fix

- �޸�setting.py���õ�����

## 2.6.1-sample (2022-07-06)

### Fix

- ���DTM�����ÿ��Դӻ���������ȡ

## 2.6.0-sample (2022-07-06)

### Fix

- �Ż�dtm���� httpx����Ϊaiohttp
- dtm����bug�޸�
- �޸�dtm���߲�������ƴ�������

### Refactor

- redis���ߵ�import���

### Feat

- **dtm_tools**: orjson replace json

## 2.5.0-sample (2022-06-27)

### Feat

- ������dtm_client

## 2.4.0-sample (2022-06-14)

### Feat

- orm�Ķ�д�����Լ�cache�м�����Ż�

## 2.3.0-sample (2022-06-14)

### Feat

- ����cache�м��

## 2.2.0-sample (2022-06-11)

### Fix

- �޸�Ĭ��devģʽ������
- ����Redis����װ����
- ����Redis�ڱ�Client��ʹ��
- �޸�RedisClientʹ��with������async with
- ���Redis�ڱ��ͻ���
- ΪObjectManager���__call__ħ������
- ������Ͷ500������ּ�������

### Feat

- ���KafkaClient��Topic�ĸ��ֲ���

### Refactor

- ɾ������ע��

### Perf

- ɾ��������������ܲ���

## 2.1.0-sample (2022-05-30)

### Feat

- �ϲ�feat/event_client�¼�����Client�Ĺ���

### Fix

- �����¼�������Client
- �¼�������RedisClient

### Refactor

- �޸İ���

## 2.0.0-sample (2022-05-27)

### Fix

- �޸����Ƶ�Pydantic���������Ϣ���µ�����
- ΪPosition���level�ֶ�
- Pydantic���뼰�ݹ鳢��
- ����ʾ��
- ���ʹ��ʾ��Test��ViewSet�ӿ�
- ���QuerySetʵ���Խӿ�
- �޸�schemaΪpydantic
- Tortoise-orm�����ʼ�����
- ����logger���ýӿ�

### Feat

- FastSample2.0��ʼ��

## 1.10.2-sample (2022-05-10)

### Fix

- ����Kafka consumer��callbasks�첽���ƿ���

## 1.10.1-sample (2022-05-10)

### Fix

- bug�޸����Ż�

## 1.10.0-sample (2022-05-05)

### Fix

- ����RedisClientʹ��ʾ�������Redis���ƿռ��ʹ��
- ɾ��ordering�������޸�Ϊʹ��path�Զ�����

### Feat

- ���Redis�ͻ��˹���

## 1.9.4-sample (2022-04-27)

### Fix

- ����fast_tools��ordering����
- �޸�debugģ��Ϊsystem_configģ��
- ����ڿ���ģʽ���޸���־���������
- ������־�������
- �޸�fast_tools��·�����ɹ���
- fastapi_tools�����Զ�Ϊ·�����Viewset����
- ʹ�õ�����Task��ִ��Kafka��Consumer�Ļص�
- �Ż�kafka�ͻ���

## 1.9.3-sample (2022-04-21)

### Fix

- �޸�Consumer����ʧ�ܵ�bug

## 1.9.2-sample (2022-04-21)

### Fix

- �޸�kafka����topicû���������ͷ������

## 1.9.1-sample (2022-04-21)

### Fix

- �޸�kafka��producer�������ݵĴ����޸���Ŀ��������

## 1.9.0-sample (2022-04-19)

### Feat

- ����dtm����

## 1.8.0-sample (2022-04-19)

### Refactor

- �ϲ�feat/kafka
- toml�����ļ�ͷ���utf-8���

### Fix

- ����Kafka�ͻ��˹���
- �޸�VERSION��settings.py����
- ������Ŀ������README�ĸ���˵��
- �޸�CBVת�����̳ж�Ӧ��ViewSet
- ��Ŀ�ṹ�����ñ��
- Kafka�ͻ����޸�
- ��Ŀ�ṹ�����ñ��

### Feat

- ���kafka���߰�

## 1.7.0-sample (2022-03-16)

### Fix

- �޸�DTM��������
- ������ݿ�����

### Refactor

- ��¼loguru������logger�����id

### Feat

- �����Ŀ����: ��־�����ݿ�

## 1.6.0-sample (2022-03-09)

### Feat

- �ϲ�DTM����

### Fix

- �ع�DTM

## 1.0.0-feat-dtm (2022-02-24)

### Feat

- ����dtmģ��

## 1.5.0-sample (2022-03-08)

### Feat

- ����Զ�����docker����ű�

## 1.4.0-sample (2022-03-08)

### Fix

- �ϲ�logger
- ��־������
- ���Ʒ�����־��������ʹ��

### Feat

- �޸�logger��־�����ʽ��loguru

## 1.0.0-feat-logger (2022-02-24)

### Feat

- **application.py**: �������е�logging��־ģ���������־��ʹ��loguru���

## 1.3.0-sample (2022-03-08)

### Feat

- ����������ʾ��
## 1.0.0-feat-logger (2022-02-24)

### Feat

- **application.py**: �������е�logging��־ģ���������־��ʹ��loguru���

## 1.2.3-sample (2022-02-16)

### Fix

- ���FastAPI�Զ����ɻ�������

## 1.0.0-feat-dtm (2022-02-24)

### Feat

- ����dtmģ��


## 1.2.2-sample (2022-02-14)

### Fix

- ��������
- �޸�toml�ļ��й���database������

## 1.2.1-sample (2022-02-14)

### Fix

- �޸�Ԥ����ʱ����pyproject.toml������
- �޸����ô�toml����ȡ
- �޸�setup.py�в����Զ�����version������

## 1.2.0-sample (2022-02-14)

### Fix

- ����settings�ж�ȡtoml��Ŀ����
- �������

### Feat

- ��ӵ�Ԫ����Ŀ¼�ṹ

## 1.1.1-sample (2021-12-16)

### Fix

- ���version����
- ɾ��toml��

### Refactor

- ���settings�ļ��ı����ʽ

## 1.1.0-sample (2021-12-16)

### Refactor

- FastAPI�ĵ��Զ�����version

### Feat

- ���version���ã���ӹ��߰�

## 1.0.0-sample (2021-12-15)

### Fix

- �޸��ֶ���֤��������ʾ
- �ع���Ŀ�ṹ
- ���Linuxϵͳ�´��uvloop
- �޸�����д������
- ������Ŀ�ṹ
- ����CBV����
- �޸�ShortUIDField
- ������л�ʾ������
- �޸�setup���ʱsite-packagesɨ�費ȫ������
- �޸�site-packages��Linux�²�����ȷƥ�������
- �޸�FastAPIȱ������������

### Refactor

- �޸�tag����
- �޸�all���������uvloop����

### Perf

- ��Ӧʹ��orjson

### Feat

- ���FastAPI��CBVʵ��
- ������ݿ�Ǩ������
- ����ݿ�������setup������
- FastAPI�����ܹ�
- Init
