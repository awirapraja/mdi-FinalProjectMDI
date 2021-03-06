import pyodbc, time
import matplotlib.pyplot as plt

conn = pyodbc.connect('Driver={SQL Server};Server=MY-PC;Database=MiningShareITS;Trusted_Connection=yes;')

#dosen Fakultas Teknologi Kelautan (FTK)
def dftk(conn):
	cursor = conn.cursor()
	hasil2 = cursor.execute("select count( distinct dosen) as Dosen from Dataset2 where fakultas = 'Fakultas Teknologi Kelautan (FTK)'and lasaccess like '%2018%'")
	while 1:
		hasil2 = cursor.fetchone()
		if not hasil2:
			break
		return hasil2.Dosen


# dosen Fakultas Ilmu Alam (FIA)
def dfia(conn):
	cursor = conn.cursor()
	hasil2 = cursor.execute("select count( distinct dosen) as Dosen from Dataset2 where fakultas = 'Fakultas Ilmu Alam (FIA)'and lasaccess like '%2018%'")
	while 1:
		hasil2 = cursor.fetchone()
		if not hasil2:
			break
		return hasil2.Dosen

# dosen Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)
def dftslk(conn):
	cursor = conn.cursor()
	hasil2 = cursor.execute("select count( distinct dosen) as Dosen from Dataset2 where fakultas = 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)'and lasaccess like '%2018%'")
	while 1:
		hasil2 = cursor.fetchone()
		if not hasil2:
			break
		return hasil2.Dosen

# dosen Fakultas Teknologi Industri (FTI)
def dfti(conn):
	cursor = conn.cursor()
	hasil2 = cursor.execute("select count( distinct dosen) as Dosen from Dataset2 where fakultas = 'Fakultas Teknologi Industri (FTI)'and lasaccess like '%2018%'")
	while 1:
		hasil2 = cursor.fetchone()
		if not hasil2:
			break
		return hasil2.Dosen

# dosen Fakultas Teknologi Informasi dan Komunikasi (FTIK)
def dftik(conn):
	cursor = conn.cursor()
	hasil2 = cursor.execute("select count( distinct dosen) as Dosen from Dataset2 where fakultas = 'Fakultas Teknologi Informasi dan Komunikasi (FTIK)'and lasaccess like '%2018%'")
	while 1:
		hasil2 = cursor.fetchone()
		if not hasil2:
			break
		return hasil2.Dosen

# dosen Program Pasca Sarjana (PPS)
def dpps(conn):
	cursor = conn.cursor()
	hasil2 = cursor.execute("select count( distinct dosen) as Dosen from Dataset2 where fakultas = 'Program Pasca Sarjana (PPS)'and lasaccess like '%2018%'")
	while 1:
		hasil2 = cursor.fetchone()
		if not hasil2:
			break
		return hasil2.Dosen

# dosen Sistem Pembelajaran Daring (SPADA) Indonesia
def dspada(conn):
	cursor = conn.cursor()
	hasil2 = cursor.execute("select count( distinct dosen) as Dosen from Dataset2 where fakultas = 'Sistem Pembelajaran Daring (SPADA) Indonesia'and lasaccess like '%2018%'")
	while 1:
		hasil2 = cursor.fetchone()
		if not hasil2:
			break
		return hasil2.Dosen

# dosen UPMB
def dupmb(conn):
	cursor = conn.cursor()
	hasil2 = cursor.execute("select count( distinct dosen) as Dosen from Dataset2 where fakultas = 'UPMB'and lasaccess like '%2018%'")
	while 1:
		hasil2 = cursor.fetchone()
		if not hasil2:
			break
		return hasil2.Dosen

def dupt(conn):
	cursor = conn.cursor()
	hasil2 = cursor.execute("select count( distinct dosen) as Dosen from Dataset2 where fakultas = 'UPT Penyelenggara Mata Kuliah Sosial Humaniora'and lasaccess like '%2018%'")
	while 1:
		hasil2 = cursor.fetchone()
		if not hasil2:
			break
		return hasil2.Dosen

def show():
    # Figure 1
	plt.figure(1)
	fakultas = ['FTK', 'FIA', 'FTSLK', 'FTI', 'FTIK', 'Pasca', 'SPADA', 'UPMB', 'UPT']

	hasildftk = dftk(conn)
	hasildfia = dfia(conn)
	hasildftslk = dftslk(conn)
	hasilfti = dfti(conn)
	hasilftik = dftik(conn)
	hasilpps = dpps(conn)
	hasilspada = dspada(conn)
	hasilupmb = dupmb(conn)
	hasilupt = dupt(conn)


	jumlahdosen = [hasildftk, hasildfia, hasildftslk, hasilfti, hasilftik, hasilpps, hasilspada, hasilupmb, hasilupt]


	print("FTK = " + str(hasildftk))
	print("FIA = " + str(hasildfia))
	print("FTSLK = " + str(hasildftslk))
	print("FTI = " + str(hasilfti))
	print("FTIK = " + str(hasilftik))
	print("PPS = " + str(hasilpps))
	print("SPADA = " + str(hasilspada))
	print("UPMB = " + str(hasilupmb))
	print("UPT = " + str(hasilupt))

	plt.bar(fakultas, jumlahdosen, color = ['red'])
	plt.xlabel('Fakultas', fontsize=12)
	plt.ylabel('Jumlah Dosen', fontsize=12)
	plt.title("Jumlah Dosen Seluruh Fakultas yang mengakses share.its.ac.id tahun 2018")
	plt.show()

show()