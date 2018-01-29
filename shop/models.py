# -*- coding: utf-8 -*-
from mongoengine import Document, EmbeddedDocument, fields





class Shop(Document):
    name = fields.StringField()
    email = fields.StringField()
    picture = fields.StringField()
    city = fields.StringField()
    location = fields.PointField()
    #location = GeopositionField(db_index=True)
