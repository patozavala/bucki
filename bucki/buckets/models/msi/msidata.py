# Django
from django.db import models

# Utils
from bucki.utils.models import BuckiModel

class MSIData(BuckiModel):
    """
    MSIData class holds multispectral images data.

    """

    
    
# class MSIChannel(BuckiModel):
#     """
#     Each multispectral image is compound by several bands with information.
#     For each channel the EXIF tags are read and stores into variables
#     """

#     exif = models.FileField(
#         'exif tags',
#         upload_to='',
#     )

#     data_channel = models.FileField(
#         'data channel',
#         upload_to='/msi/channels/'
#     )

#     msi_data = models.ForeignKey(
#         ''
#     )
