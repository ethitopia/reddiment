#for short stories, people can add their own stores, need help designing actual application that can implement cloud reading app 
#looking for: 
"""
users have a library of books that they can add to or remove from 
users can set a book from their library as active
the reading application remembers where a user left off in a given book 
the reading app only displays a page of text at a time in active book
"""

class Book: 
    """
    book class
    """
    def __init__(self, title, content, pages): 
        self.title = title 
        self.content = content
        self.pages = pages 
        self.isactive = False
        
    def set_active(self): 
        self.isactive = True
        
    def display_page(self, page): 
        for _, a in enumerate(self.pages): 
            if a == page: 
                return page 
        

class libApp: 
    """
    library app to store reader's books, and where they left off per each book.
    """
    
    def __init__(self): 
        self.library = []
        
    def set_active(self, book : Book): 
        """
        sets book in library as active
        """ 
        if book in self.library:
            book.set_active()
            
    def add(self, book): 
        if book not in self.library: 
            self.library[book]
            
    def remove(self, book): 
        if book in self.library: 
            self.library.pop(book)
            
    def display_page(self, book): 
        if book in self.library: 
            book.display_page()
            
    
    
            

            
            
        
        
    
     
    