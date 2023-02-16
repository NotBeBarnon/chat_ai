# -*- coding: utf-8 -*-
# @Time    : 2023/2/14:10:24
# @Author  : fzx
# @Description :
import asyncio
import datetime
from enum import Enum
from json import JSONDecodeError
from typing import Any

import aiohttp
import httpx
import loguru
import openai
import orjson
from httpcore import ReadTimeout

from src.settings import API_KEY


class Gpt_3_ModelType(str, Enum):
    """文本模型"""
    text_davinci_003 = "text-davinci-003"
    text_curie_001 = "text-curie-001"
    text_babbage_001 = "text-babbage-001"
    text_ada_001 = "text-ada-001"


class Codex_ModelType(str, Enum):
    """代码,限量，待官方完善"""
    code_davinci_002 = "code-davinci-002"
    code_cushman_001 = "code-cushman-001"


class ChatGPT:

    def __init__(self):
        # self._client = Client(base_url=base_url)
        self.api_key = API_KEY
        # self.header = {
        #     "Authorization": f"Bearer {self.api_key}"
        # }
        # self._client.header.update(self.header)

        # 模型选择
        self._model: Gpt_3_ModelType = Gpt_3_ModelType.text_davinci_003
        # 结果的最大 tokens 数，不能超过模型的上下文长度，目前最大限制是4097, 请求内容的tokens+_max_tokens需要小于4097
        self._max_tokens = 1000
        # 控制结果的随机性，如果希望结果更有创意可以尝试 0.9，或者希望有固定结果可以尝试 0.0
        self._temperature = 0.0
        # 一个可用于代替 temperature 的参数，对应机器学习中 nucleus sampling，如果设置 0.1 意味着只考虑构成前 10% 概率质量的 tokens
        self._top_p = 0.5
        # 控制字符的重复度, -2.0 ~ 2.0 之间的数字,正值会根据新 tokens 在文本中的现有频率降低模型逐字重复同一行的可能性
        self._frequency_penalty = 0.0
        # 控制主题的重复度 -2.0 ~ 2.0 之间的数字，正值会根据到目前为止是否出现在文本中来增加模型谈论新主题的可能性
        self._presence_penalty = 0.0
        # 最大长度为 4 的字符串列表，一旦生成的 tokens 包含其中的内容，将停止生成并返回结果
        # self.stop = 0.5

    async def call_completion_create(self, prompt, max_tokens=16):
        async with aiohttp.ClientSession() as session:
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.api_key}',
            }
            data = {
                "model": self._model,
                "prompt": prompt,
                "temperature": self._temperature,
                "max_tokens": self._max_tokens,
                "top_p": self._top_p,
                "frequency_penalty": self._frequency_penalty,
                "presence_penalty": self._presence_penalty,
            }
            async with session.post('https://api.openai.com/v1/completions', headers=headers, json=data) as response:
                response_json = await response.json()
                if response.status == 401:
                    return response.status, "Incorrect API key provided"
                # print(response_json["choices"][0]["text"])
                return response.status, response_json["choices"][0]["text"]

    async def ask_question(self, prompt):
        # await self.set_args(max_tokens=4097-len(prompt))
        openai.api_key = self.api_key
        print(datetime.datetime.now())
        response = openai.Completion.create(model=self._model,
                                            prompt=prompt,
                                            temperature=self._temperature,
                                            max_tokens=self._max_tokens,
                                            top_p=self._top_p,
                                            frequency_penalty=self._frequency_penalty,
                                            presence_penalty=self._presence_penalty,
                                            )
        print(datetime.datetime.now())
        print(response.choices[0].text)

        return response.choices[0].text

    async def set_args(self, model: Gpt_3_ModelType = None,
                       max_tokens: int = None,
                       temperature: float = None,
                       frequency_penalty: float = None,
                       presence_penalty: float = None,
                       top_p: float = None):
        if model is not None:
            self._model = model
        if max_tokens is not None:
            self._max_tokens = max_tokens
        if top_p is not None:
            self._top_p = top_p
        if temperature is not None:
            self._temperature = temperature
        if frequency_penalty is not None:
            self._frequency_penalty = frequency_penalty
        if presence_penalty is not None:
            self._presence_penalty = presence_penalty

async def run_task():
    gtp3 = ChatGPT()
    asyncio.get_event_loop().create_task(gtp3.call_completion_create(prompt="你的接口可以异步调用吗"))
    asyncio.get_event_loop().create_task(gtp3.call_completion_create(prompt="你叫啥"))
    await asyncio.sleep(100)

if __name__ == '__main__':
    # tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    # print(tokenizer("hello")["input_ids"])

    asyncio.run(run_task())
