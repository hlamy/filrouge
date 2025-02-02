# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# Code partiellement récupéré sur les tutoriels AWS Rekognition

"""
Purpose

Wraps several Amazon Rekognition elements in Python classes. Provides functions
to draw bounding boxes and polygons on an image and display it with the default
viewer.
"""

import io
import logging

class RekognitionText:
    """Encapsulates an Amazon Rekognition text element."""
    def __init__(self, text_data):
        """
        Initializes the text object.

        :param text_data: Text data, in the format returned by Amazon Rekognition
                          functions.
        """
        self.text = text_data.get('DetectedText')
        self.kind = text_data.get('Type')
        self.id = text_data.get('Id')
        self.parent_id = text_data.get('ParentId')
        self.confidence = text_data.get('Confidence')
        self.geometry = text_data.get('Geometry')

    def to_dict(self):
        """
        Renders some of the text data to a dict.

        :return: A dict that contains the text data.
        """
        rendering = {}
        if self.text is not None:
            rendering['text'] = self.text
        if self.kind is not None:
            rendering['kind'] = self.kind
        if self.geometry is not None:
            rendering['polygon'] = self.geometry.get('Polygon')
        return rendering
