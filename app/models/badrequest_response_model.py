from flask_restplus import fields


class BadRequestResponseModel:

    def __init__(self, api):
        self.api = api

    field = fields.String(
        title="フィールド名",
        example="フィールド名",
        description="",
        required=True,
    )

    message = fields.String(
        title="エラー内容",
        description="IDを数値で指定してください.",
        required=True,
    )

    def badrequest_error(self):
        return self.api.model(name="BadRequest Error", model={
            self.field.title: self.field,
            self.message.title: self.message,
        })

    def badrequest_response_model(self):
        return self.api.model(name="BadRequest Response Model", model={
            "errors": fields.Nested(self.badrequest_error()),
        })
