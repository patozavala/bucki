"""
MSImage model.

A stacked tiff file with all bands is passed to the model.
https://stackoverflow.com/questions/47248065/creating-a-tiff-stack-from-individual-tiffs-in-python



# CHANGE
Regions are catched by using GeoDjango
https://docs.djangoproject.com/en/3.2/ref/contrib/gis/tutorial/#geographic-models


"""

# Django
from django.db import models
from django.db.models.deletion import CASCADE


# Utils
from bucki.utils.models import BuckiModel

class MSImage(BuckiModel):
    """
    MSImage class holds multispectral images.

    regions must be incorporated in the following way:

    {
        'label': '[v_1,...v_i,...,v_n]',
    }
    Where v_i is the i-th vertex of the box ground truth for objects in the image.

    exif_tags holds exif tags for all bands and is optional. 

    We should store at least the following tags:
    {
        'band_i': {
            manufacturer: 'value',
            model: 'value',
            date_and_time: 'value',
            focal_length: 'value',
            x_resolution: 'value',
            y_resolution: 'value',
            resolution_unit: 'value',
            pixel_x_dimension: 'value',
            pixel_y_dimension: 'value',
            flash: 'value',
        }
    }
    """

    # Multispectral image
    multispectral_image = models.FileField(
        'multispectral image',
        upload_to='/msdata/',
        help_text='A stacked tiff file with all bands.',
        blank=True,
        null=True
    )

    bucket = models.ForeignKey('multispectral.MSBucket', on_delete=CASCADE)

    # Metadata
    
    # exif tags
    exif_tags = models.JSONField(blank=True, null=True)

    # Location
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    label = models.CharField(
        'label',
        help_text='label for image classification.'
    )

    # Regions are box ground truth for objects in the image.
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#jsonfield
    regions = models.JSONField(blank=True, null=True)

