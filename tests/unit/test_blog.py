from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Title', 'Author')

        self.assertEqual('Title', b.title)
        self.assertEqual('Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test']

        b2 = Blog('Book of Many', 'Test Author')
        b2.posts = ['First post', 'Second post']

        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'Book of Many by Test Author (2 posts)')