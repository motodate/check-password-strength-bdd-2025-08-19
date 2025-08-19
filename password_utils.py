"""パスワードユーティリティモジュール"""


def generate_password(length: int) -> str:
    """指定された長さのパスワードを生成する"""
    return "A" * length