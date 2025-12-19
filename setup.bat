@echo off
REM QRコード生成Webアプリケーションのセットアップスクリプト（Windows用）
REM このスクリプトは必要なパッケージをインストールし、アプリケーションを実行する準備をします

echo QRコード生成Webアプリケーションのセットアップを開始します...

REM uvを使用して依存関係を同期
uv sync

echo セットアップが完了しました！
echo アプリケーションを起動するには以下のコマンドを実行してください：
echo uv run streamlit run app.py

pause