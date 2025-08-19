"""パスワード生成機能のテスト"""
import string

from password_utils import generate_password


# テスト用の定数
MINIMUM_PASSWORD_LENGTH = 4


def test_4文字のパスワードが生成できる():
    """最小長である4文字のパスワードが生成できることを確認"""
    password = generate_password(MINIMUM_PASSWORD_LENGTH)
    
    assert len(password) == MINIMUM_PASSWORD_LENGTH


def test_生成されたパスワードに大文字が含まれる():
    """パスワードに大文字が必ず含まれることを確認"""
    password = generate_password(MINIMUM_PASSWORD_LENGTH)
    
    assert any(c.isupper() for c in password)


def test_生成されたパスワードに小文字が含まれる():
    """パスワードに小文字が必ず含まれることを確認"""
    password = generate_password(MINIMUM_PASSWORD_LENGTH)
    
    assert any(c.islower() for c in password)


def test_生成されたパスワードに数字が含まれる():
    """パスワードに数字が必ず含まれることを確認"""
    password = generate_password(MINIMUM_PASSWORD_LENGTH)
    
    assert any(c.isdigit() for c in password)


def test_生成されたパスワードに記号が含まれる():
    """パスワードに記号が必ず含まれることを確認"""
    password = generate_password(MINIMUM_PASSWORD_LENGTH)
    
    assert any(c in string.punctuation for c in password)