from unittest import TestCase
from post import Post

# PostTest inherits from TestCase
class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test Content Here')

        # Make sure that post title and content are the same as expected
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content Here', p.content)

    def test_json(self):
        p = Post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}

        self.assertDictEqual(expected, p.json())