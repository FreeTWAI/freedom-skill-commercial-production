import unittest
import json
import os
from urllib.parse import urlparse

class TestSkillBookValidation(unittest.TestCase):
    def setUp(self):
        self.skill_book_path = 'skill-book.json'
        with open(self.skill_book_path, 'r', encoding='utf-8') as f:
            self.skill_book = json.load(f)

    def test_schema_keys(self):
        """Verify the required keys are present in skill-book.json."""
        required_keys = ['format', 'id', 'title', 'version', 'guild_key', 'entry', 'execution', 'repository', 'license']
        for key in required_keys:
            self.assertIn(key, self.skill_book, f"Missing required key: {key}")

    def test_entry_path_traversal(self):
        """Verify entry path does not contain path traversal characters."""
        entry = self.skill_book.get('entry', '')
        # Check for path traversal elements
        self.assertNotIn('..', entry, "Entry path contains '..'")
        self.assertNotIn('/', entry, "Entry path contains '/'")
        self.assertNotIn('\\', entry, r"Entry path contains '\'")

        # Verify it points to an existing file
        self.assertTrue(os.path.exists(entry), f"Entry file '{entry}' does not exist")
        self.assertTrue(os.path.isfile(entry), f"Entry '{entry}' is not a file")

    def test_repository_url(self):
        """Verify repository URL is from authorized domains."""
        repo_url = self.skill_book.get('repository', '')
        parsed_url = urlparse(repo_url)

        # Only allow github.com
        self.assertEqual(parsed_url.scheme, 'https', "Repository URL must use https")
        self.assertEqual(parsed_url.netloc, 'github.com', "Repository URL must be on github.com")
        self.assertTrue(parsed_url.path.startswith('/FreeTWAI-AI/'), "Repository must be in FreeTWAI-AI org")

    def test_no_secrets(self):
        """Verify there are no unexpected keys in the JSON."""
        allowed_keys = {'format', 'id', 'title', 'version', 'guild_key', 'entry', 'execution', 'repository', 'license'}
        for key in self.skill_book.keys():
            self.assertIn(key, allowed_keys, f"Found unexpected key which could be a secret: {key}")

if __name__ == '__main__':
    unittest.main()
