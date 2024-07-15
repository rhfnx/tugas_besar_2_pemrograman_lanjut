from pydantic import BaseModel  # type: ignore

class BukuBase(BaseModel):
    judul: str
    penulis: str
    penerbit: str | None = None
    tahun_terbit: int | None = None
    konten: str
    iktisar: str

class BukuCreate(BukuBase):
    pass

class BukuUpdate(BukuBase):
    pass

class Buku(BukuBase):
    id: int

    class Config:
        orm_mode = True
