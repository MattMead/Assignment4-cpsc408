CREATE TABLE Customer(
    CustomerId INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL
);

CREATE TABLE CustomerAddress(
    AddressId INT PRIMARY KEY AUTO_INCREMENT,
    CustomerId INT,
    Street VARCHAR(50),
    City VARCHAR(50),
    Zip VARCHAR(50),
    FOREIGN KEY CustomerAddress(CustomerId) REFERENCES Customer(CustomerId)
);

CREATE TABLE Salesman(
    SalesmanId INT PRIMARY KEY AUTO_INCREMENT,
    Salesman_First VARCHAR(50),
    Salesman_Last VARCHAR(50)
);

CREATE TABLE CustomerSalesman(
    CustomerSalesmanId INT PRIMARY KEY AUTO_INCREMENT,
    CustomerId INT,
    SalesmanId INT,
    FOREIGN KEY (CustomerId) REFERENCES Customer(CustomerId),
    FOREIGN KEY (SalesmanId) REFERENCES Salesman(SalesmanId)
);


CREATE TABLE Orders(
    OrderId INT PRIMARY KEY AUTO_INCREMENT,
    CustomerId INT,
    Order_Date DATE,
    FOREIGN KEY Orders(CustomerId) REFERENCES Customer(CustomerId)
);

DROP TABLE Orders;
DROP TABLE CustomerAddress;
DROP TABLE CustomerSalesman;
DROP TABLE Salesman;
DROP TABLE Customer;



