import sqlite3

conn = sqlite3.connect('filetype.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_types(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT, \
        col_filetype TEXT  \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('filetype.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_types(col_filename, col_filetype) VALUES(?,?)", \
                 ('information','.docx '))
    cur.execute("INSERT INTO tbl_types(col_filename, col_filetype) VALUES(?,?)", \
                 ('World','.txt'))
    cur.execute("INSERT INTO tbl_types(col_filename, col_filetype) VALUES(?,?)", \
                 ('myImage','.png'))
    cur.execute("INSERT INTO tbl_types(col_filename, col_filetype) VALUES(?,?)", \
                 ('myMovie','.mpg '))
    cur.execute("INSERT INTO tbl_types(col_filename, col_filetype) VALUES(?,?)", \
                 ('Hello','.txt'))
    cur.execute("INSERT INTO tbl_types(col_filename, col_filetype) VALUES(?,?)", \
                 ('data','.pdf'))
    cur.execute("INSERT INTO tbl_types(col_filename, col_filetype) VALUES(?,?)", \
                 ('myPhoto','.jpg '))
    conn.commit()
conn.close()

conn = sqlite3.connect('filetype.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_filename, col_filetype FROM tbl_types WHERE col_filetype = '.txt'")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "Returing files with the file type of: .txt\nFile: {}{}".format(item[0],item[1])
    print(msg)
