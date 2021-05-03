from mongoengine import Document, StringField, ListField, EmbeddedDocumentField, IntField, EmbeddedDocument, connect
import json


class Author_profile(EmbeddedDocument):
    experience = IntField()
    courses = IntField()
    books = IntField()

    def __str__(self):
        return {
            "experience": self.experience,
            "courses": self.courses,
            "books": self.books
        }



class Author(EmbeddedDocument):
    auth_pro=Author_profile()
    name = StringField()
    call_name = StringField()
    profile = EmbeddedDocumentField(Author_profile)

    def __str__(self):
        return {
            "name":self.name,
            "call_name":self.call_name,
            "profile":self.auth_pro.__str__()
        }


class Mains(Document):
    author = Author()
    tittle = StringField()
    isbn = StringField()
    downloadable = StringField()
    no_of_reviews = IntField()
    tags = ListField()
    languages = ListField()
    author_details = EmbeddedDocumentField(Author)

    def to_json(self):
        return {
            "tittle": self.tittle,
            "isbn": self.isbn,
            "downloadable": self.downloadable,
            "no_of_reviews": self.no_of_reviews,
            "tags": self.tags,
            "languages": self.languages,
            "author_details": self.author.__str__()
        }
