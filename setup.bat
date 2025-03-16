@echo off
REM QRコード生成Webアプリケーションのセットアップスクリプト（Windows用）
REM このスクリプトは必要なパッケージをインストールし、アプリケーションを実行する準備をします

echo QRコード生成Webアプリケーションのセットアップを開始します...

REM 仮想環境が存在するか確認
if not exist env (
    echo 仮想環境を作成しています...
    python -m venv env
    echo 仮想環境を作成しました。
) else (
    echo 既存の仮想環境を使用します。
)

REM 仮想環境をアクティベート
echo 仮想環境をアクティベートしています...
call env\Scripts\activate.bat

REM 必要なパッケージをインストール
echo 必要なパッケージをインストールしています...
pip install -r requirements.txt

echo セットアップが完了しました！
echo アプリケーションを起動するには以下のコマンドを実行してください：
echo call env\Scripts\activate.bat ^&^& streamlit run app.py

pause 