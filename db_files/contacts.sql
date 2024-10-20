USE contact_db;

CREATE TABLE Contacts(
    id INT IDENTITY(1,1) PRIMARY KEY,
    FirstName NVARCHAR(200) NOT NULL,
    LastName NVARCHAR(200) NOT NULL,
    PhoneNo NVARCHAR(10) NOT NULL,
    CONSTRAINT chk_phone CHECK (PhoneNo not like '%[^0-9]%'),
    Email NVARCHAR(50) NOT NULL,
    Area NVARCHAR(50) NOT NULL,
    city NVARCHAR(30) NOT NULL,
    State NVARCHAR(30) NOT NULL,
    Pincode INT NOT NULL,
    username NVARCHAR(80) NOT NULL
);

SELECT * FROM Contacts;