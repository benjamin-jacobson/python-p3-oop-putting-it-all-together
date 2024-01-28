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
        if isnstance(title,str) and len(title)>0:
            self._title = title
        else:
            raise ValueError("Title must be string  more than 1 character." )

        