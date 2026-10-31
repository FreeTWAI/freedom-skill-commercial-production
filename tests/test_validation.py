import unittest
import os

class TestTemplates(unittest.TestCase):
    def setUp(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.result_template_path = os.path.join(base_dir, "RESULT-TEMPLATE.md")
        self.source_register_path = os.path.join(base_dir, "SOURCE-REGISTER.md")

        self.assertTrue(os.path.exists(self.result_template_path))
        self.assertTrue(os.path.exists(self.source_register_path))

        with open(self.result_template_path, "r", encoding="utf-8") as f:
            self.result_template = f.read()

        with open(self.source_register_path, "r", encoding="utf-8") as f:
            self.source_register = f.read()

    def test_result_template_sections(self):
        """Verify milestone delivery checklist validation by checking for required sections."""
        required_sections = [
            "## 拍攝清單",
            "## 製作依賴",
            "## 交付版本",
            "## 回饋"
        ]
        for section in required_sections:
            self.assertIn(section, self.result_template)

    def test_result_template_sign_off_criteria(self):
        """Verify sign-off criteria fields are present."""
        required_fields = [
            "確認狀態",
            "已確認內容",
            "待修改內容與負責人",
            "交付日期與後續安排"
        ]
        for field in required_fields:
            self.assertIn(field, self.result_template)

    def test_source_register_schema(self):
        """Verify asset handover schema checks by ensuring required columns exist."""
        required_columns = [
            "素材／檔名",
            "作者或來源",
            "原始連結／私人證據 ref",
            "可使用範圍與限制",
            "署名方式",
            "本次用途",
            "核對者／日期"
        ]
        for column in required_columns:
            self.assertIn(column, self.source_register)

if __name__ == '__main__':
    unittest.main()
