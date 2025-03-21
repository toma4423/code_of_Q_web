# QRコード生成アプリケーション 使用方法

このドキュメントでは、QRコード生成アプリケーションの使用方法について説明します。

## 目次

1. [アプリケーションの起動](#アプリケーションの起動)
2. [基本的な使い方](#基本的な使い方)
3. [QRコードのカスタマイズ](#QRコードのカスタマイズ)
4. [QRコードの保存](#QRコードの保存)
5. [トラブルシューティング](#トラブルシューティング)

## アプリケーションの起動

アプリケーションを起動するには、以下の手順に従ってください。

### Macの場合

1. ターミナルを開きます。
2. プロジェクトのディレクトリに移動します。
   ```
   cd path/to/qr_web
   ```
3. 仮想環境を有効化します。
   ```
   source env/bin/activate
   ```
4. アプリケーションを起動します。
   ```
   streamlit run app.py
   ```

### Windowsの場合

1. コマンドプロンプトまたはPowerShellを開きます。
2. プロジェクトのディレクトリに移動します。
   ```
   cd path\to\qr_web
   ```
3. 仮想環境を有効化します。
   ```
   env\Scripts\activate
   ```
4. アプリケーションを起動します。
   ```
   streamlit run app.py
   ```

ブラウザが自動的に開き、アプリケーションが表示されます。表示されない場合は、ターミナルに表示されるURLをブラウザで開いてください（通常は http://localhost:8501 です）。

## 基本的な使い方

1. テキスト入力欄に、QRコードに変換したいテキストを入力します。
   - URLやテキスト、連絡先情報など、任意のテキストを入力できます。
2. 「QRコードを生成」ボタンをクリックします。
3. 右側のパネルにQRコードが表示されます。

## QRコードのカスタマイズ

左側のサイドバーには、QRコードをカスタマイズするためのオプションがあります。

### サイズの調整

「QRコードのサイズ」スライダーを使用して、QRコードのサイズを調整できます。値が大きいほど、QRコードが大きくなります。

### 余白の調整

「QRコードの余白」スライダーを使用して、QRコードの周囲の余白を調整できます。値が大きいほど、余白が広くなります。

### 色の設定

- 「QRコードの色」カラーピッカーを使用して、QRコードのモジュール（黒い部分）の色を変更できます。
- 「背景色」カラーピッカーを使用して、QRコードの背景色を変更できます。

### 出力形式の選択

「出力形式」ドロップダウンメニューから、QRコードの保存形式を選択できます。

- PNG: 一般的な画像形式で、透明背景をサポートしています。
- JPEG: 写真などの画像に適した形式です。
- SVG: ベクター形式で、サイズを変更しても品質が低下しません。

## QRコードの保存

QRコードを生成した後、右側のパネルに表示されるダウンロードリンクをクリックして、QRコードを保存できます。選択した形式（PNG、JPEG、SVG）でダウンロードされます。

ファイル名には現在の日時が含まれるため、複数のQRコードを生成しても上書きされることはありません。

## トラブルシューティング

### QRコードが生成されない

- テキスト入力欄が空でないことを確認してください。
- 入力テキストが非常に長い場合、QRコードの生成に時間がかかる場合があります。

### QRコードが読み取れない

- QRコードのサイズを大きくしてみてください。
- QRコードの色と背景色のコントラストが十分であることを確認してください。
- 非常に長いテキストの場合、QRコードが複雑になり、一部のスキャナーで読み取りにくくなる可能性があります。

### SVG形式のQRコードが読み取れない

一部のQRコードリーダーはSVG形式をサポートしていない場合があります。PNG形式を使用してみてください。

### その他の問題

アプリケーションを再起動してみてください。それでも問題が解決しない場合は、以下の情報を含むイシューを報告してください。

- 使用しているオペレーティングシステム
- ブラウザの種類とバージョン
- 問題の詳細な説明
- 可能であれば、問題を再現する手順 