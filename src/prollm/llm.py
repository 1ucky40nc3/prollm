# Copyright 2023 Louis Wendler
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Callable, Optional
import os
from langchain.llms import OpenAI

# Define a LLM a simple function
LLM = Callable[[str], str]


def gpt4(openai_api_key: Optional[str] = None, **kwargs) -> LLM:
    """Return a OpenAI GPT-4 LLM function.

    Args:
        openai_api_key: An optional OpenAI API-Key.
            This can also be provided through the 'OPENAI_API_KEY' environment variable.

    Returns:
        A OpenAI GPT-4 LLM function.
    """
    openai_api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
    return OpenAI(openai_api_key=openai_api_key, **kwargs)
