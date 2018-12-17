import pyodbc, time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import operator as o

conn = pyodbc.connect('Driver={SQL Server};Server=MY-PC;Database=MiningShareITS;Trusted_Connection=yes;')

#dosen Fakultas Teknologi Kelautan (FTK)
def dftk18(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Fakultas Teknologi Kelautan (FTK)' and Lastaccess like '%2018%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen

def dftk17(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Fakultas Teknologi Kelautan (FTK)' and Lastaccess like '%2017%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen

def dftk16(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Fakultas Teknologi Kelautan (FTK)' and Lastaccess like '%2016%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen


# jumlah dosen Fakultas Teknologi Informasi dan Komunikasi (FTIK)
def dftik18(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Fakultas Teknologi Informasi dan Komunikasi (FTIK)' "
                            "and Lastaccess like '%2018%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen

def dftik17(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Fakultas Teknologi Informasi dan Komunikasi (FTIK)' "
                            "and Lastaccess like '%2017%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen

def dftik16(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Fakultas Teknologi Informasi dan Komunikasi (FTIK)' "
                            "and Lastaccess like '%2016%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen

# Program Pasca Sarjana (PPS)
def dpasca16(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Program Pasca Sarjana (PPS)' "
                            "and Lastaccess like '%2016%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen
def dpasca17(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Program Pasca Sarjana (PPS)' "
                            "and Lastaccess like '%2017%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen
def dpasca18(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Program Pasca Sarjana (PPS)' "
                            "and Lastaccess like '%2018%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen

#Fakultas Teknologi Industri (FTI)
def dfti18(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Fakultas Teknologi Industri (FTI)' "
                            "and Lastaccess like '%2018%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen
def dfti17(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Fakultas Teknologi Industri (FTI)' "
                            "and Lastaccess like '%2017%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen
def dfti16(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Fakultas Teknologi Industri (FTI)' "
                            "and Lastaccess like '%2016%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen

#Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)
def dftslk16(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)' "
                            "and Lastaccess like '%2016%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen
def dftslk17(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)' "
                            "and Lastaccess like '%2017%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen
def dftslk18(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)' "
                            "and Lastaccess like '%2018%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen

#Fakultas Ilmu Alam (FIA)
def dfia18(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Fakultas Ilmu Alam (FIA)' "
                            "and Lastaccess like '%2018%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen
def dfia17(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Fakultas Ilmu Alam (FIA)' "
                            "and Lastaccess like '%2017%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen
def dfia16(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Fakultas Ilmu Alam (FIA)' "
                            "and Lastaccess like '%2016%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen

#Sistem Pembelajaran Daring (SPADA) Indonesia
def dspd16(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Sistem Pembelajaran Daring (SPADA) Indonesia' "
                            "and Lastaccess like '%2016%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen

def dspd17(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Sistem Pembelajaran Daring (SPADA) Indonesia' "
                            "and Lastaccess like '%2017%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen

def dspd18(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'Sistem Pembelajaran Daring (SPADA) Indonesia' "
                            "and Lastaccess like '%2018%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen
#UPMB
def dup18(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'UPMB' "
                            "and Lastaccess like '%2018%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen
def dup17(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'UPMB' "
                            "and Lastaccess like '%2017%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen
def dup16(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'UPMB' "
                            "and Lastaccess like '%2016%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen

#UPT Penyelenggara Mata Kuliah Sosial Humaniora
def dupt16(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'UPT Penyelenggara Mata Kuliah Sosial Humaniora' "
                            "and Lastaccess like '%2016%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen
def dupt17(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'UPT Penyelenggara Mata Kuliah Sosial Humaniora' "
                            "and Lastaccess like '%2017%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen
def dupt18(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct Dosen) as jumlah_dosen "
                            "from MatakuliahITSNamaDosenAksesMKTerakhir "
                            "where fakultas = 'UPT Penyelenggara Mata Kuliah Sosial Humaniora' "
                            "and Lastaccess like '%2018%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.jumlah_dosen


def show():




# Figure 1

    print("FTK18 = " + str(dftk18(conn)))
    print("FTK17 = " + str(dftk17(conn)))
    print("FTK16 = " + str(dftk16(conn)))
    print("FTIK18 = " + str(dftik18(conn)))
    print("FTIK17 = " + str(dftik17(conn)))
    print("FTIK16 = " + str(dftik16(conn)))
    print("PASCA16 = " + str(dpasca16(conn)))
    print("PASCA17 = " + str(dpasca17(conn)))
    print("PASCA18 = " + str(dpasca18(conn)))
    print("FTI18 = " + str(dfti18(conn)))
    print("FTI17 = " + str(dfti17(conn)))
    print("FTI16 = " + str(dfti16(conn)))
    print("FTSLK18 = " + str(dftslk16(conn)))
    print("FTSLK17 = " + str(dftslk17(conn)))
    print("FTSLK16 = " + str(dftslk18(conn)))
    print("FIA16 = " + str(dfia16(conn)))
    print("FIA17 = " + str(dfia17(conn)))
    print("FIA18 = " + str(dfia18(conn)))
    print("SPADA18 = " + str(dspd18(conn)))
    print("SPADA17 = " + str(dspd17(conn)))
    print("SPADA16 = " + str(dspd16(conn)))
    print("UPMB18 = " + str(dup18(conn)))
    print("UPMB17 = " + str(dup17(conn)))
    print("UPMB16 = " + str(dup16(conn)))
    print("UPT18 = " + str(dupt18(conn)))
    print("UPT17 = " + str(dupt17(conn)))
    print("UPT16 = " + str(dupt16(conn)))

hasildata = np.array ([[ 'FTK','2016', dftk18(conn)], ['FTK','2017',dftk17(conn)],['FTK', '2018',dftk16(conn)],
                         ['FTIK','2016',dftik18(conn)], ['FTIK','2017',dftik17(conn)],['FTIK','2018',dftik16(conn)],
                       ['PASCA', '2018', dpasca18(conn)], ['PASCA','2017',dpasca17(conn)],['PASCA','2016',dpasca16(conn)],
                       ['FTI', '2016', dfti18(conn)], ['FTI', '2017', dfti17(conn)], ['FTI', '2018', dfti16(conn)],
                       ['FTSLK', '2016', dftslk16(conn)], ['FTSLK', '2017', dftslk17(conn)], ['FTSLK', '2018', dftslk18(conn)],
                        ['FIA', '2016', dfia18(conn)], ['FIA', '2017', dfia17(conn)], ['FIA', '2018', dfia16(conn)],
                        ['SPADA', '2016', dspd18(conn)], ['SPADA', '2017', dspd17(conn)], ['SPADA', '2018', dspd16(conn)],
                       ['UPMB', '2016', dup16(conn)], ['UPMB', '2017', dup17(conn)], ['UPMB', '2018', dup18(conn)],
                       ['UPT', '2016', dupt16(conn)], ['UPT', '2017', dupt17(conn)], ['UPT', '2018', dupt18(conn)],

                       ])


fig = plt.figure()
ax = fig.add_subplot(111)
def barplot(ax, hasildata):
    conditions = [(c, np.mean(hasildata[hasildata[:, 0] == c][:, 2].astype(float)))
                  for c in np.unique(hasildata[:, 0])]
    categories = [(c, np.mean(hasildata[hasildata[:, 1] == c][:, 2].astype(float)))
                  for c in np.unique(hasildata[:, 1])]

    conditions = [c[0] for c in sorted(conditions, key=o.itemgetter(1))]
    categories = [c[0] for c in sorted(categories, key=o.itemgetter(1))]

    space = 0.3
    n = len(conditions)
    width = (1 - space) / (len(conditions))

    # Create a set of bars at each position
    for i, cond in enumerate(conditions):
        indeces = range(1, len(categories) + 1)
        vals = hasildata[hasildata[:, 0] == cond][:, 2].astype(np.float)
        pos = [j - (1 - space) / 2. + i * width for j in indeces]
        ax.bar(pos, vals, width=width, label=cond,
               color=cm.Accent(float(i) / n))

    # Set the x-axis tick labels to be equal to the categories
    ax.set_title('Perbandingan Jumlah Dosen seluruh fakultas yang mengakses Share.its.ac.id tahun 2016 - 2018')
    ax.set_xticks(indeces)
    ax.set_xticklabels(categories)
    plt.setp(plt.xticks()[1], rotation=90)

    # Add the axis labels
    ax.set_ylabel("Jumlah Dosen")
    ax.set_xlabel("Tahun")

    # Add a legend
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1], loc='upper left')


barplot(ax, hasildata)
plt.show()

show()
conn.close()