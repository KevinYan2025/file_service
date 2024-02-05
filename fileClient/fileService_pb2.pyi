from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FileRequest(_message.Message):
    __slots__ = ("fileName",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    fileName: str
    def __init__(self, fileName: _Optional[str] = ...) -> None: ...

class FileResponse(_message.Message):
    __slots__ = ("fileContent",)
    FILECONTENT_FIELD_NUMBER: _ClassVar[int]
    fileContent: str
    def __init__(self, fileContent: _Optional[str] = ...) -> None: ...
