import logging
import boto3
import os
import magic

from botocore.exceptions import ClientError
from boto3.s3.transfer import TransferConfig

# Set the desired multipart threshold value (5GB)
MB = 1024 ** 2
config = TransferConfig(multipart_threshold=10*MB, max_concurrency=4)
BUCKET_NAME = "tcc-unip-images"
s3_client = boto3.client('s3')
bucket_base_url = "https://tcc-unip-images.s3.sa-east-1.amazonaws.com/"
mime = magic.Magic(True)


def save_image(file_name, object_name):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)


    object_name += file_name[-4:len(file_name)]
    content_type = mime.from_file(file_name)

    # Upload the file
    try:
        s3_client.upload_file(file_name, BUCKET_NAME, object_name, ExtraArgs={'ContentType': content_type})
    except Exception as e:
        logging.error(e)
        return False
    image_url = bucket_base_url + object_name
    print(f'Image {image_url} uploaded successfully')
    return image_url


def get_image(file_name, object_name=None):

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        response = s3_client.upload_file(file_name, BUCKET_NAME, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
