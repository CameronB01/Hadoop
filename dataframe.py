#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# To run this example use
# ./bin/spark-submit examples/src/main/r/dataframe.R


from pyspark.sql import SparkSession


# Initialize SparkSession

spark = SparkSession.builder.appName("PySpark-DataFrame-example").getOrCreate()

# sparkR.session(appName = "SparkR-DataFrame-example")

# Create a simple local data.frame

local_data = [("John", 19), ("Smith", 23), ("Sarah", 18)]
localDF = spark.createDataFrame(local_data, ["name", "age"])

localDF.printSchema()

# root
#  |-- name: string (nullable = true)
#  |-- age: double (nullable = true)

# Create a DataFrame from a JSON file
path = "https://raw.githubusercontent.com/apache/spark/master/examples/src/main/resources/people.json"
peopleDF = spark.read.json(path)
peopleDF.printSchema()

# path <- file.path(Sys.getenv("SPARK_HOME"), "examples/src/main/resources/people.json")
# peopleDF <- read.json(path)
# printSchema(peopleDF)
# root
#  |-- age: long (nullable = true)
#  |-- name: string (nullable = true)

# Register this DataFrame as a table.
peopleDF.createOrReplaceTempView("people")

# createOrReplaceTempView(peopleDF, "people")

# SQL statements can be run by using the sql methods
teenagers = spark.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")

# teenagers <- sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")

# Call collect to get a local data.frame
teenagersLocalDF = teenagers.collect()

# teenagersLocalDF <- collect(teenagers)

# Print the teenagers in our dataset
for row in teenagersLocalDF:
    print(row)

# Stop the SparkSession now
spark.stop()

# Output
My terminal output was: Row(name='Justin')
