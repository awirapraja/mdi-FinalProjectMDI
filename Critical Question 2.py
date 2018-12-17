import pyodbc, time
import matplotlib.pyplot as plt


conn = pyodbc.connect('Driver={SQL Server};Server=MY-PC;Database=MiningShareITS;Trusted_Connection=yes;')

#jumlah total akses selama 2018
def ak2018(conn):
	cursor = conn.cursor()
	hasil2 = cursor.execute("select count (lastaccessdatetime) as lastaccess  from MatakuliahITSNamaMahasiswaAksesMKTerakhir where Lastaccess like '%2018%'")
	while 1:
		hasil2 = cursor.fetchone()
		if not hasil2:
			break
		return hasil2.lastaccess

#jumlah total akses selama 2017
def ak2017(conn):
	cursor = conn.cursor()
	hasil2 = cursor.execute("select count (lastaccessdatetime) as lastaccess  from MatakuliahITSNamaMahasiswaAksesMKTerakhir  where Lastaccess like '%2017%'")
	while 1:
		hasil2 = cursor.fetchone()
		if not hasil2:
			break
		return hasil2.lastaccess

#jumlah total akses selama 2016
def ak2016(conn):
	cursor = conn.cursor()
	hasil2 = cursor.execute("select count (lastaccessdatetime) as lastaccess  from MatakuliahITSNamaMahasiswaAksesMKTerakhir  where Lastaccess like '%2016%'")
	while 1:
		hasil2 = cursor.fetchone()
		if not hasil2:
			break
		return hasil2.lastaccess

#jumlah total akses selama 2015
def ak2015(conn):
	cursor = conn.cursor()
	hasil2 = cursor.execute("select count (lastaccessdatetime) as lastaccess  from MatakuliahITSNamaMahasiswaAksesMKTerakhir  where Lastaccess like '%2015%'")
	while 1:
		hasil2 = cursor.fetchone()
		if not hasil2:
			break
		return hasil2.lastaccess

#jumlah total akses selama 2014
def ak2014(conn):
	cursor = conn.cursor()
	hasil2 = cursor.execute("select count (lastaccessdatetime) as lastaccess  from MatakuliahITSNamaMahasiswaAksesMKTerakhir  where Lastaccess like '%2014%'")
	while 1:
		hasil2 = cursor.fetchone()
		if not hasil2:
			break
		return hasil2.lastaccess

#jumlah total akses selama 2013
def ak2013(conn):
	cursor = conn.cursor()
	hasil2 = cursor.execute("select count (lastaccessdatetime) as lastaccess  from MatakuliahITSNamaMahasiswaAksesMKTerakhir  where Lastaccess like '%2013%'")
	while 1:
		hasil2 = cursor.fetchone()
		if not hasil2:
			break
		return hasil2.lastaccess


def show():
    # Figure 1
    plt.figure(1)
    tahun = ['2013', '2014', '2015', '2016', '2017', '2018']

    jak2013 = ak2013(conn)
    jak2014 = ak2014(conn)
    jak2015 = ak2015(conn)
    jak2016 = ak2016(conn)
    jak2017 = ak2017(conn)
    jak2018 = ak2018(conn)

    jumlah_akses = [jak2013,jak2014,jak2015,jak2016,jak2017,jak2018]


    print("2013 = " + str(jak2013))
    print("2014 = " + str(jak2014))
    print("2015 = " + str(jak2015))
    print("2016 = " + str(jak2016))
    print("2017 = " + str(jak2017))
    print("2018 = " + str(jak2018))

    plt.bar(tahun,jumlah_akses, color = ['orange'])
    plt.xlabel('Jumlah Akses', fontsize=12)
    plt.ylabel('Tahun', fontsize=12)
    plt.title("Jumlah Akses seluruh mahasiswa yang mengakses share.its.ac.id tahun 2013-2018")
    plt.show()

show()
