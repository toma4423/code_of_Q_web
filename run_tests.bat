@echo off
REM QRコード生成アプリケーションのテスト実行スクリプト（Windows用）
REM このスクリプトはテストを実行し、結果を表示します

echo QRコード生成アプリケーションのテストを開始します...

REM uvを使用してテストを実行
uv run python -m unittest test_qr_generator.py

REM 終了ステータスを取得
set status=%errorlevel%

if %status%==0 (
    echo すべてのテストが成功しました！
) else (
    echo テストに失敗しました。エラーを確認してください。
)

exit /b %status%