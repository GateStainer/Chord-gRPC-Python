# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='server.proto',
  package='server',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cserver.proto\x12\x06server\"\x1c\n\x0e\x46indSucRequest\x12\n\n\x02id\x18\x01 \x01(\x05\")\n\x0f\x46indSucResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\n\n\x02ip\x18\x02 \x01(\t\" \n\x12PredecessorRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"6\n\x13PredecessorResponse\x12\x1f\n\x03ret\x18\x01 \x01(\x0e\x32\x12.server.ReturnCode*&\n\nReturnCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\x32\x9c\x01\n\x06Server\x12\x43\n\x0e\x66ind_successor\x12\x16.server.FindSucRequest\x1a\x17.server.FindSucResponse\"\x00\x12M\n\x10live_predecessor\x12\x1a.server.PredecessorRequest\x1a\x1b.server.PredecessorResponse\"\x00\x62\x06proto3')
)

_RETURNCODE = _descriptor.EnumDescriptor(
  name='ReturnCode',
  full_name='server.ReturnCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=187,
  serialized_end=225,
)
_sym_db.RegisterEnumDescriptor(_RETURNCODE)

ReturnCode = enum_type_wrapper.EnumTypeWrapper(_RETURNCODE)
SUCCESS = 0
FAILURE = 1



_FINDSUCREQUEST = _descriptor.Descriptor(
  name='FindSucRequest',
  full_name='server.FindSucRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='server.FindSucRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=24,
  serialized_end=52,
)


_FINDSUCRESPONSE = _descriptor.Descriptor(
  name='FindSucResponse',
  full_name='server.FindSucResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='server.FindSucResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='server.FindSucResponse.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=54,
  serialized_end=95,
)


_PREDECESSORREQUEST = _descriptor.Descriptor(
  name='PredecessorRequest',
  full_name='server.PredecessorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='server.PredecessorRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=97,
  serialized_end=129,
)


_PREDECESSORRESPONSE = _descriptor.Descriptor(
  name='PredecessorResponse',
  full_name='server.PredecessorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='server.PredecessorResponse.ret', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=131,
  serialized_end=185,
)

_PREDECESSORRESPONSE.fields_by_name['ret'].enum_type = _RETURNCODE
DESCRIPTOR.message_types_by_name['FindSucRequest'] = _FINDSUCREQUEST
DESCRIPTOR.message_types_by_name['FindSucResponse'] = _FINDSUCRESPONSE
DESCRIPTOR.message_types_by_name['PredecessorRequest'] = _PREDECESSORREQUEST
DESCRIPTOR.message_types_by_name['PredecessorResponse'] = _PREDECESSORRESPONSE
DESCRIPTOR.enum_types_by_name['ReturnCode'] = _RETURNCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FindSucRequest = _reflection.GeneratedProtocolMessageType('FindSucRequest', (_message.Message,), dict(
  DESCRIPTOR = _FINDSUCREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.FindSucRequest)
  ))
_sym_db.RegisterMessage(FindSucRequest)

FindSucResponse = _reflection.GeneratedProtocolMessageType('FindSucResponse', (_message.Message,), dict(
  DESCRIPTOR = _FINDSUCRESPONSE,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.FindSucResponse)
  ))
_sym_db.RegisterMessage(FindSucResponse)

PredecessorRequest = _reflection.GeneratedProtocolMessageType('PredecessorRequest', (_message.Message,), dict(
  DESCRIPTOR = _PREDECESSORREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.PredecessorRequest)
  ))
_sym_db.RegisterMessage(PredecessorRequest)

PredecessorResponse = _reflection.GeneratedProtocolMessageType('PredecessorResponse', (_message.Message,), dict(
  DESCRIPTOR = _PREDECESSORRESPONSE,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.PredecessorResponse)
  ))
_sym_db.RegisterMessage(PredecessorResponse)



_SERVER = _descriptor.ServiceDescriptor(
  name='Server',
  full_name='server.Server',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=228,
  serialized_end=384,
  methods=[
  _descriptor.MethodDescriptor(
    name='find_successor',
    full_name='server.Server.find_successor',
    index=0,
    containing_service=None,
    input_type=_FINDSUCREQUEST,
    output_type=_FINDSUCRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='live_predecessor',
    full_name='server.Server.live_predecessor',
    index=1,
    containing_service=None,
    input_type=_PREDECESSORREQUEST,
    output_type=_PREDECESSORRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVER)

DESCRIPTOR.services_by_name['Server'] = _SERVER

# @@protoc_insertion_point(module_scope)
