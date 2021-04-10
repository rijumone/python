from marshmallow import Schema, fields


class EncodeInputSchema(Schema):
    """ /encode - POST

    Parameters:
     - url (str)

    """

    url = fields.Str(required=True)


class DecodeInputSchema(Schema):
    """ /decode - POST

    Parameters:
     - short_url (str)

    """

    short_url = fields.Str(required=True)
