# libraries to load the environment variables
import os
from dotenv import load_dotenv

load_dotenv()

from src.extract import extract_transactional_data
from src.transform import identify_and_remove_duplicates
from src.load_data_to_s3 import load_df_to_s3

aws_access_key = os.getenv("aws_access_key")
aws_secret_access_key= os.getenv("aws_secret_access_key")
aws_s3_bucket = os.getenv("aws_s3_bucket")

#extract data from tables
ot_transformed = extract_transactional_data()


# remove the duplicates
print("\nIdentifying and removing duplicates")
ot_wout_duplicates = identify_and_remove_duplicates(ot_transformed)

# load to S3
key = "etl/al_online_trans_final.csv"
load_df_to_s3(ot_wout_duplicates, key,aws_s3_bucket, aws_access_key, aws_secret_access_key)







