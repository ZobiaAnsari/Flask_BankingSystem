from marshmallow import Schema, fields,validate


class TransactionSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    amount = fields.Float(required=True, positive = True)
    transaction_type = fields.Str(required=True)
    timestamp = fields.DateTime(dump_only=True)