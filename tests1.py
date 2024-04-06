# run this with the command
#  pytest pytest/testing.py

import pytest
import pyodbc


@pytest.fixture(scope="module")
def connect():
    # Establish connection to the SQL Server
    conn_str = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=EPLTVILW00B3\SQLEXPRESS;'
        r'DATABASE=AdventureWorks2012;'
        r'UID=HWUser;'
        r'PWD=HW!Login123;'
        r'Trusted_Connection=yes'
    )
    connection = pyodbc.connect(conn_str)
    yield connection
    connection.close()


# TEST TO CHECK IF COLUMN AddressLine1 CONTAINS EMPTY OR NULL VALUES
# Expected result:
# 0. AdventureWorks2012 DB with [AdventureWorks2012].[Person].[Address] table are present in MSSQL Server.
# 1. Query was completed successfully and the results were received.
# 2. The AddressLine1 column, which must have a NOT NULL constraint, does not have rows with empty or NULL values.
def test_null_values(connect):
    cursor = connect.cursor()
    cursor.execute("SELECT count(*) FROM AdventureWorks2012.Person.Address WHERE AddressLine1 IS NULL OR TRIM("
                   "AddressLine1) = ''")
    row_count = cursor.fetchone()[0]
    assert row_count == 0, "NULL or empty values are present in the AddressLine1 column"


# TEST TO CHECK IF ROW COUNTS IN THE TABLE EQUAL TO EXPECTED VALUE
# Expected result:
# 0. AdventureWorks2012 DB with [AdventureWorks2012].[Person].[Address] table are present in MSSQL Server.
# 1. Query was completed successfully and the results were received.
# 2. Row counts in the Address table is equal to the expected value.
def test_row_count(connect):
    cursor = connect.cursor()
    cursor.execute("SELECT COUNT(*) FROM [Person].[Address]")
    row_count = cursor.fetchone()[0]
    assert row_count == 19614, "Row count doesn't match expected value"


# TEST TO CHECK THAT TABLE [Production].[UnitMeasure] DOESN'T CONTAIN DUPLICATE RECORDS
# Expected result:
# 0. AdventureWorks2012 DB with [AdventureWorks2012].[Production].[UnitMeasure] table are present in MSSQL Server
# 1. Query was completed successfully and the results were received
# 2. Number of duplicate records in the UnitMeasure table is equal to '0'
def test_duplicates_check(connect):
    cursor = connect.cursor()
    cursor.execute("SELECT count(*) FROM (SELECT UPPER(TRIM([UnitMeasureCode])) AS CLEAN_UMC, COUNT(*) AS CNT FROM ["
                   "AdventureWorks2012].[Production].[UnitMeasure] GROUP BY UPPER(TRIM([UnitMeasureCode])) HAVING "
                   "COUNT(*) > 1) rez;")
    row_count = cursor.fetchone()[0]
    assert row_count == 0, "Table contains duplicates"


# TEST TO CHECK THAT [ModifiedDate] COLUMN DOESN'T CONTAIN VALUES GREATER THEN CURRENT DATE
# Expected result:
# 0. AdventureWorks2012 DB with [AdventureWorks2012].[Production].[UnitMeasure] table are present in MSSQL Server
# 1. Query was completed successfully and the results were received
# 2. Number of rows where ModifiedDate column have values greater than current date is equal to '0'
def test_date_less_now(connect):
    cursor = connect.cursor()
    cursor.execute("SELECT COUNT(*) FROM [AdventureWorks2012].[Production].[UnitMeasure] WHERE [ModifiedDate] > "
                   "CURRENT_TIMESTAMP;")
    row_count = cursor.fetchone()[0]
    assert row_count == 0, "Table contains ModifiedDate greater then current_date"


# TEST TO CHECK THAT [FolderFlag] COLUMN DOESN'T CONTAIN OTHER VALUES THAN 0 OR 1
# Expected result:
# 0. AdventureWorks2012 DB with [AdventureWorks2012].[Production].[Document] table are present in MSSQL Server
# 1. Query was completed successfully and the results were received
# 2. Number of rows where FolderFlag column have values other than 0 or 1 is equal to '0'
def test_values_in_set(connect):
    cursor = connect.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM [AdventureWorks2012].[Production].[Document] WHERE [FolderFlag] NOT IN (0, 1);")
    row_count = cursor.fetchone()[0]
    assert row_count == 0, "Table contains FolderFlag with incorrect values"


# TEST TO CHECK THAT THE [File Extension] COLUMN HAS VALUES BEGINNING WITH '.' FOLLOWED BY SMALL LETTERS
# Expected result:
# 0. AdventureWorks2012 DB with [AdventureWorks2012].[Production].[Document] table are present in MSSQL Server
# 1. Query was completed successfully and the results were received
# 2. Number of rows where File_Extension column has values with a different pattern is equal to '0'
def test_file_extension(connect):
    cursor = connect.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM [AdventureWorks2012].[Production].[Document] WHERE [FileExtension] NOT LIKE '.[a-z]%' "
        "AND [FileExtension] NOT LIKE '';")
    row_count = cursor.fetchone()[0]
    assert row_count == 0, "Table contains records with incorrect file extension"
