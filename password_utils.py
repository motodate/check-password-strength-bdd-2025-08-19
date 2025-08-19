"""パスワードユーティリティモジュール"""


def generate_password(length: int) -> str:
    """指定された長さのパスワードを生成する"""
    required_chars = "Aa1!"
    remaining_length = length - len(required_chars)
    return required_chars + "A" * remaining_length