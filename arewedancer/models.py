from typing import Optional, List

from pydantic import BaseModel, Field


class Patient(BaseModel):
    name: str
    surname: str


class Track(BaseModel):
    TrackId: int
    Name: str
    AlbumId: Optional[int]
    MediaTypeId: int
    GenreId: Optional[int]
    Composer: Optional[str]
    Milliseconds: int
    Bytes: Optional[int]
    UnitPrice: float


class NewAlbumRequest(BaseModel):
    title: str
    artist_id: int


class Album(BaseModel):
    AlbumId: int
    Title: str
    ArtistId: int


class CustomerUpdateRequest(BaseModel):
    company: str = None
    address: str = None
    city: str = None
    state: str = None
    country: str = None
    postalcode: str = None
    fax: str = None


class Customer(BaseModel):
    CustomerId: int
    FirstName: str
    LastName: str
    Company: str
    Address: str
    City: str
    State: str
    Country: str
    PostalCode: str
    Phone: str
    Fax: str
    Email: str
    SupportRepId: int


class CustomerExpense(BaseModel):
    CustomerId: int
    Email: str
    Phone: Optional[str]
    Sum: float = Field(..., alias="number")


class GenreSales(BaseModel):
    Name: str
    Sum: int = Field(..., alias="number")
