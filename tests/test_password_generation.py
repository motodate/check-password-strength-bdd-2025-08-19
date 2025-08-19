"""パスワード生成機能のテスト"""
import string
import pytest

from password_utils import generate_password


# テスト用の定数
MINIMUM_PASSWORD_LENGTH = 4
MAXIMUM_PASSWORD_LENGTH = 100


def test_4文字のパスワードが生成できる():
    password = generate_password(MINIMUM_PASSWORD_LENGTH)
    
    assert len(password) == MINIMUM_PASSWORD_LENGTH


def test_生成されたパスワードに大文字が含まれる():
    password = generate_password(MINIMUM_PASSWORD_LENGTH)
    
    assert any(c.isupper() for c in password)


def test_生成されたパスワードに小文字が含まれる():
    password = generate_password(MINIMUM_PASSWORD_LENGTH)
    
    assert any(c.islower() for c in password)


def test_生成されたパスワードに数字が含まれる():
    password = generate_password(MINIMUM_PASSWORD_LENGTH)
    
    assert any(c.isdigit() for c in password)


def test_生成されたパスワードに記号が含まれる():
    password = generate_password(MINIMUM_PASSWORD_LENGTH)
    
    assert any(c in string.punctuation for c in password)


def test_100文字のパスワードが生成できる():
    password = generate_password(MAXIMUM_PASSWORD_LENGTH)
    
    assert len(password) == MAXIMUM_PASSWORD_LENGTH


def test_生成されたパスワードはユニークである():
    password1 = generate_password(12)
    password2 = generate_password(12)
    
    assert password1 != password2


def test_3文字以下のパスワード生成でエラーが発生する():
    with pytest.raises(ValueError, match="4種類の文字を含めるには最低4文字必要です"):
        generate_password(3)


def test_負の長さのパスワード生成でエラーが発生する():
    with pytest.raises(ValueError, match="4種類の文字を含めるには最低4文字必要です"):
        generate_password(-1)


def test_101文字のパスワード生成でエラーが発生する():
    with pytest.raises(ValueError, match="パスワードの長さは4〜100である必要があります"):
        generate_password(MAXIMUM_PASSWORD_LENGTH + 1)


def test_文字列での長さ指定でエラーが発生する():
    with pytest.raises(TypeError, match="長さは整数である必要があります"):
        generate_password("twelve")  # type: ignore


def test_nullでの長さ指定でエラーが発生する():
    with pytest.raises(TypeError, match="長さがnullです"):
        generate_password(None)  # type: ignore