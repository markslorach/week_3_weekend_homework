from models.book import *

book_1 = Book("The 4-Hour Work Week",
              "Timothy Ferriss",
              "Self-help",
              "The 4-Hour Work Week is a book by Timothy Ferriss that teaches how to reconstruct your life so it’s not all about work. It provides a blueprint for luxury lifestyle design and includes practical tips and case studies for doubling income, overcoming common sticking points, and reinventing oneself. The book teaches how to outsource your life to overseas virtual assistants for $5 per hour, how to eliminate 50 percent of your work in 48 hours using the principles of a forgotten Italian economist, and how to trade a long-haul career for short work bursts and frequent 'mini-retirements’.",
              True)

book_2 = Book("Most Dope: The Extraordinary Life of Mac Miller",
              "Paul Cantor",
              "Biography",
              "Mac Miller was a talented rapper, singer, and producer who rose to fame in the early 2010s. He was known for his unique blend of hip-hop, jazz, and rock, and his music often explored themes of love, loss, and addiction. Miller struggled with substance abuse throughout his career, and he died of an accidental overdose in 2018 at the age of 26. In his book, Most Dope: The Extraordinary Life of Mac Miller, Paul Cantor tells the story of Miller's life and career. Cantor draws on interviews with Miller's friends, family, and collaborators to paint a portrait of a complex and talented artist who was both loved and troubled. The book is a moving and insightful look at the life of one of the most promising young artists of his generation.",
              False)

book_3 = Book("HTML & CSS",
              "Jon Duckett",
              "Education",
              "HTML & CSS by Jon Duckett is a comprehensive guide that explores the fundamentals of web development using HTML and CSS. The book provides a clear and beginner-friendly approach, making it suitable for both novices and experienced developers looking to enhance their skills. With a visually appealing layout and interactive examples, Duckett demystifies the building blocks of the web, covering topics such as structuring web pages with HTML, applying styles and layouts with CSS, and responsive design. The book equips readers with the knowledge needed to create visually appealing and functional websites, making it an invaluable resource for aspiring web developers.",
              False)

book_4 = Book("Your Head is a Houseboat",
              "Campbell Walker",
              "Self-help",
              "Your Head is a Houseboat is a book by Campbell Walker that provides a uniquely hilarious guide to what goes on in your brain. The book demystifies brain functions, mental health, emotions, mindfulness and psychology with less complex terminology and more bizarre metaphors. It’s filled with illustrations, journal exercises and words that will probably hit too close to home. At its core, this is a funny, accessible approach to understanding your head and making it a nicer place to live1.",
              True)

books = [book_1, book_2, book_3, book_4]

# Add a book to the list
def add_new_book(book):
    books.append(book)

# Remove a book from the list
def remove_book_by_index(index):
    books.pop(index)


