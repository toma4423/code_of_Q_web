"""
QRコード生成機能のテストスクリプト

このスクリプトは、QRコード生成アプリケーションの主要機能をテストします。
QRコードの生成、色の設定、サイズの設定などの機能が正しく動作することを確認します。

主なテスト項目:
- QRコードの生成
- 色の設定
- サイズの設定
- エラー処理
"""

import unittest
from PIL import Image
import os
import sys

# アプリケーションのモジュールをインポートするためのパスを追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# app.pyからgenerate_qr_code関数をインポート
from app import generate_qr_code


class TestQRGenerator(unittest.TestCase):
    """
    QRコード生成機能のテストクラス
    """

    def check_image_type(self, img):
        """
        画像オブジェクトが有効か確認するヘルパー関数
        qrcode 8.x以降はPilImageラッパーを返すことがあるため、
        厳密な型チェックではなく、必要な属性（save, size）を持つか確認する
        """
        self.assertTrue(hasattr(img, 'save'), "Image object should have 'save' method")
        self.assertTrue(hasattr(img, 'size'), "Image object should have 'size' attribute")

    def test_generate_qr_code(self):
        """
        基本的なQRコード生成機能をテストする

        テスト内容:
        - テキストからQRコードが正しく生成されるか
        - 生成されたQRコードが有効なオブジェクトであるか
        """
        # テスト用のテキスト
        test_text = "https://example.com"

        # QRコードを生成
        qr_image = generate_qr_code(
            text=test_text,
            box_size=10,
            border=4,
            fill_color="#000000",
            back_color="#FFFFFF",
        )

        # 生成されたQRコードが有効であることを確認
        self.check_image_type(qr_image)

        # 画像のサイズが正しいことを確認
        # qrcode 8.xでのサイズ計算（Version 2相当になる場合があるため、実測値に合わせる）
        # 33 modules * 10 = 330
        expected_size = (330, 330)
        self.assertEqual(qr_image.size, expected_size)

    def test_custom_colors(self):
        """
        カスタム色設定のテストを行う

        テスト内容:
        - カスタム色（赤いQRコード、青い背景）が正しく適用されるか
        """
        # テスト用のテキスト
        test_text = "https://example.com"

        # カスタム色でQRコードを生成（赤いQRコード、青い背景）
        qr_image = generate_qr_code(
            text=test_text,
            box_size=10,
            border=4,
            fill_color="#FF0000",  # 赤
            back_color="#0000FF",  # 青
        )

        # 生成されたQRコードが有効であることを確認
        self.check_image_type(qr_image)

    def test_different_sizes(self):
        """
        異なるサイズ設定のテストを行う

        テスト内容:
        - 小さいサイズ（box_size=5）のQRコードが正しく生成されるか
        - 大きいサイズ（box_size=15）のQRコードが正しく生成されるか
        """
        # テスト用のテキスト
        test_text = "https://example.com"

        # 小さいサイズでQRコードを生成
        small_qr = generate_qr_code(
            text=test_text,
            box_size=5,
            border=4,
            fill_color="#000000",
            back_color="#FFFFFF",
        )

        # 大きいサイズでQRコードを生成
        large_qr = generate_qr_code(
            text=test_text,
            box_size=15,
            border=4,
            fill_color="#000000",
            back_color="#FFFFFF",
        )

        # 小さいQRコードのサイズを確認
        # 33 modules * 5 = 165
        expected_small_size = (165, 165)
        self.assertEqual(small_qr.size, expected_small_size)

        # 大きいQRコードのサイズを確認
        # 33 modules * 15 = 495
        expected_large_size = (495, 495)
        self.assertEqual(large_qr.size, expected_large_size)

    def test_long_text(self):
        """
        長いテキストのテストを行う

        テスト内容:
        - 長いテキストからQRコードが正しく生成されるか
        """
        # 長いテキスト
        long_text = "https://example.com/" + "a" * 1000

        # QRコードを生成
        qr_image = generate_qr_code(
            text=long_text,
            box_size=10,
            border=4,
            fill_color="#000000",
            back_color="#FFFFFF",
        )

        # 生成されたQRコードが有効であることを確認
        self.check_image_type(qr_image)

        # 長いテキストの場合、QRコードのバージョンが上がるため、サイズが大きくなる
        min_size = (330, 330)
        self.assertGreaterEqual(qr_image.size[0], min_size[0])
        self.assertGreaterEqual(qr_image.size[1], min_size[1])


if __name__ == "__main__":
    unittest.main()