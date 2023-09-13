host: str = '0.0.0.0'
port: int = 8000
allow_credentials: bool = True
allow_methods: list[str] = ["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"]
allow_headers: list[str] = ["*"]
