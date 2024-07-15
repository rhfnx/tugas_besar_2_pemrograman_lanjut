from fastapi import FastAPI, HTTPException # type: ignore
import crud, schemas
import logging

app = FastAPI()

# Konfigurasi logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/buku/", response_model=list[schemas.Buku])
async def get_buku():
    try:
        buku_list = crud.get_buku()
        logger.info("Data buku berhasil diambil dari basis data.")
        return buku_list
    except Exception as e:
        logger.error(f"Terjadi kesalahan: {e}")
        raise HTTPException(status_code=500, detail="Terjadi kesalahan pada server")

@app.get("/buku/{buku_id}", response_model=schemas.Buku)
async def get_buku_by_id(buku_id: int):
    try:
        buku = crud.get_buku_by_id(buku_id)
        if buku is None:
            raise HTTPException(status_code=404, detail="Buku tidak ditemukan")
        logger.info(f"Data buku dengan ID {buku_id} berhasil diambil dari basis data.")
        return buku
    except Exception as e:
        logger.error(f"Terjadi kesalahan: {e}")
        raise HTTPException(status_code=500, detail="Terjadi kesalahan pada server")

@app.post("/buku/", response_model=schemas.Buku)
async def create_buku(buku: schemas.BukuCreate):
    try:
        buku_created = crud.create_buku(buku)
        logger.info("Buku berhasil disimpan ke basis data.")
        return buku_created
    except Exception as e:
        logger.error(f"Terjadi kesalahan: {e}")
        raise HTTPException(status_code=500, detail="Terjadi kesalahan pada server")

@app.put("/buku/{buku_id}", response_model=schemas.Buku)
async def update_buku(buku_id: int, buku: schemas.BukuUpdate):
    try:
        buku_updated = crud.update_buku(buku_id, buku)
        if buku_updated is None:
            raise HTTPException(status_code=404, detail="Buku tidak ditemukan")
        logger.info(f"Buku dengan ID {buku_id} berhasil diperbarui.")
        return buku_updated
    except Exception as e:
        logger.error(f"Terjadi kesalahan: {e}")
        raise HTTPException(status_code=500, detail="Terjadi kesalahan pada server")

@app.delete("/buku/{buku_id}", response_model=dict)
async def delete_buku(buku_id: int):
    try:
        result = crud.delete_buku(buku_id)
        if not result:
            raise HTTPException(status_code=404, detail="Buku tidak ditemukan")
        logger.info(f"Buku dengan ID {buku_id} berhasil dihapus dari basis data.")
        return {"message": "Buku berhasil dihapus"}
    except Exception as e:
        logger.error(f"Terjadi kesalahan: {e}")
        raise HTTPException(status_code=500, detail="Terjadi kesalahan pada server")