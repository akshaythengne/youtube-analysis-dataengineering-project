import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog2
AWSGlueDataCatalog2_node1707305773142 = glueContext.create_dynamic_frame.from_catalog(
    database="youtube-project-db-cleaned",
    table_name="raw_statistics",
    transformation_ctx="AWSGlueDataCatalog2_node1707305773142",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1707305709758 = glueContext.create_dynamic_frame.from_catalog(
    database="youtube-project-db-cleaned",
    table_name="cleaned_statistics_reference_data",
    transformation_ctx="AWSGlueDataCatalog_node1707305709758",
)

# Script generated for node Join
Join_node1707305790319 = Join.apply(
    frame1=AWSGlueDataCatalog2_node1707305773142,
    frame2=AWSGlueDataCatalog_node1707305709758,
    keys1=["category_id"],
    keys2=["id"],
    transformation_ctx="Join_node1707305790319",
)

# Script generated for node Amazon S3
AmazonS3_node1707306084936 = glueContext.getSink(
    path="s3://youtube-project-buck-cleansed-analytical",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["region"],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1707306084936",
)
AmazonS3_node1707306084936.setCatalogInfo(
    catalogDatabase="youtube-project-db-cleaned",
    catalogTableName="final_table_analytics",
)
AmazonS3_node1707306084936.setFormat("glueparquet", compression="snappy")
AmazonS3_node1707306084936.writeFrame(Join_node1707305790319)
job.commit()
