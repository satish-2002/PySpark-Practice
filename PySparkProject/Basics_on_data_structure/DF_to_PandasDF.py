import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder.appName("DF_to_PandasDF example").getOrCreate()

#Initilaizing Customer data
Customer_Data = [
    ("Satish", "", "Kollipaka", "8919903684", "Kakinada", 60000),
    ("Ayyappa", "Maruthi", "Alapati", "7899891234", "Guntur", 120000),
    ("Surya", "Prakash", "Kollipaka", "9391231991", "Kakinada", 20000),
    ("Siva", "Sai", "Nekkala", "9934564212", "Pithapuram", 39000)
]

#Initializing Column names
Column_names = ["First name", "Middle name", "Last name", "Phone", "Address", "Salary"]

#Creating Dataframe
Customer_df = spark.createDataFrame(Customer_Data, Column_names)
#Customer_df.show()                                        #Normal Show Statement
Customer_df.show(truncate=False)                           #Show statement with entire column data
#Customer_df.show(2, truncate=False)                       #Show statement with 2 rows and entire column data
#Customer_df.show(3, truncate=False, vertical=True)        #Show statement with 2 rows and entire column data in vertical way

#Converting Pyspark Dataframe into Pandas Dataframe
pandasdf = Customer_df.toPandas()
print(pandasdf)

#Data for Nested Dataframe
Nested_Customer_Data = [
    (("Satish", "", "Kollipaka"), "8919903684", "Kakinada", 60000),
    (("Ayyappa", "Maruthi", "Alapati"), "7899891234", "Guntur", 120000),
    (("Surya", "Prakash", "Kollipaka"), "9391231991", "Kakinada", 20000),
    (("Siva", "Sai", "Nekkala"), "9934564212", "Pithapuram", 39000)
]

# Initializing schema for Nested Dimensional Dataframe
Customer_details = StructType([
    StructField('Name', StructType([
        StructField('Middle name', StringType(),True),
        StructField('Middle name', StringType(),True),
        StructField('Last name', StringType(),True)
    ])),
    StructField('Phone', StringType(),True),
    StructField('Address', StringType(),True),
    StructField('Salary', IntegerType(),True)
])

#Creating Nested Dataframe
Customer_df2 = spark.createDataFrame(Nested_Customer_Data, Customer_details)
Customer_df2.show(3,truncate=False)

#Converting Pyspark Nested Dataframe into Pandas Dataframe
pandasdf2 = Customer_df2.toPandas()
print(pandasdf2)