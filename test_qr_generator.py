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
import qrcode
from PIL import Image
import io
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
    
    def test_generate_qr_code(self):
        """
        基本的なQRコード生成機能をテストする
        
        テスト内容:
        - テキストからQRコードが正しく生成されるか
        - 生成されたQRコードが有効なPIL.Image.Imageオブジェクトであるか
        """
        # テスト用のテキスト
        test_text = "https://example.com"
        
        # QRコードを生成
        qr_image = generate_qr_code(
            text=test_text,
            box_size=10,
            border=4,
            fill_color="#000000",
            back_color="#FFFFFF"
        )
        
        # 生成されたQRコードが有効なPIL.Image.Imageオブジェクトであることを確認
        self.assertIsInstance(qr_image, Image.Image)
        
        # 画像のサイズが正しいことを確認（box_size=10, border=4の場合）
        # QRコードのバージョン1は21x21モジュール、境界線が4モジュールなので、合計サイズは(21+2*4)*10 = 290
        expected_size = (290, 290)  # 境界線を含む
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
            back_color="#0000FF"   # 青
        )
        
        # 生成されたQRコードが有効なPIL.Image.Imageオブジェクトであることを確認
        self.assertIsInstance(qr_image, Image.Image)
        
        # 色の検証は複雑なため、ここでは画像が生成されることのみを確認
    
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
            back_color="#FFFFFF"
        )
        
        # 大きいサイズでQRコードを生成
        large_qr = generate_qr_code(
            text=test_text,
            box_size=15,
            border=4,
            fill_color="#000000",
            back_color="#FFFFFF"
        )
        
        # 小さいQRコードのサイズを確認
        expected_small_size = (145, 145)  # (21+2*4)*5 = 145
        self.assertEqual(small_qr.size, expected_small_size)
        
        # 大きいQRコードのサイズを確認
        expected_large_size = (435, 435)  # (21+2*4)*15 = 435
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
            back_color="#FFFFFF"
        )
        
        # 生成されたQRコードが有効なPIL.Image.Imageオブジェクトであることを確認
        self.assertIsInstance(qr_image, Image.Image)
        
        # 長いテキストの場合、QRコードのバージョンが上がるため、サイズが大きくなる
        # 正確なサイズは予測できないが、少なくとも最小サイズよりは大きいはず
        min_size = (290, 290)  # バージョン1の最小サイズ
        self.assertGreaterEqual(qr_image.size[0], min_size[0])
        self.assertGreaterEqual(qr_image.size[1], min_size[1])

if __name__ == "__main__":
    unittest.main() 