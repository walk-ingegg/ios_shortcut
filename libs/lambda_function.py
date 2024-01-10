import json


def lambda_handler(event, context):
    # イベントのbodyを取得
    body = event.get("body")

    # bodyが存在するか確認
    if body is not None:
        # bodyをJSONオブジェクトにパース
        try:
            parsed_body = json.loads(body)
            text_value = parsed_body.get("text")
            # 処理が成功した場合のレスポンス
            return {
                "statusCode": 200,
                "body": json.dumps(
                    {"message": "Processing Success", "textValue": text_value}
                ),
            }
        except json.JSONDecodeError:
            # JSON解析に失敗した場合のエラーレスポンス
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Invalid JSON format"}),
            }
    else:
        # bodyが存在しない場合のエラーレスポンス
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "request body is empty"}),
        }
