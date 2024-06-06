# Hadoop

1. Make a working directory, 

```
mkdir running-hadoop
cd running-hadoop
```

2. Clone the big-data-europe fork for commodity hardware

```
git clone https://github.com/wxw-matt/docker-hadoop.git
cd docker-hadoop
```

4. Change version - we need to use docker-compose-v2, but the docker-compose command will look for an unversioned file.

```
mv docker-compose.yml docker-compose-v1.yml
mv docker-compose-v3.yml docker-compose.yml
```


5. Bring the Hadoop containers up.

```
docker-compose up -d
```

6. Used namenode.

```
docker exec -it docker-hadoop-namenode-1 /bin/bash
```


7. Set up the node

```
mkdir app
mkdir app/data
mkdir app/res
mkdir app/jars
```

8. Fetch data to app/data

```
cd /app/data
curl https://www.gutenberg.org/cache/epub/1342/pg1342.txt -o austen.txt
curl https://www.gutenberg.org/cache/epub/84/pg84.txt -o shelley.txt
curl https://www.gutenberg.org/cache/epub/768/pg768.txt -o bronte.txt
```

9. Fetch compute to app/jars

```
cd /app/jars
curl https://github.com/wxw-matt/docker-hadoop/blob/master/jobs/jars/WordCount.jar -o WordCounter.jar
```

10. Load data in HDFS

```
cd /
hdfs dfs -mkdir /test-1-input
hdfs dfs -copyFromLocal -f /app/data/*.txt /test-1-input/
```

11. Run Hadoop/MapReduce

```
hadoop jar jars/WordCount.jar WordCount /test-1-input /test-1-output
```

12. Copy results out of hdfs

```
hdfs dfs -copyToLocal /test-1-output /app/res/
```

```
cat /app/res/test-1-output/part-r-00000
```
