from fastapi import APIRouter, Response
from db import SessionDep
from dto import BookDto
from sqlmodel import select
from model import Book
from typing import Union

book_router = APIRouter()

@book_router.get("/books")
def getAllbooks(session: SessionDep):
    return session.exec(select(Book)).all()

@book_router.post("/books")
def createBook(bookDto: BookDto, session: SessionDep):
    book = bookDto.toBook()
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

@book_router.get("/books/search")
def searchBook(session: SessionDep, title: str | None = None, author: str | None = None,):
    query = select(Book)
    if title:
        query = query.filter(Book.title == title)
    if author:
        query = query.filter(Book.author == author)
    return session.exec(query).all()

@book_router.put("/books/{id}")
def changeBook(id: int, bookDto: BookDto, session: SessionDep):
    book = session.get(Book, id)
    book.title = bookDto.title
    book.author = bookDto.author
    session.commit()
    session.refresh(book)
    return book

@book_router.delete("/books/{id}")
def deleteBook(id: int, session: SessionDep):
    book = session.get(Book, id)
    session.delete(book)
    session.commit()
    return {"message": "Book deleted successfully"}

@book_router.post("/books/{id}/borrow")
def borrowBook(id: int, session: SessionDep, resp: Response):
    book = session.get(Book, id)
    if not book.availability:
        resp.status_code = 404
        return {"message": "Book is already borrowed"}
    book.availability = False
    session.commit()
    session.refresh(book)
    return book
