# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: slice_create.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='slice_create.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x12slice_create.proto\"\x1c\n\rCreateRequest\x12\x0b\n\x03SID\x18\x01 \x01(\t\" \n\rCreationReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1c\n\rDeleteRequest\x12\x0b\n\x03SID\x18\x01 \x01(\t\" \n\rDeletionReply\x12\x0f\n\x07message\x18\x01 \x01(\t2p\n\x0cSliceManager\x12/\n\x0b\x43reateSlice\x12\x0e.CreateRequest\x1a\x0e.CreationReply\"\x00\x12/\n\x0b\x44\x65leteSlice\x12\x0e.DeleteRequest\x1a\x0e.DeletionReply\"\x00\x62\x06proto3'
)




_CREATEREQUEST = _descriptor.Descriptor(
  name='CreateRequest',
  full_name='CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SID', full_name='CreateRequest.SID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=22,
  serialized_end=50,
)


_CREATIONREPLY = _descriptor.Descriptor(
  name='CreationReply',
  full_name='CreationReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='CreationReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=52,
  serialized_end=84,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SID', full_name='DeleteRequest.SID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_end=114,
)


_DELETIONREPLY = _descriptor.Descriptor(
  name='DeletionReply',
  full_name='DeletionReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='DeletionReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=116,
  serialized_end=148,
)

DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
DESCRIPTOR.message_types_by_name['CreationReply'] = _CREATIONREPLY
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeletionReply'] = _DELETIONREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREQUEST,
  '__module__' : 'slice_create_pb2'
  # @@protoc_insertion_point(class_scope:CreateRequest)
  })
_sym_db.RegisterMessage(CreateRequest)

CreationReply = _reflection.GeneratedProtocolMessageType('CreationReply', (_message.Message,), {
  'DESCRIPTOR' : _CREATIONREPLY,
  '__module__' : 'slice_create_pb2'
  # @@protoc_insertion_point(class_scope:CreationReply)
  })
_sym_db.RegisterMessage(CreationReply)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUEST,
  '__module__' : 'slice_create_pb2'
  # @@protoc_insertion_point(class_scope:DeleteRequest)
  })
_sym_db.RegisterMessage(DeleteRequest)

DeletionReply = _reflection.GeneratedProtocolMessageType('DeletionReply', (_message.Message,), {
  'DESCRIPTOR' : _DELETIONREPLY,
  '__module__' : 'slice_create_pb2'
  # @@protoc_insertion_point(class_scope:DeletionReply)
  })
_sym_db.RegisterMessage(DeletionReply)



_SLICEMANAGER = _descriptor.ServiceDescriptor(
  name='SliceManager',
  full_name='SliceManager',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=150,
  serialized_end=262,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateSlice',
    full_name='SliceManager.CreateSlice',
    index=0,
    containing_service=None,
    input_type=_CREATEREQUEST,
    output_type=_CREATIONREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteSlice',
    full_name='SliceManager.DeleteSlice',
    index=1,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_DELETIONREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SLICEMANAGER)

DESCRIPTOR.services_by_name['SliceManager'] = _SLICEMANAGER

# @@protoc_insertion_point(module_scope)
