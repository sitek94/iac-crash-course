"""A Python Pulumi program"""

import pulumi
import pulumi_aws as aws
import os
import mimetypes

config = pulumi.Config()
site_dir = config.require("site_dir")

bucket = aws.s3.Bucket('my-bucket',
  website={
    'index_document': 'index.html'
  })

filepath = os.path.join(site_dir, 'index.html')

mime_type, _ = mimetypes.guess_type(filepath)

obj = aws.s3.BucketObject('index.html',
  bucket=bucket.bucket,
  source=pulumi.FileAsset(filepath),
  acl='public-read',
  content_type=mime_type 
)

pulumi.export('bucket_name', bucket.bucket)
pulumi.export('bucket_endpoint', pulumi.Output.concat('http://', bucket.website_endpoint))
