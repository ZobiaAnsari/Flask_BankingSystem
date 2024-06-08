from marshmallow import Schema, fields,validate

class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    email = fields.Str(validate = validate.Regexp(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'))
    phone = fields.Str(validate=validate.Regexp(r'^\d{10}$'))
    address = fields.Str()
    pin = fields.Int(validate=validate.Range(min=100000, max=999999))
    accountNo = fields.Str(validate=validate.Regexp(r'^\d{10}$'))
    accountPin = fields.Str(validate=validate.Regexp(r'^\d{4}$'))
    password = fields.Str(validate = validate.Length(min=8))
    balance  = fields.Int(validate=(validate.Range(min=0),validate.Regexp(r'^[0-9]$')), positive = True)