from dataclasses import dataclass

from bcrypt import checkpw, gensalt, hashpw


@dataclass
class PasswordHasherService:
    _encoding: str = "utf-8"

    def hash_password(self, plain_password: str) -> str:
        return hashpw(
            password=plain_password.encode(self._encoding),
            salt=gensalt(),
        ).decode(self._encoding)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return checkpw(
            password=plain_password.encode(self._encoding),
            hashed_password=hashed_password.encode(self._encoding),
        )
