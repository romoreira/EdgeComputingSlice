# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sid_management.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sid_management.proto',
  package='sidmanagement',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14sid_management.proto\x12\rsidmanagement\"-\n\nSIDMessage\x12\x1f\n\x03sid\x18\x01 \x03(\x0b\x32\x12.sidmanagement.SID\"_\n\x03SID\x12\x0b\n\x03SID\x18\x01 \x01(\t\x12\x14\n\x0cSID_BEHAVIOR\x18\x02 \x01(\t\x12\x0f\n\x07IP_ADDR\x18\x03 \x01(\t\x12\x11\n\tTARGET_IF\x18\x04 \x01(\t\x12\x11\n\tSOURCE_IF\x18\x05 \x01(\t\"\"\n\x0fSIDMessageReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\x9d\x01\n\rSIDManagement\x12\x45\n\x06\x41\x64\x64SID\x12\x19.sidmanagement.SIDMessage\x1a\x1e.sidmanagement.SIDMessageReply\"\x00\x12\x45\n\x06\x44\x65lSID\x12\x19.sidmanagement.SIDMessage\x1a\x1e.sidmanagement.SIDMessageReply\"\x00\x62\x06proto3')
)




_SIDMESSAGE = _descriptor.Descriptor(
  name='SIDMessage',
  full_name='sidmanagement.SIDMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sid', full_name='sidmanagement.SIDMessage.sid', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=84,
)


_SID = _descriptor.Descriptor(
  name='SID',
  full_name='sidmanagement.SID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SID', full_name='sidmanagement.SID.SID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SID_BEHAVIOR', full_name='sidmanagement.SID.SID_BEHAVIOR', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='IP_ADDR', full_name='sidmanagement.SID.IP_ADDR', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TARGET_IF', full_name='sidmanagement.SID.TARGET_IF', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='SOURCE_IF', full_name='sidmanagement.SID.SOURCE_IF', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=181,
)


_SIDMESSAGEREPLY = _descriptor.Descriptor(
  name='SIDMessageReply',
  full_name='sidmanagement.SIDMessageReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='sidmanagement.SIDMessageReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=183,
  serialized_end=217,
)

_SIDMESSAGE.fields_by_name['sid'].message_type = _SID
DESCRIPTOR.message_types_by_name['SIDMessage'] = _SIDMESSAGE
DESCRIPTOR.message_types_by_name['SID'] = _SID
DESCRIPTOR.message_types_by_name['SIDMessageReply'] = _SIDMESSAGEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SIDMessage = _reflection.GeneratedProtocolMessageType('SIDMessage', (_message.Message,), {
  'DESCRIPTOR' : _SIDMESSAGE,
  '__module__' : 'sid_management_pb2'
  # @@protoc_insertion_point(class_scope:sidmanagement.SIDMessage)
  })
_sym_db.RegisterMessage(SIDMessage)

SID = _reflection.GeneratedProtocolMessageType('SID', (_message.Message,), {
  'DESCRIPTOR' : _SID,
  '__module__' : 'sid_management_pb2'
  # @@protoc_insertion_point(class_scope:sidmanagement.SID)
  })
_sym_db.RegisterMessage(SID)

SIDMessageReply = _reflection.GeneratedProtocolMessageType('SIDMessageReply', (_message.Message,), {
  'DESCRIPTOR' : _SIDMESSAGEREPLY,
  '__module__' : 'sid_management_pb2'
  # @@protoc_insertion_point(class_scope:sidmanagement.SIDMessageReply)
  })
_sym_db.RegisterMessage(SIDMessageReply)



_SIDMANAGEMENT = _descriptor.ServiceDescriptor(
  name='SIDManagement',
  full_name='sidmanagement.SIDManagement',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=220,
  serialized_end=377,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddSID',
    full_name='sidmanagement.SIDManagement.AddSID',
    index=0,
    containing_service=None,
    input_type=_SIDMESSAGE,
    output_type=_SIDMESSAGEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DelSID',
    full_name='sidmanagement.SIDManagement.DelSID',
    index=1,
    containing_service=None,
    input_type=_SIDMESSAGE,
    output_type=_SIDMESSAGEREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIDMANAGEMENT)

DESCRIPTOR.services_by_name['SIDManagement'] = _SIDMANAGEMENT

# @@protoc_insertion_point(module_scope)
