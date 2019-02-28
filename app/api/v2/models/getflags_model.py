"""This module represents a meetup entity"""
from datetime import datetime

from app.api.v2.models.basemodel import BaseModel

TABLE_NAME = 'redflags'

class RedflagModel(BaseModel):
    """Entity representation for a meetup"""
    def __init__(self, **kwargs):
        super().__init__()
        self.created_by = kwargs.get('created_by')
        self.created_on = kwargs.get('created_on')
        self.type = kwargs.get('type')
        self.location = kwargs.get('comment')
        self.location = kwargs.get('location')
        self.images = "{}" if not kwargs.get('images') else kwargs.get('images')
        self.videos = "{}" if not kwargs.get('videos') else kwargs.get('videos')
        self.status = "{}" if not kwargs.get('status') else kwargs.get('status')

    def get_all(self):
        """Fetch all meetups"""
        result = self.fetch_all(TABLE_NAME)
        return result
