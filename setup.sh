#!/bin/bash

# QRコード生成Webアプリケーションのセットアップスクリプト
# このスクリプトは必要なパッケージをインストールし、アプリケーションを実行する準備をします

echo "QRコード生成Webアプリケーションのセットアップを開始します..."

# 仮想環境が存在するか確認
if [ ! -d "env" ]; then
    echo "仮想環境を作成しています..."
    python3 -m venv env
    echo "仮想環境を作成しました。"
else
    echo "既存の仮想環境を使用します。"
fi

# 仮想環境をアクティベート
echo "仮想環境をアクティベートしています..."
source env/bin/activate

# 必要なパッケージをインストール
echo "必要なパッケージをインストールしています..."
pip install -r requirements.txt

echo "セットアップが完了しました！"
echo "アプリケーションを起動するには以下のコマンドを実行してください："
echo "source env/bin/activate && streamlit run app.py" 