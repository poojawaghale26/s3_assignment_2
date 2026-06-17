import unittest
from unittest import result
import boto3

from moto import mock_aws
from s3_operation import S3Operations

@mock_aws
class TestS3Operations(unittest.TestCase):
    def setUp(self):
        self.bucket_name = "test-bucket"
        self.s3 = boto3.client('s3',region_name='us-east-1')
        self.s3.create_bucket(Bucket=self.bucket_name)
        self.operation = S3Operations(self.bucket_name)

        self.operation.add_s3_objects()

    # 1. Add 2500 Objects

    def test_add_s3_objects(self):
        paginator = self.s3.get_paginator("list_objects_v2")

        total = 0

        for page in paginator.paginate(Bucket=self.bucket_name):
            total += len(page.get("Contents", []))

        self.assertEqual(total, 2500)
        
    

    # 2. Fetch S3 Objects by Tag
    def test_fetch_s3_objects_by_tag(self):
        result = self.operation.fetch_s3_objects_by_tag(
        "type",
        "even"
    )

        self.assertEqual(len(result), 834)

    # 3. Fetch S3 Objects by Metadata

    def test_fetch_s3_objects_by_metadata(self):
        result = self.operation.fetch_s3_objects_by_metadata(
        "group",
        "natural"
    )

        self.assertEqual(len(result), 2500)

    # 4. Delete S3 Objects by Tag

    def test_delete_s3_objects_by_tags(self):
        deleted = self.operation.delete_s3_objects_by_tags(
        "type",
        "even"
        )

        remaining = len(self.operation.get_all_keys())

        self.assertEqual(deleted, 834)
        self.assertEqual(remaining, 1666)

    # 5. Delete S3 Objects by Metadata

    def test_delete_s3_objects_by_metadata(self):
        deleted = self.operation.delete_s3_objects_by_metadata(
        "group",
        "natural"
    )

        remaining = len(self.operation.get_all_keys())

        self.assertEqual(deleted, 2500)
        self.assertEqual(remaining, 0)

if __name__ == '__main__':    
    unittest.main(verbosity=2)

