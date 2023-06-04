import unittest
from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        
        self.book = Book(
            title = "Test Book",
            author = "Test Author",
            genre = "Test Genre",
            description = "Test Description",
            available = "available")
        

    def test_title(self):
        self.assertEqual(self.book.title, "Test Book")

    def test_author(self):
        self.assertEqual(self.book.author, "Test Author")

    
    def test_genre(self):
        self.assertEqual(self.book.genre, "Test Genre")

    def test_description(self):
        self.assertEqual(self.book.description, "Test Description")

    def test_available(self):
        self.assertEqual(self.book.available, "available")

    
    
