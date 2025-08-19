"""パスワードユーティリティモジュール"""
import random
import string


def generate_password(length: int) -> str:
    """指定された長さのパスワードを生成する"""
    # 必須文字を各カテゴリから1つずつ
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)
    
    required_chars = [uppercase, lowercase, digit, symbol]
    
    # 残りの文字をランダム生成
    all_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    remaining_length = length - len(required_chars)
    remaining_chars = [random.choice(all_chars) for _ in range(remaining_length)]
    
    # 全文字をシャッフル
    all_password_chars = required_chars + remaining_chars
    random.shuffle(all_password_chars)
    
    return ''.join(all_password_chars)