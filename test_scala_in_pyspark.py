from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark import sql
from pyspark.sql import SparkSession
from pyspark.sql.column import Column, _to_java_column, _to_seq
import pyspark.sql.functions as f

sc = SparkContext()
sqlContext = sql.SQLContext(sc)

def sum_to_five(col):
    _sum_five = sc._jvm.com.example.scalaudf.SumValue.getFun()
    return Column(_sum_five.apply(_to_seq(sc, [col], _to_java_column)))

expected = sc.parallelize([
    {"id": 1, "value": 10, "Country": "Poland"},
    {"id": 2, "value": 25, "Country": "Iran"},
    {"id": 3, "value": 30, "Country": "United States"},
    {"id": 4, "value": 45, "Country": "France"},
]).toDF()

final = expected.withColumn('Summed', sum_to_five('value'))

final.show()

# +-------------+---+-----+
# |      Country| id|value|
# +-------------+---+-----+
# |       Poland|  1|   10|
# |         Iran|  2|   25|
# |United States|  3|   30|
# |       France|  4|   45|
# +-------------+---+-----+

# +-------------+---+-----+------+
# |      Country| id|value|Summed|
# +-------------+---+-----+------+
# |       Poland|  1|   10|    15|
# |         Iran|  2|   25|    30|
# |United States|  3|   30|    35|
# |       France|  4|   45|    50|
# +-------------+---+-----+------+