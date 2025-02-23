from dataclasses import dataclass

from bcrypt import checkpw, gensalt, hashpw


@dataclass
class PasswordHasherService:
    encoding: str = "utf-8"

    def hash_password(self, plain_password: str) -> str:
        return hashpw(
            password=plain_password.encode(self.encoding),
            salt=gensalt(),
        ).decode(self.encoding)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return checkpw(
            password=plain_password.encode(self.encoding),
            hashed_password=hashed_password.encode(self.encoding),
        )
