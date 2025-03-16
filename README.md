# QRコード生成Webアプリケーション

Streamlitを使用して、テキストからQRコードを生成するWebアプリケーションです。

## 機能

- テキスト入力からQRコードを生成
- QRコードのサイズ調整
- QRコードの色をカスタマイズ
- 複数の形式（PNG、JPG、SVG）でQRコードを保存

## インストール方法

1. リポジトリをクローン
   ```
   git clone https://github.com/toma4423/code_of_Q_web.git
   cd code_of_Q_web
   ```

2. 仮想環境を作成して有効化（すでに作成済みの場合はスキップ）
   ```
   python -m venv env
   source env/bin/activate  # Linuxの場合
   # または
   env\Scripts\activate  # Windowsの場合
   ```

3. 必要なパッケージをインストール
   ```
   pip install -r requirements.txt
   ```

## 使用方法

1. アプリケーションを起動
   ```
   streamlit run app.py
   ```

2. ブラウザで表示されるインターフェースを使用してQRコードを生成

## 開発者

- toma4423

## ライセンス

このプロジェクトはオープンソースとして公開されています。 