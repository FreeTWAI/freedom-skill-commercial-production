import unittest
import os

class TestTemplates(unittest.TestCase):
    def test_result_template_sections(self):
        filepath = 'RESULT-TEMPLATE.md'
        self.assertTrue(os.path.exists(filepath), f"File {filepath} does not exist")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn('## 拍攝清單', content)
        self.assertIn('## 製作依賴', content)
        self.assertIn('## 交付版本', content)
        self.assertIn('## 回饋', content)

    def test_skill_md_sections(self):
        filepath = 'SKILL.md'
        self.assertTrue(os.path.exists(filepath), f"File {filepath} does not exist")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn('# 廣告攝影與影片製作入門', content)
        self.assertIn('## 把「拍得漂亮」變成可確認的需求', content)
        self.assertIn('## 用最少鏡頭說清楚商品', content)
        self.assertIn('## 開拍前核對依賴', content)
        self.assertIn('## 以交付版本組織後製', content)
        self.assertIn('## 完成時交付', content)

    def test_source_register_sections(self):
        filepath = 'SOURCE-REGISTER.md'
        self.assertTrue(os.path.exists(filepath), f"File {filepath} does not exist")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn('# 素材來源紀錄', content)
        self.assertIn('| 素材／檔名 | 作者或來源 | 原始連結／私人證據 ref | 可使用範圍與限制 | 署名方式 | 本次用途 | 核對者／日期 |', content)

if __name__ == '__main__':
    unittest.main()
