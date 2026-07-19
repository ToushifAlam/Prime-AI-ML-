import mysql.connector

def dispmenu():
    print("\n\n\n\t\t# # # # # # LIBRARY MANAGEMENT # # # # # #")
    print("\n\t 1. BOOK MANAGEMENT")
    print("\n\t 2. MEMBER MANAGEMENT")
    print("\n\t 3. ISSUED BOOK")
    print("\n\t 4. RETURN BOOK")
    print("\n\t 5. EXIT")
    print("\t\t# # # # # # # # # # # # # # # # # # # # # #")

def bookmenu():
    print("\n\n\n\t\t# # # # # # BOOK MANAGEMENT # # # # # #")
    print("\n\t 1. ADD BOOK")
    print("\n\t 2. DELETE BOOK")
    print("\n\t 3. MODIFY BOOK")
    print("\n\t 4. DISPLAY BOOK")
    print("\n\t 5. EXIT")
    print("\t\t# # # # # # # # # # # # # # # # # # # # # #")

def membermenu():
    print("\n\t\t# # # # # # MEMBER MANAGEMENT # # # # # #")
    print("\n\t 1. ADD MEMBER")
    print("\n\t 2. MODIFY MEMBER")
    print("\n\t 3. DISPLAY MEMBER")
    print("\n\t 4. EXIT")
    print("\t\t# # # # # # # # # # # # # # # # # # # # # #")

def bookadd():
    con1 = mysql.connector.connect(host="localhost", user="root", password="national", database="world")
    cursor1 = con1.cursor()
    bno = int(input("Enter book number: "))
    bname = input("Enter book name: ")
    bauthor = input("Enter author name: ")
    bprice = float(input("Enter book price: "))
    bstat = 'N'
    cursor1.execute(
        "INSERT INTO book VALUES (%s,%s,%s,%s,%s)",
        (bno, bname, bauthor, bprice, bstat)
    )
    con1.commit()
    con1.close()
    cursor1.close()

def bookdelete():
    con1 = mysql.connector.connect(host="localhost", user="root", password="national", database="world")
    cursor1 = con1.cursor()
    bno = int(input("Enter book number to delete: "))
    cursor1.execute("DELETE FROM book WHERE bookno=%s", (bno,))
    con1.commit()
    con1.close()
    cursor1.close()

def bookmodify():
    con1 = mysql.connector.connect(host="localhost", user="root", password="national", database="world")
    cursor1 = con1.cursor()
    bno = int(input("Enter book number: "))
    bname = input("Enter book name: ")
    bauthor = input("Enter author name: ")
    bprice = float(input("Enter price: "))
    cursor1.execute(
        "UPDATE book SET bookname=%s, bookauthor=%s, bookprice=%s WHERE bookno=%s",
        (bname, bauthor, bprice, bno)
    )
    con1.commit()
    con1.close()
    cursor1.close()

def bookdisp():
    con1 = mysql.connector.connect(host="localhost", user="root", password="national", database="world")
    cursor1 = con1.cursor()
    cursor1.execute("SELECT * FROM book")
    for row in cursor1.fetchall():
        print(row)
    con1.close()

def memberadd():
    con1 = mysql.connector.connect(host="localhost", user="root", password="national", database="world")
    cursor1 = con1.cursor()
    mno = int(input("Enter member number: "))
    mname = input("Enter name: ")
    cursor1.execute(
        "INSERT INTO member1 VALUES (%s,%s,%s,%s)",
        (mno, mname, 0, 'N')
    )
    con1.commit()
    con1.close()
    cursor1.close()

def memberdelete():
    con1 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="national",
        database="world"
    )
    cursor1 = con1.cursor()

    mno = int(input("Enter member number to delete: "))
    cursor1.execute("DELETE FROM member1 WHERE memberno=%s", (mno,))
    con1.commit()

    cursor1.close()
    con1.close()

def membermodify():
    con1 = mysql.connector.connect(host="localhost", user="root", password="national", database="world")
    cursor1 = con1.cursor()
    mno = int(input("Enter member number: "))
    mname = input("Enter new name: ")
    cursor1.execute(
        "UPDATE member1 SET membername=%s WHERE memberno=%s",
        (mname, mno)
    )
    con1.commit()
    con1.close()
    cursor1.close()

def memberdisp():
    con1 = mysql.connector.connect(host="localhost", user="root", password="national", database="world")
    cursor1 = con1.cursor()
    cursor1.execute("SELECT * FROM member1")
    for row in cursor1.fetchall():
        print(row)
    con1.close()

def issuebook():
    con1 = mysql.connector.connect(host="localhost", user="root", password="national", database="world")
    cursor1 = con1.cursor()
    mno = int(input("Enter member number: "))
    bno = int(input("Enter book number: "))
    cursor1.execute("SELECT * FROM member1 WHERE memberno=%s", (mno,))
    mrec = cursor1.fetchone()
    if mrec and mrec[3] == 'N':
        cursor1.execute("SELECT * FROM book WHERE bookno=%s", (bno,))
        brec = cursor1.fetchone()
        if brec and brec[4] == 'N':
            cursor1.execute(
                "UPDATE member1 SET bookno=%s, status='Y' WHERE memberno=%s",
                (bno, mno)
            )
            cursor1.execute(
                "UPDATE book SET status='Y' WHERE bookno=%s",
                (bno,)
            )
            con1.commit()
    con1.close()

def returnbook():
    con1 = mysql.connector.connect(host="localhost", user="root", password="national", database="world")
    cursor1 = con1.cursor()
    mno = int(input("Enter member number: "))
    cursor1.execute("SELECT * FROM member1 WHERE memberno=%s", (mno,))
    mrec = cursor1.fetchone()
    if mrec and mrec[3] == 'Y':
        bno = mrec[2]
        cursor1.execute(
            "UPDATE member1 SET bookno=0, status='N' WHERE memberno=%s",
            (mno,)
        )
        cursor1.execute(
            "UPDATE book SET status='N' WHERE bookno=%s",
            (bno,)
        )
        con1.commit()
    con1.close()

choice = 0
while choice != 5:
    dispmenu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        ch = 0
        while ch != 5:
            bookmenu()
            ch = int(input("Enter choice: "))
            if ch == 1:
                bookadd()
            elif ch == 2:
                bookdelete()
            elif ch == 3:
                bookmodify()
            elif ch == 4:
                bookdisp()
            elif ch == 5:
                break
            else:
                print("\n\t\t\t ==INVALID CHOICE==")

    elif choice == 2:
        ch = 0
        while ch != 5:
            membermenu()
            ch = int(input("Enter choice: "))
            if ch == 1:
                memberadd()
            elif ch == 2:
                memberdelete()
            elif ch == 3:
                membermodify()
            elif ch == 4:
                memberdisp()
            elif ch == 5:
                break
            else:
                print("\n\t\t\t ==INVALID CHOICE==")

    elif choice == 3:
        issuebook()

    elif choice == 4:
        returnbook()

    elif choice == 5:
        break
    else:
        print("\n\t\t\t ==INVALID CHOICE==")