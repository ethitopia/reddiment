from itsdangerous import URLSafeSerializer

SECRET_KEY = "your-secret-key"

serializer = URLSafeSerializer(SECRET_KEY)

def create_session_token(username: str):
    return serializer.dumps({"username": username})

def get_username_from_token(token: str):
    try:
        data = serializer.loads(token)
        return data.get("username")
    except Exception:
        return None
