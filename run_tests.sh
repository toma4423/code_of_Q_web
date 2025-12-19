#!/bin/bash

# QRコード生成アプリケーションのテスト実行スクリプト
# このスクリプトはテストを実行し、結果を表示します

echo "QRコード生成アプリケーションのテストを開始します..."

# uvを使用してテストを実行
uv run python -m unittest test_qr_generator.py

# 終了ステータスを取得
status=$?

if [ $status -eq 0 ]; then
    echo "すべてのテストが成功しました！"
else
    echo "テストに失敗しました。エラーを確認してください。"
fi

exit $status