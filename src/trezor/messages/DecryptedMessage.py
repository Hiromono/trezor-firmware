# Automatically generated by pb2py
import protobuf as p


class DecryptedMessage(p.MessageType):
    FIELDS = {
        1: ('message', p.BytesType, 0),
        2: ('address', p.UnicodeType, 0),
    }
    MESSAGE_WIRE_TYPE = 52

    def __init__(
        self,
        message: bytes = None,
        address: str = None,
        **kwargs,
    ):
        self.message = message
        self.address = address
        p.MessageType.__init__(self, **kwargs)