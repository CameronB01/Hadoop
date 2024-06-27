"""SimpleApp.py"""
from pyspark.sql import SparkSession

textFile = "/opt/spark/work-dir/austen.txt"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
textData = spark.read.text(textFile).cache() # cache for performance

numAs = textData.filter(textData.value.contains('a')).count()
numBs = textData.filter(textData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()
