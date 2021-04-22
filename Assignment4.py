import mysql.connector
from faker import Faker
import csv

db = mysql.connector.connect(
        host='34.94.182.22',
        user='pascualmead@chapman.edu',
        passwd='FooBar!@#$',
        database='pascualmead_db',
    )

# User input for name of the file
def getFile():
    fileName = input("Enter the file name: ")
    fileName = "./" + fileName + ".csv"
    return fileName


# Generating data
def genData(fileName, rows):
    fake = Faker()
    csv_file = open(fileName, "w")
    writer = csv.writer(csv_file)
    writer.writerow(['FirstName', 'LastName', 'Street', 'City', 'State', 'Zip', 'Salesman_First', 'Salesman_Last',
                     'Order_Date'])
    for x in range(0, rows):
        writer.writerow([fake.first_name(), fake.last_name(), fake.street_address(), fake.city(), fake.state(), fake.zipcode(),
                         fake.first_name(), fake.last_name(), fake.date()])


# Importing the data
def importData(fileName):
    mycursor = db.cursor()

    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        print("Importing data.")
        for row in reader:
            print(".............")
            # Inserting data into 'Salesman' table
            mycursor.execute("INSERT INTO Salesman(Salesman_First, Salesman_Last)"
                             "VALUES (%s,%s);", (row['Salesman_First'], row['Salesman_Last']))
            db.commit()
            salesman_Id = mycursor.lastrowid

            # Inserting data into 'Customer' table
            mycursor.execute("INSERT INTO Customer(FirstName, LastName)"
                             "VALUES (%s,%s);", (row['FirstName'], row['LastName']))
            db.commit()
            customer_Id = mycursor.lastrowid

            # Inserting data into 'CustomerAddress' table
            mycursor.execute("INSERT INTO CustomerAddress(CustomerId, Street,City,Zip)"
                             "VALUES (%s, %s, %s, %s);", (customer_Id, row['Street'], row['City'], row['Zip']))
            db.commit()

            # Inserting data into 'CustomerSalesman' table
            mycursor.execute("INSERT INTO CustomerSalesman(CustomerId, SalesmanId)"
                             "VALUES (%s, %s);", (customer_Id, salesman_Id))
            db.commit()

            # Inserting data into 'Orders' table
            mycursor.execute("INSERT INTO Orders(CustomerId, Order_Date)"
                             "VALUES (%s, %s);", (customer_Id, row['Order_Date']))
            db.commit()

        print("Data imported successfully. Exiting Program.")



# Prompting user for input
choice = int(input("Would you like to generate data or import an existing data file? "
                   "(1)Generate Data (2)Import Data (3)Exit: "))

# Generate and import data
if choice == 1:
    file = getFile()
    rows = int(input("Enter the number of rows you would like to generate: "))
    genData(file, rows)
    import_data = int(input("Would you like to import this data? (1)Yes (2)No: "))
    if import_data == 1:
        importData(file)
    else:
        print("Exiting Program.")
# Imports existing data
elif choice == 2:
    file = getFile()
    importData(file)
else:
    print("Exiting Program.")



