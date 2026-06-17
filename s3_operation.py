import boto3
import os

class S3Operations:

    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3')

    # Add 2500 objects
    def add_s3_objects(self, total_objects=2500):
        tags = ["type=even", "type=odd", "type=prime"]

        for i in range(1, total_objects + 1):
            key = f"number_{i}.txt"

            metadata = {
                "number": str(i),
                "group": "natural"
            }

            self.s3.put_object(
                Bucket=self.bucket_name,
                Key=key,
                Body=f"Natural Number : {i}",
                Metadata=metadata,
                Tagging=tags[(i - 1) % len(tags)]
            )

        print(f"{total_objects} objects uploaded.")

    # Get all keys
    def get_all_keys(self):
        keys = []

        paginator = self.s3.get_paginator('list_objects_v2')

        for page in paginator.paginate(Bucket=self.bucket_name):
            for obj in page.get('Contents', []):
                keys.append(obj['Key'])

        return keys

    # Fetch by tags
    def fetch_s3_objects_by_tag(
        self,
        tag_key,
        tag_value,
        output_file="output/filtered_by_tags.txt"
    ):
        matched_keys = []

        for key in self.get_all_keys():
            tags = self.s3.get_object_tagging(
                Bucket=self.bucket_name,
                Key=key
            )['TagSet']

            for tag in tags:
                if tag['Key'] == tag_key and tag['Value'] == tag_value:
                    matched_keys.append(key)

        os.makedirs("output", exist_ok=True)

        with open(output_file, "w") as file:
            file.write("\n".join(matched_keys))

        return matched_keys

    # Fetch by metadata
    def fetch_s3_objects_by_metadata(
        self,
        metadata_key,
        metadata_value,
        output_file="output/filtered_by_metadata.txt"
    ):
        matched_keys = []

        for key in self.get_all_keys():
            metadata = self.s3.head_object(
                Bucket=self.bucket_name,
                Key=key
            )['Metadata']

            if metadata.get(metadata_key) == metadata_value:
                matched_keys.append(key)

        os.makedirs("output", exist_ok=True)

        with open(output_file, "w") as file:
            file.write("\n".join(matched_keys))

        return matched_keys

    # Delete by tags
    def delete_s3_objects_by_tags(self, tag_key, tag_value):
        deleted_count = 0

        for key in self.get_all_keys():
            tags = self.s3.get_object_tagging(
                Bucket=self.bucket_name,
                Key=key
            )['TagSet']

            for tag in tags:
                if tag['Key'] == tag_key and tag['Value'] == tag_value:
                    self.s3.delete_object(
                        Bucket=self.bucket_name,
                        Key=key
                    )
                    deleted_count += 1
                    break

        return deleted_count

    # Delete by metadata
    def delete_s3_objects_by_metadata(self, metadata_key, metadata_value):
        deleted_count = 0

        for key in self.get_all_keys():
            metadata = self.s3.head_object(
                Bucket=self.bucket_name,
                Key=key
            )['Metadata']

            if metadata.get(metadata_key) == metadata_value:
                self.s3.delete_object(
                    Bucket=self.bucket_name,
                    Key=key
                )
                deleted_count += 1

        return deleted_count