import database, schemas

def get_buku():
    conn = database.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM buku")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def get_buku_by_id(buku_id: int):
    conn = database.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM buku WHERE id = %s", (buku_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def create_buku(buku: schemas.BukuCreate):
    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO buku (judul, penulis, penerbit, tahun_terbit, konten, iktisar)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (buku.judul, buku.penulis, buku.penerbit, buku.tahun_terbit, buku.konten, buku.iktisar))
    conn.commit()
    cursor.execute("SELECT LAST_INSERT_ID()")
    buku_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    return schemas.Buku(id=buku_id, **buku.dict())

def update_buku(buku_id: int, buku: schemas.BukuUpdate):
    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE buku
        SET judul = %s, penulis = %s, penerbit = %s, tahun_terbit = %s, konten = %s, iktisar = %s
        WHERE id = %s
    """, (buku.judul, buku.penulis, buku.penerbit, buku.tahun_terbit, buku.konten, buku.iktisar, buku_id))
    conn.commit()
    
    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return None

    cursor.execute("SELECT * FROM buku WHERE id = %s", (buku_id,))
    updated_buku = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if updated_buku:
        return schemas.Buku(
            id=updated_buku[0],  # Pastikan ini adalah indeks yang benar
            judul=updated_buku[1],
            penulis=updated_buku[2],
            penerbit=updated_buku[3],
            tahun_terbit=updated_buku[4],
            konten=updated_buku[5],
            iktisar=updated_buku[6]
        )
    return None


def delete_buku(buku_id: int):
    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM buku WHERE id = %s", (buku_id,))
    affected_rows = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return affected_rows > 0
