class Article:
    all =[]
    def __init__(self, author, magazine, title):
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters inclusive.")
        self._title = title
        self.author = author
        self.magazine = magazine        
        Article.all.append(self)
       
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title is immutable")
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be of type Author.")
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be of type Magazine.")
        self._magazine = value
        
class Author:
    def __init__(self, name):
        if len(name) == 0:
            raise ValueError("Name cannot be empty")
        self._name = name
        self._articles = []
        

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        raise AttributeError("Name cannot be changed")

    
    @property
    def articles(self):
        return self._articles

   
    def magazines(self):
        return list(set(article.magazine for article in Article.all if article.author == self))
        pass

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.articles.append(article)
        return article
        pass

    


    def topic_areas(self):
        categories = {article.magazine.category for article in Article.all if article.author == self}
        return list(categories) if categories else None
        pass

       
class Magazine:
    def __init__(self, name, category):
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        if len(category) == 0:
            raise ValueError("Category cannot be empty")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (2 <= len(value) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters inclusive.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    @property
    def articles(self):
        return self._articles

    @property
    def contributors(self):
        return list(self._contributors)
        
    def add_contributor(self, author):
        if not isinstance(author, Author):
            raise TypeError("Author must be of type Author.")
        self._contributors.add(author)

    
    def article_titles(self):
        return [article.title for article in self._articles]
        pass

    def contributing_authors(self):
        author_article_count = {}
        for article in self._articles:
            author = article.author
            if author not in author_article_count:
                author_article_count[author] = 0
            author_article_count[author] += 1
        
        return [author for author, count in author_article_count.items() if count > 2]
    
    @staticmethod
    def magazine_with_most_articles(magazines):
        return max(magazines, key=lambda mag: len(mag.articles))

        pass
    
    
    
