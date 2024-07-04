# ETL-Pipeline

## Introduction

This code contains the steps to build an ETL pipeline that carries out the following tasks:

1. Extracts transactions from local database
2. Identifies and removes duplicates
3. Loads the transformed data to a s3 bucket

Extract, transform, and load (ETL) is the process of combining data from multiple sources into a large, central repository called a data warehouse. ETL uses a set of business rules to clean and organize raw data and prepare it for storage, data analytics, and machine learning (ML).

In the given example I've extracted data from local database, explored it and made some cleaning of data i.e. transformation and then loaded it to an AWS S3 bucket.

## Requirements

The minimum requirement is Python.



