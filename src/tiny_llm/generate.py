import mlx.core as mx
from mlx_lm.tokenizer_utils import TokenizerWrapper
from .qwen2_week1 import Qwen2ModelWeek1
from .qwen2_week2 import Qwen2ModelWeek2


def simple_generate(
    model: Qwen2ModelWeek1, tokenizer: TokenizerWrapper, prompt: str
) -> str:
    pass


def simple_generate_with_kv_cache(
    model: Qwen2ModelWeek2, tokenizer: TokenizerWrapper, prompt: str
) -> str:
    pass
