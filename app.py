"""
QRコード生成Webアプリケーション

このスクリプトは、Streamlitを使用してテキストからQRコードを生成するWebアプリケーションを提供します。
ユーザーはテキストを入力し、QRコードのサイズや色をカスタマイズして、
複数の形式（PNG、JPG、SVG）でQRコードを保存することができます。

主な機能:
- テキスト入力からQRコードを生成
- QRコードのサイズ調整
- QRコードの色をカスタマイズ
- 複数の形式でQRコードを保存

制限事項:
- 入力テキストが長すぎる場合、QRコードが複雑になり読み取りにくくなる可能性があります
- SVG形式で保存する場合、一部のQRコードリーダーで読み取れない可能性があります
"""

import streamlit as st
import qrcode
import io
import base64
from datetime import datetime
import os


def load_css():
    """
    CSSファイルを読み込んでStreamlitに適用する関数

    戻り値:
        None
    """
    css_file = "style.css"
    if os.path.exists(css_file):
        with open(css_file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def generate_qr_code(text, box_size, border, fill_color, back_color):
    """
    テキストからQRコードを生成する関数

    引数:
        text (str): QRコードに変換するテキスト
        box_size (int): QRコードの各モジュール（黒または白の正方形）のサイズ（ピクセル単位）
        border (int): QRコードの周囲の余白（モジュール単位）
        fill_color (str): QRコードのモジュールの色（16進数カラーコード）
        back_color (str): QRコードの背景色（16進数カラーコード）

    戻り値:
        PIL.Image.Image: 生成されたQRコードの画像
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(text)
    qr.make(fit=True)

    # 16進数カラーコードをRGBタプルに変換
    fill_color_rgb = tuple(
        int(fill_color.lstrip("#")[i : i + 2], 16) for i in (0, 2, 4)
    )
    back_color_rgb = tuple(
        int(back_color.lstrip("#")[i : i + 2], 16) for i in (0, 2, 4)
    )

    img = qr.make_image(fill_color=fill_color_rgb, back_color=back_color_rgb)
    return img


def pil_image_to_bytes(pil_image, format="PNG"):
    """
    PIL Imageオブジェクトをバイト列に変換する関数

    引数:
        pil_image (PIL.Image.Image): 変換するPIL画像オブジェクト
        format (str): 画像形式（'PNG', 'JPEG'など）

    戻り値:
        bytes: 画像のバイト列
    """
    img_byte_arr = io.BytesIO()
    pil_image.save(img_byte_arr, format=format)
    return img_byte_arr.getvalue()


def get_image_download_link(img, filename, format_type):
    """
    画像のダウンロードリンクを生成する関数

    引数:
        img (PIL.Image.Image): ダウンロード対象の画像
        filename (str): ダウンロード時のファイル名
        format_type (str): 画像の形式（'PNG', 'JPEG', 'SVG'）

    戻り値:
        str: ダウンロードリンクのHTML
    """
    buffered = io.BytesIO()

    if format_type == "SVG":
        # SVG形式の場合は特別な処理が必要
        import qrcode.image.svg

        # 既存のQRコードデータを取得
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(st.session_state.qr_text)
        qr.make(fit=True)

        # SVG形式で生成
        factory = qrcode.image.svg.SvgImage
        img_svg = qr.make_image(image_factory=factory)

        # SVGデータをバイト列に変換
        svg_data = io.BytesIO()
        img_svg.save(svg_data)
        svg_bytes = svg_data.getvalue()

        # Base64エンコード
        b64 = base64.b64encode(svg_bytes).decode()

        # SVGのMIMEタイプとファイル拡張子
        mime_type = "image/svg+xml"
        file_ext = "svg"
    else:
        # PNG/JPEG形式の場合
        img.save(buffered, format=format_type)
        b64 = base64.b64encode(buffered.getvalue()).decode()

        # MIMEタイプとファイル拡張子
        mime_type = f"image/{format_type.lower()}"
        file_ext = format_type.lower()

    # ダウンロードリンクを生成
    href = f'<a href="data:{mime_type};base64,{b64}" download="{filename}.{file_ext}">クリックして{format_type}形式でダウンロード</a>'
    return href


def main():
    """
    メイン関数 - Streamlitアプリケーションのエントリーポイント
    """
    st.set_page_config(
        page_title="QRコード生成アプリ", page_icon="📱", layout="centered"
    )

    # CSSを読み込む
    load_css()

    # タイトルとアプリの説明
    st.title("📱 QRコード生成アプリ")
    st.markdown("""
    テキストを入力して、カスタマイズされたQRコードを生成しましょう。
    サイズや色を調整して、お好みの形式でダウンロードできます。
    """)

    # セッション状態の初期化
    if "qr_text" not in st.session_state:
        st.session_state.qr_text = ""
    if "qr_image" not in st.session_state:
        st.session_state.qr_image = None

    # サイドバーにカスタマイズオプションを配置
    with st.sidebar:
        st.header("QRコードのカスタマイズ")

        # QRコードのサイズ設定
        box_size = st.slider(
            "QRコードのサイズ",
            min_value=1,
            max_value=20,
            value=10,
            help="QRコードの各モジュールのサイズ（ピクセル単位）",
        )

        # QRコードの余白設定
        border = st.slider(
            "QRコードの余白",
            min_value=0,
            max_value=10,
            value=4,
            help="QRコードの周囲の余白（モジュール単位）",
        )

        # QRコードの色設定
        fill_color = st.color_picker(
            "QRコードの色", "#000000", help="QRコードのモジュール（黒い部分）の色"
        )
        back_color = st.color_picker("背景色", "#FFFFFF", help="QRコードの背景色")

        # 出力形式の選択
        format_options = ["PNG", "JPEG", "SVG"]
        selected_format = st.selectbox(
            "出力形式", format_options, help="ダウンロードするQRコードの画像形式"
        )

    # メインエリアにテキスト入力とQRコード表示
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("テキスト入力")
        qr_text = st.text_area(
            "QRコードに変換するテキストを入力してください",
            value=st.session_state.qr_text,
            height=150,
            help="URLやテキストなど、QRコードに変換したい内容を入力してください",
        )

        generate_button = st.button("QRコードを生成", type="primary")

        if generate_button and qr_text:
            st.session_state.qr_text = qr_text
            st.session_state.qr_image = generate_qr_code(
                qr_text, box_size, border, fill_color, back_color
            )
            st.success("QRコードが生成されました！")

        elif generate_button and not qr_text:
            st.error("テキストを入力してください")

    with col2:
        st.subheader("生成されたQRコード")

        if st.session_state.qr_image:
            # PIL Imageをバイト形式に変換してから表示
            img_bytes = pil_image_to_bytes(st.session_state.qr_image)
            st.image(img_bytes, caption="生成されたQRコード", use_container_width=True)

            # 現在の日時をファイル名に使用
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"qrcode_{timestamp}"

            # ダウンロードリンクを表示
            st.markdown(
                get_image_download_link(
                    st.session_state.qr_image, filename, selected_format
                ),
                unsafe_allow_html=True,
            )
        else:
            st.info("テキストを入力して「QRコードを生成」ボタンをクリックしてください")

    # フッター
    st.markdown("---")
    st.markdown("© 2023 QRコード生成アプリ | 作成者: toma4423")


if __name__ == "__main__":
    main()
