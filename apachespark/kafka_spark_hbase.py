#import KafkaUtils and create an input DStream as follow

#import os
#os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars /Volumes/Data SSD/python/spark-streaming-kafka-0-10-assembly_2.11-2.1.1.jar pyspark-shell'
from pyspark import SparkContext
#from pyspark import Sparkconf
from pyspark.streaming import StreamingContext 
from pyspark.streaming.kafka import KafkaUtils

#Create Spark context
sc = SparkContext(appName="StreamingKafkaToFS") 
sc.setLogLevel("WARN")

#create the streaming context
#60 is teh batch duration
ssc = StreamingContext(sc,6)

#Connect to Kafka topic "LOGWARN"
kafkaStream = KafkaUtils.createStream(ssc, 'localhost:2181','spark-streaming', {'LOGWARN':1})
#works
kafkaStream .pprint()
#parsed= kafkaStream.map(lambda a: a.split(""))
#parsed= kafkaStream.map(lambda a: a.split("\n"))
#parsed.pprint() 
ssc.start()
ssc.awaitTermination()

############################
# HBASE/HDFS/HIVE
############################

val sparkConf = new SparkConf().setAppName("StreamHDFSdata")
sparkConf.set("spark.dynamicAllocation.enabled","false")
val ssc = new StreamingContext(sparkConf, Seconds(5))
ssc.checkpoint("/user/hdpuser/checkpoint")
val sc = ssc.sparkContext

val smDStream = ssc.textFileStream("/user/hdpuser/data")
val smSplitted = smDStream.map( x => x.split(";") ).map( x => Row.fromSeq( x ) )
...

lazy val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)

smSplitted.foreachRDD( rdd => {
// use sqlContext  here
} )