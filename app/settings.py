# app/settings.py
import base64
from pydantic import BaseModel

class Settings(BaseModel):
    # Keep the AES keys as they are (they rarely change)
    MAIN_KEY_B64: str = "WWcmdGMlREV1aDYlWmNeOA=="
    MAIN_IV_B64: str = "Nm95WkRyMjJFM3ljaGpNJQ=="
    
    # UPDATE 1: Change the release version to OB55
    RELEASE_VERSION: str = "OB55"
    
    # UPDATE 2: Update User-Agent to a recent Android version (OB55 era)
    USER_AGENT: str = "GarenaMSDK/4.0.19P10(I2404 ;Android 15;en;US;)"
    
    # UPDATE 3: The /api/v2/ path is removed in the newer endpoint
    OAUTH_URL: str = "https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant"
    
    # This remains the same
    MAJOR_LOGIN_URL: str = "https://loginbp.ggwhitehawk.com/MajorLogin"
    
    # Client secret remains the same for this flow
    CLIENT_SECRET_PAYLOAD: str = (
        "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3&client_id=100067"
    )
    
    X_UNITY_VERSION: str = "2018.4.11f1"
    TIMEOUT: float = 10.0

    @property
    def MAIN_KEY(self) -> bytes:
        return base64.b64decode(self.MAIN_KEY_B64)

    @property
    def MAIN_IV(self) -> bytes:
        return base64.b64decode(self.MAIN_IV_B64)

settings = Settings()