 ##########
 spark-submit --driver-java-options='-Dspark.yarn.app.container.log.dir=/mnt/var/log/hadoop' s3://chorus-analytics-npe-codebase/functions/churn-spark-etl_v3_dev.py Weekly
 
 ##########
 spark-submit --driver-java-options='-Dspark.yarn.app.container.log.dir=/mnt/var/log/hadoop'  --jars /home/hadoop/postgresql-9.4-1201-jdbc41.jar s3://chorus-analytics-codebase/functions/churn_redshift_load.py

 spark-submit --driver-java-options='-Dspark.yarn.app.container.log.dir=/mnt/var/log/hadoop'  --jars /home/hadoop/postgresql-9.4-1201-jdbc41.jar s3://chorus-analytics-codebase/functions/churn_redshift_load.py
 
 ##########
 sudo yum -y downgrade aws-cli python27-botocore

##########
%pyspark 
s3 = boto3.resource('s3')
bucket = s3.Bucket('mybucket')
bucket.objects.filter(Prefix="myprefix/").delete()

########## Moving last column from DF to first column -- Rearranging columns
%pyspark
    cols = list(df_rs.columns)
    cols = [cols[-1]] + cols[:-1]
    df_rs = df_rs[cols]

########## Types of Datatype in PySpark. Conversion of Datatype
%pyspark
import pyspark.sql.types
"DataType",			"NullType",
"StringType",		"BinaryType", 
"BooleanType", 		"DateType",
"TimestampType",	"DecimalType", 
"DoubleType", 		"FloatType", 
"ByteType", 		"IntegerType",
"LongType", 		"ShortType", 
"ArrayType", 		"MapType", 
"StructField", 		"StructType"

df = df.withColumn("col_name", df_rs["col_name"].cast(IntegerType()))


##########
%pyspark
s3 = boto3.resource('s3')
bucket_s3 = s3.Bucket('')
period_date=['2019-10-31', '2019-11-30', '2019-12-31', '2020-01-31']
for x in period_date:
    bucket_s3.objects.filter(Prefix = 'churn/rsp_movements_weekly/period_end_date='+x).delete()

##########	
%pyspark
def iterate_bucket_items(bucket, prefix):
    paginator = client.get_paginator('list_objects_v2')
    operation_parameters = {'Bucket': bucket,
                            'Prefix': prefix}
    page_iterator = paginator.paginate(**operation_parameters)

    for page in page_iterator:
        for item in page['Contents']:
            yield item
			

##########
Redshift load -- emr role should have secrets manager role added

#########Copy from Prod to Non Prod S3
aws s3 sync --profile chorus_pro s3://chorus-analytics-transformed/cdw/cdw_wp/product_inventory_wps_f/ s3://chorus-analytics-npe-transformed/cdw/cdw_wp/product_inventory_wps_f/ --acl bucket-owner-full-control


##########Zeppelin Interpreter to take Redshift jars
%dep 
z.load("/home/hadoop/spark-redshift_2.10-2.0.0.jar")
z.load("/usr/share/aws/redshift/jdbc/RedshiftJDBC41.jar")
z.load("/home/hadoop/minimal-json-0.9.4.jar")
z.load("/home/hadoop/spark-avro_2.11-4.0.0.jar")
z.load("/home/hadoop/postgresql-9.4-1201-jdbc41.jar")

################
jdbc:redshift://rs-network-stats.c37itvrnlwlz.ap-southeast-2.redshift.amazonaws.com:5439/cdwrs?user=svc_churn_loader&password=dVdpxg88FheAzZQBGcej


################REDSHIFT
--select * from STL_ERROR order by recordtime desc limit 10

#######
--driver-class-path /homepostgresql-9.4.1207.jar --jars postgresql-9.4.1207.jar

jdbc:redshift://rs-network-stats.c37itvrnlwlz.ap-southeast-2.redshift.amazonaws.com:5439/cdwrs?user=svc_churn_loader&password=dVdpxg88FheAzZQBGcej

arn:aws:iam::562132058527:role/IAMRoleForRedshiftPPE

 pyspark --driver-class-path postgresql-9.4-1201-jdbc41.jar --jars postgresql-9.4-1201-jdbc41.jar
 
 ##############
  com.amazon.redshift.jdbc42.Driver
  spark.read.format("jdbc")\  
  .option("driver", "com.amazon.redshift.jdbc42.Driver")\  
  .option("url", REDSHIFT_JDBC_URL)\  
  .option("dbtable", QUERY)\  
  .option("user", REDSHIFT_USERNAME)\  
  .option("password", REDSHIFT_PASSWORD)\  
  .load()
