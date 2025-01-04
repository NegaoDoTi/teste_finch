from itsdangerous import URLSafeTimedSerializer
from config.config import SECRET_KEY

serializer = URLSafeTimedSerializer(SECRET_KEY)