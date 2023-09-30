import logging

import boto3
from botocore.exceptions import ClientError


class AWSS3:
    __session = boto3.session.Session(
        region_name='us-east-1',
        aws_access_key_id="AKIAQYDW2EL7OR5PNC3N",
        aws_secret_access_key="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"
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
