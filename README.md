# パスワードユーティリティツール - BDD/TDD練習リポジトリ

このリポジトリは、BDD（振る舞い駆動開発） と TDD（テスト駆動開発）の実践的な学習を目的としたパスワード関連機能の実装プロジェクトです。

## 🎯 学習目的

- **BDD**: Gherkinシナリオから機能要件を明確化
- **TDD**: Red-Green-Blueサイクルでの堅実な開発
- **品質保証**: 自動テスト・コード品質ツールの活用
- **モダンPython開発**: pyproject.toml、ruff等の最新ツール使用

## 📋 機能概要

パスワードに関する以下の操作を提供：

### 1. パスワード強度チェック (`check_strength`) ⏳ 未実装
- **入力**: パスワード文字列
- **出力**: 強度レベル（非常に弱い、弱い、普通、強い、非常に強い）
- **判定基準**: 文字数と文字種（大文字・小文字・数字・記号）

### 2. パスワード生成 (`generate_password`) ✅ 完成
- **入力**: 文字数（4〜100文字）
- **出力**: セキュアなランダムパスワード
- **特徴**: 4種類の文字種を必ず含む、完全ランダム

### 3. パスワードリスト生成 (`generate_password_list`) ⏳ 未実装
- **入力**: 生成数、各パスワードの文字数
- **出力**: パスワードのリスト
- **特徴**: 各パスワードがユニーク

## 🛠️ 技術スタック

- **言語**: Python 3.13
- **テストフレームワーク**: pytest
- **コード品質ツール**:
  - **フォーマッター**: Black (120文字制限)
  - **リンター**: Ruff (高速、flake8互換)
- **実行環境**: pipenv

## 📁 プロジェクト構造

```
.
├── docs/
│   ├── features/           # BDDシナリオ（Gherkin形式）
│   │   ├── password_generation.feature      # ✅ パスワード生成機能
│   │   ├── password_strength.feature        # ⏳ パスワード強度チェック機能
│   │   └── password_list_generation.feature # ⏳ パスワードリスト生成機能
│   └── reqirement.md       # 要件定義書
├── tests/
│   └── test_password_generation.py  # ✅ パスワード生成機能のテスト（12項目）
├── password_utils.py       # ✅ コアライブラリ
├── pyproject.toml         # 統一設定ファイル
└── README.md              # このファイル
```

## 🚀 セットアップ

### 1. 環境構築

```bash
# リポジトリをクローン
git clone <repository-url>
cd check-password-strength-bdd-2025-08-19

# 依存関係をインストール
pipenv install --dev
pipenv shell
```

### 2. テスト実行

```bash
# 全テスト実行（環境変数設定不要！）
pipenv run pytest

# 詳細表示でテスト実行
pipenv run pytest -v

# 特定のテストファイルのみ実行
pipenv run pytest tests/test_password_generation.py
```

### 3. コード品質チェック

```bash
# リンター（構文・スタイルチェック）
pipenv run ruff check .

# フォーマッター（コード整形）
pipenv run black .

# フォーマット確認（変更せず確認のみ）
pipenv run black --check .
```

### 4. 統合チェック（CI相当）

```bash
# テスト + 品質チェックを一括実行
pipenv run pytest && pipenv run ruff check . && pipenv run black --check .
```

## 📝 BDDシナリオ例

### パスワード生成機能の振る舞い
```gherkin
Feature: パスワード生成機能
  指定された長さで、大文字・小文字・数字・記号を含むセキュアなパスワードを生成する

  Scenario: 最小長4文字のパスワードを生成する
    When 長さ 4 のパスワードを生成する
    Then 生成されたパスワードの長さは 4 である
    And パスワードに大文字が含まれる
    And パスワードに小文字が含まれる
    And パスワードに数字が含まれる
    And パスワードに記号が含まれる

  Scenario: 3文字以下のパスワード生成でエラーが発生する
    When 長さ 3 のパスワードを生成する
    Then エラー "4種類の文字を含めるには最低4文字必要です" が発生する
```

## 🔄 TDD開発サイクル

このプロジェクトは**Red-Green-Blue**サイクルで開発されました：

### 🔴 Red: 失敗するテスト作成
```python
def test_4文字のパスワードが生成できる():
    password = generate_password(MINIMUM_PASSWORD_LENGTH)
    assert len(password) == MINIMUM_PASSWORD_LENGTH
```
→ `ModuleNotFoundError: No module named 'password_utils'`

### 🟢 Green: 最小限の実装
```python
def generate_password(length: int) -> str:
    return "Aa1!"  # まず最小限でテストをパスさせる
```
→ テストがパス！

### 🔵 Blue: リファクタリング
```python
def generate_password(length: int) -> str:
    if length is None:
        raise TypeError("長さがnullです")
    # ... 完全なランダム生成実装
```
→ 機能完成、コミット

## 🧪 テスト構成

### ✅ パスワード生成機能（12テストケース完了）

**正常系:**
- 最小長4文字の生成
- 最大長100文字の生成  
- ユニーク性確認

**異常系:**
- 文字数範囲外（3文字以下、101文字以上、負の数）
- 型エラー（文字列、null指定）

**品質保証:**
- 4種類の文字種を必ず含む
- 完全ランダム生成
- 厳密なバリデーション

## 📈 開発進捗

- ✅ **パスワード生成機能**: 完全実装（12テスト通過）
- ⏳ **パスワード強度チェック機能**: 未実装
- ⏳ **パスワードリスト生成機能**: 未実装  
- ⏳ **CLI機能**: 未実装

## 🎓 学習ポイント

### BDDで学べること
- ビジネス要件からテストシナリオへの変換
- Given-When-Then形式での振る舞い定義
- ステークホルダーとの共通言語としてのGherkin

### TDDで学べること
- **一度に一つの失敗するテスト**から始める重要性
- テスト駆動による設計の改善
- Red→Green→Blueサイクルの実践
- リファクタリングの安全な実施方法

### 品質管理で学べること
- 自動テストによる継続的品質保証
- モダンなPython品質ツール（ruff, black）
- pyproject.tomlでの統一設定管理

### 開発環境で学べること
- **pipenvによる依存関係管理**
- **pyproject.tomlでのツール統一設定**
- **pytest設定によるモジュール解決**（環境変数不要）

## 🤝 貢献方法

1. 新しいBDDシナリオの追加
2. 未実装機能のTDD実装
3. テストケースの拡充
4. ドキュメント改善

## 📄 ライセンス

MIT License

---

**このリポジトリで、BDD/TDDの実践的なスキルを身につけましょう！**

*環境変数設定不要で、`pipenv run pytest`一発で動きます 🚀*
