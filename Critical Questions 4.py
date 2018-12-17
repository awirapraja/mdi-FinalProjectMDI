import pyodbc, time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import operator as o

conn = pyodbc.connect('Driver={SQL Server};Server=MY-PC;Database=MiningShareITS;Trusted_Connection=yes;')

#dosen pengguna email its.ac.id tahun 2016-2018
def de16(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct (email)) as email from Dataset2 "
                            "where email like '%its.ac.id%'and lasaccess like '%2016%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.email
def de17(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct (email)) as email from Dataset2 "
                            "where email like '%its.ac.id%'and lasaccess like '%2017%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.email
def de18(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct (email)) as email from Dataset2 "
                            "where email like '%its.ac.id%'and lasaccess like '%2018%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.email

#dosen pengguna email google.com tahun 2016-2018
def dg16(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct (email)) as email from Dataset2 "
                            "where email like '%google.com%'and lasaccess like '%2016%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.email
def dg17(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct (email)) as email from Dataset2 "
                            "where email like '%google.com%'and lasaccess like '%2017%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.email
def dg18(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct (email)) as email from Dataset2 "
                            "where email like '%google.com%'and lasaccess like '%2018%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.email

#dosen pengguna email yahoo.com tahun 2016-2018
def dy18(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct (email)) as email from Dataset2 "
                            "where email like '%yahoo.com%'and lasaccess like '%2018%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.email
def dy17(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct (email)) as email from Dataset2 "
                            "where email like '%yahoo.com%'and lasaccess like '%2017%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.email
def dy16(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct (email)) as email from Dataset2 "
                            "where email like '%yahoo.com%'and lasaccess like '%2016%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.email

#dosen pengguna email yahoo.co.id tahun 2016-2018
def dyi18(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct (email)) as email from Dataset2 "
                            "where email like '%yahoo.co.id%'and lasaccess like '%2018%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.email
def dyi17(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct (email)) as email from Dataset2 "
                            "where email like '%yahoo.co.id%'and lasaccess like '%2017%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.email
def dyi16(conn):
    cursor = conn.cursor()
    hasil2 = cursor.execute("select count (distinct (email)) as email from Dataset2 "
                            "where email like '%yahoo.co.id%'and lasaccess like '%2016%'")
    while 1:
        hasil = cursor.fetchone()
        if not hasil:
            break
        return hasil.email

def show():




# Figure 1

    print("its.ac.id 18 = " + str(de18(conn)))
    print("its.ac.id 17 = " + str(de17(conn)))
    print("its.ac.id 16 = " + str(de16(conn)))
    print("google.com 18 = " + str(dg18(conn)))
    print("google.com 17 = " + str(dg17(conn)))
    print("google.com 16 = " + str(dg16(conn)))
    print("yahoo.com 18 = " + str(dy18(conn)))
    print("yahoo.com 17 = " + str(dy17(conn)))
    print("yahoo.com 16 = " + str(dy16(conn)))
    print("yahoo.co.id 18 = " + str(dyi18(conn)))
    print("yahoo.co.id 17 = " + str(dyi17(conn)))
    print("yahoo.co.id 16 = " + str(dyi16(conn)))


hasildata = np.array ([[ 'Pengguna email its.ac.id ','2016', de18(conn)], ['Pengguna email its.ac.id ','2017', de17(conn)],['Pengguna email its.ac.id ','2018', de16(conn)],
                        [ 'Pengguna email google.com ','2016', dg16(conn)],[ 'Pengguna email google.com ','2017', dg17(conn)],['Pengguna email google.com ','2018', dg18(conn)],
                        [ 'Pengguna email yahoo.com ','2016', dy18(conn)],[ 'Pengguna email yahoo.com ','2017', dy17(conn)],['Pengguna email yahoo.com ','2018', dy16(conn)],
                       ['Pengguna email yahoo.co.id ', '2016', dyi18(conn)], ['Pengguna email yahoo.co.id ', '2017', dyi17(conn)], ['Pengguna email yahoo.co.id ', '2018', dyi16(conn)]
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
    ax.set_title('sebaran Email Dosen pengguna share.its.ac.id tahun 2016 - 2018')
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