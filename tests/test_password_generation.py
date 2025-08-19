"""パスワード生成機能のテスト"""
import pytest


def test_4文字のパスワードが生成できる():
    """最小長である4文字のパスワードが生成できることを確認"""
    from password_utils import generate_password
    
    password = generate_password(4)
    
    assert len(password) == 4