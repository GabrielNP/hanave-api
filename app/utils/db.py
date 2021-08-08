import json
import uuid
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import DeclarativeMeta


db = SQLAlchemy()

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}

            for field in [x for x in dir(obj) if not x.startswith('') and x != 'metadata' and not x.startswith('_') and x != 'registry' and x != 'query' and x != 'query_class']:
                data = obj.__getattribute(field)
                try:
                    if isinstance(data, uuid.UUID):
                        data = data.hex
                    elif isinstance(data, datetime):
                        data = data.isoformat()
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None

            return fields

        return json.JSONEncoder.default(self, obj)

class Parser():
    def parse(obj):
        if isinstance(obj, list):
            processed = []

            for o in obj:
                processed.append(json.loads(json.dumps(o, cls=AlchemyEncoder)))

            return processed
        else:
            return json.loads(json.dumps(obj, cls=AlchemyEncoder))