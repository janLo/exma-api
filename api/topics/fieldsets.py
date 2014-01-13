from api.fieldset import Fieldset
from flask.ext.restful import fields


class TopicFieldset(Fieldset):
    tid = fields.Integer
    title = fields.String
    last_post = fields.String
    last_poster_name = fields.String
    starter_name = fields.String


class PostFields(Fieldset):
    pid = fields.Integer
    post = fields.String
    author_name = fields.String
    post_date = fields.String
