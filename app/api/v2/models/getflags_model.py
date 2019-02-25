from datetime import datetime

REDFLAG = []

class Redflag:
    ''' Creates an objects for the class '''
    def __init__(self, **kwargs):
        self.id = len(REDFLAG)+1
        self.createdOn = str(datetime.utcnow())
        self.createdBy = kwargs.get("createdBy")
        self.type = kwargs.get("type")
        self.comment = kwargs.get("comment")
        self.location = kwargs.get("location")
        self.status = "DRAFT" if kwargs.get("status") is None else kwargs.get("status")
        self.images = [] if kwargs.get("images") is None else kwargs.get("images")
        self.videos = [] if kwargs.get("videos") is None else kwargs.get("videos")
    @staticmethod
    def get_all():
        ''' The endpoint returns all redflags ''' 
        return REDFLAG
