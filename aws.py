import logging

import boto3
from botocore.exceptions import ClientError
from properties_reader import config

class AWSS3:
    __session = boto3.session.Session(
        region_name= config['AWS']['region_name'],
        aws_access_key_id = config['AWS']['access_key'],
        aws_secret_access_key=config['AWS']['secret_key']
    )

    __s3_client = __session.client('s3')

    __bucket = "seade"

    def upload_object(self, folder, file_name):
        try:
            response = self.__s3_client.upload_file(folder + file_name, self.__bucket, file_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

folder = "C:\\Users\\antto\\projects\\pucrio\\Ciência de Dados & Analytics\\pucrio_datascience_sprint3\\"
file_name = "casos_obitos_raca_cor.csv"

aws_s3 = AWSS3()
aws_s3.upload_object(folder, file_name)
