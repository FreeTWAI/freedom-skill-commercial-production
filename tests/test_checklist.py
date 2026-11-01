import unittest
import os

class TestChecklist(unittest.TestCase):
    def test_deliverables_checklist(self):
        filepath = 'RESULT-TEMPLATE.md'
        self.assertTrue(os.path.exists(filepath), f"File {filepath} does not exist")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Validate the "交付版本" (Deliverables) checklist headers
        self.assertIn('## 交付版本', content)
        self.assertIn('| 檔名／版本 | 渠道 | 尺寸／比例 | 時長 | 字幕／封面 | 成果連結或私人 ref | 確認狀態 |', content)
        self.assertIn('|---|---|---|---|---|---|---|', content)

    def test_handover_checklist(self):
        filepath = 'SKILL.md'
        self.assertTrue(os.path.exists(filepath), f"File {filepath} does not exist")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Validate the "完成時交付" (Handover) checklist items
        self.assertIn('## 完成時交付', content)
        self.assertIn('1. 雙方確認的拍攝 brief 與鏡位清單。', content)
        self.assertIn('2. 實際照片／影片，或明確標示未拍攝的企劃成果。', content)
        self.assertIn('3. 交付版本表、素材來源與仍待補齊的項目。', content)
        self.assertIn('4. 修改紀錄與下一步。', content)

if __name__ == '__main__':
    unittest.main()
