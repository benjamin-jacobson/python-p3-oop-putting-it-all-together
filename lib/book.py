#!/usr/bin/env python3

class Book:
    
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title,str) and len(title)>0:
            self._title = title
        else:
            raise ValueError("Title must be string  more than 1 character." )

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        #c = self.page_count + 1
        print("Flipping the page...wow, you read fast!")
