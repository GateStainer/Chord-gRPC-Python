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
  serialized_pb=_b('\n\x0cserver.proto\x12\x06server\"\x94\x01\n\nNodeStatus\x12\n\n\x02id\x18\x01 \x01(\x05\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0f\n\x07pred_id\x18\x03 \x01(\x05\x12\x0f\n\x07pred_ip\x18\x04 \x01(\t\x12\x12\n\nsuclist_id\x18\x05 \x03(\x05\x12\x12\n\nsuclist_ip\x18\x06 \x03(\t\x12\x11\n\tfinger_id\x18\x07 \x03(\x05\x12\x11\n\tfinger_ip\x18\x08 \x03(\t\"\x0e\n\x0c\x45mptyRequest\"\x0f\n\rEmptyResponse\"(\n\x0eRectifyRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\n\n\x02ip\x18\x02 \x01(\t\"\x1c\n\x0e\x46indSucRequest\x12\n\n\x02id\x18\x01 \x01(\x05\")\n\x0f\x46indSucResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\n\n\x02ip\x18\x02 \x01(\t\"*\n\x10\x46indPredResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\n\n\x02ip\x18\x02 \x01(\t\"8\n\x14\x46indSucclistResponse\x12\x0f\n\x07id_list\x18\x01 \x03(\x05\x12\x0f\n\x07ip_list\x18\x02 \x03(\t\" \n\x12PredecessorRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"6\n\x13PredecessorResponse\x12\x1f\n\x03ret\x18\x01 \x01(\x0e\x32\x12.server.ReturnCode\"4\n\x08LogEntry\x12\x0e\n\x06hashID\x18\x01 \x01(\x05\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0b\n\x03val\x18\x03 \x01(\t\"5\n\x10ReplicateRequest\x12!\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x10.server.LogEntry\"4\n\x11ReplicateResponse\x12\x1f\n\x03ret\x18\x01 \x01(\x0e\x32\x12.server.ReturnCode\"\x19\n\nGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"?\n\x0bGetResponse\x12\x10\n\x08response\x18\x01 \x01(\t\x12\x0e\n\x06nodeID\x18\x02 \x01(\x05\x12\x0e\n\x06nodeIP\x18\x03 \x01(\t\"(\n\nPutRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"N\n\x0bPutResponse\x12\x1f\n\x03ret\x18\x01 \x01(\x0e\x32\x12.server.ReturnCode\x12\x0e\n\x06nodeID\x18\x02 \x01(\x05\x12\x0e\n\x06nodeIP\x18\x03 \x01(\t*&\n\nReturnCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\x32\xd4\x04\n\x06Server\x12\x43\n\x0e\x66ind_successor\x12\x16.server.FindSucRequest\x1a\x17.server.FindSucResponse\"\x00\x12M\n\x10live_predecessor\x12\x1a.server.PredecessorRequest\x1a\x1b.server.PredecessorResponse\"\x00\x12\x45\n\rfind_succlist\x12\x14.server.EmptyRequest\x1a\x1c.server.FindSucclistResponse\"\x00\x12\x44\n\x10\x66ind_predecessor\x12\x14.server.EmptyRequest\x1a\x18.server.FindPredResponse\"\x00\x12:\n\x07rectify\x12\x16.server.RectifyRequest\x1a\x15.server.EmptyResponse\"\x00\x12=\n\x0fget_node_status\x12\x14.server.EmptyRequest\x1a\x12.server.NodeStatus\"\x00\x12J\n\x11replicate_entries\x12\x18.server.ReplicateRequest\x1a\x19.server.ReplicateResponse\"\x00\x12\x30\n\x03get\x12\x12.server.GetRequest\x1a\x13.server.GetResponse\"\x00\x12\x30\n\x03put\x12\x12.server.PutRequest\x1a\x13.server.PutResponse\"\x00\x62\x06proto3')
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
  serialized_start=892,
  serialized_end=930,
)
_sym_db.RegisterEnumDescriptor(_RETURNCODE)

ReturnCode = enum_type_wrapper.EnumTypeWrapper(_RETURNCODE)
SUCCESS = 0
FAILURE = 1



_NODESTATUS = _descriptor.Descriptor(
  name='NodeStatus',
  full_name='server.NodeStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='server.NodeStatus.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='server.NodeStatus.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pred_id', full_name='server.NodeStatus.pred_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pred_ip', full_name='server.NodeStatus.pred_ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suclist_id', full_name='server.NodeStatus.suclist_id', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suclist_ip', full_name='server.NodeStatus.suclist_ip', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finger_id', full_name='server.NodeStatus.finger_id', index=6,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finger_ip', full_name='server.NodeStatus.finger_ip', index=7,
      number=8, type=9, cpp_type=9, label=3,
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
  serialized_start=25,
  serialized_end=173,
)


_EMPTYREQUEST = _descriptor.Descriptor(
  name='EmptyRequest',
  full_name='server.EmptyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=175,
  serialized_end=189,
)


_EMPTYRESPONSE = _descriptor.Descriptor(
  name='EmptyResponse',
  full_name='server.EmptyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=191,
  serialized_end=206,
)


_RECTIFYREQUEST = _descriptor.Descriptor(
  name='RectifyRequest',
  full_name='server.RectifyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='server.RectifyRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='server.RectifyRequest.ip', index=1,
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
  serialized_start=208,
  serialized_end=248,
)


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
  serialized_start=250,
  serialized_end=278,
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
  serialized_start=280,
  serialized_end=321,
)


_FINDPREDRESPONSE = _descriptor.Descriptor(
  name='FindPredResponse',
  full_name='server.FindPredResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='server.FindPredResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='server.FindPredResponse.ip', index=1,
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
  serialized_start=323,
  serialized_end=365,
)


_FINDSUCCLISTRESPONSE = _descriptor.Descriptor(
  name='FindSucclistResponse',
  full_name='server.FindSucclistResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_list', full_name='server.FindSucclistResponse.id_list', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_list', full_name='server.FindSucclistResponse.ip_list', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=367,
  serialized_end=423,
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
  serialized_start=425,
  serialized_end=457,
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
  serialized_start=459,
  serialized_end=513,
)


_LOGENTRY = _descriptor.Descriptor(
  name='LogEntry',
  full_name='server.LogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hashID', full_name='server.LogEntry.hashID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='server.LogEntry.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='val', full_name='server.LogEntry.val', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=515,
  serialized_end=567,
)


_REPLICATEREQUEST = _descriptor.Descriptor(
  name='ReplicateRequest',
  full_name='server.ReplicateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='server.ReplicateRequest.entries', index=0,
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
  serialized_start=569,
  serialized_end=622,
)


_REPLICATERESPONSE = _descriptor.Descriptor(
  name='ReplicateResponse',
  full_name='server.ReplicateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='server.ReplicateResponse.ret', index=0,
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
  serialized_start=624,
  serialized_end=676,
)


_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='server.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='server.GetRequest.key', index=0,
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
  serialized_start=678,
  serialized_end=703,
)


_GETRESPONSE = _descriptor.Descriptor(
  name='GetResponse',
  full_name='server.GetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='server.GetResponse.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodeID', full_name='server.GetResponse.nodeID', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodeIP', full_name='server.GetResponse.nodeIP', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=705,
  serialized_end=768,
)


_PUTREQUEST = _descriptor.Descriptor(
  name='PutRequest',
  full_name='server.PutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='server.PutRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='server.PutRequest.value', index=1,
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
  serialized_start=770,
  serialized_end=810,
)


_PUTRESPONSE = _descriptor.Descriptor(
  name='PutResponse',
  full_name='server.PutResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='server.PutResponse.ret', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodeID', full_name='server.PutResponse.nodeID', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodeIP', full_name='server.PutResponse.nodeIP', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=812,
  serialized_end=890,
)

_PREDECESSORRESPONSE.fields_by_name['ret'].enum_type = _RETURNCODE
_REPLICATEREQUEST.fields_by_name['entries'].message_type = _LOGENTRY
_REPLICATERESPONSE.fields_by_name['ret'].enum_type = _RETURNCODE
_PUTRESPONSE.fields_by_name['ret'].enum_type = _RETURNCODE
DESCRIPTOR.message_types_by_name['NodeStatus'] = _NODESTATUS
DESCRIPTOR.message_types_by_name['EmptyRequest'] = _EMPTYREQUEST
DESCRIPTOR.message_types_by_name['EmptyResponse'] = _EMPTYRESPONSE
DESCRIPTOR.message_types_by_name['RectifyRequest'] = _RECTIFYREQUEST
DESCRIPTOR.message_types_by_name['FindSucRequest'] = _FINDSUCREQUEST
DESCRIPTOR.message_types_by_name['FindSucResponse'] = _FINDSUCRESPONSE
DESCRIPTOR.message_types_by_name['FindPredResponse'] = _FINDPREDRESPONSE
DESCRIPTOR.message_types_by_name['FindSucclistResponse'] = _FINDSUCCLISTRESPONSE
DESCRIPTOR.message_types_by_name['PredecessorRequest'] = _PREDECESSORREQUEST
DESCRIPTOR.message_types_by_name['PredecessorResponse'] = _PREDECESSORRESPONSE
DESCRIPTOR.message_types_by_name['LogEntry'] = _LOGENTRY
DESCRIPTOR.message_types_by_name['ReplicateRequest'] = _REPLICATEREQUEST
DESCRIPTOR.message_types_by_name['ReplicateResponse'] = _REPLICATERESPONSE
DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['GetResponse'] = _GETRESPONSE
DESCRIPTOR.message_types_by_name['PutRequest'] = _PUTREQUEST
DESCRIPTOR.message_types_by_name['PutResponse'] = _PUTRESPONSE
DESCRIPTOR.enum_types_by_name['ReturnCode'] = _RETURNCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeStatus = _reflection.GeneratedProtocolMessageType('NodeStatus', (_message.Message,), dict(
  DESCRIPTOR = _NODESTATUS,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.NodeStatus)
  ))
_sym_db.RegisterMessage(NodeStatus)

EmptyRequest = _reflection.GeneratedProtocolMessageType('EmptyRequest', (_message.Message,), dict(
  DESCRIPTOR = _EMPTYREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.EmptyRequest)
  ))
_sym_db.RegisterMessage(EmptyRequest)

EmptyResponse = _reflection.GeneratedProtocolMessageType('EmptyResponse', (_message.Message,), dict(
  DESCRIPTOR = _EMPTYRESPONSE,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.EmptyResponse)
  ))
_sym_db.RegisterMessage(EmptyResponse)

RectifyRequest = _reflection.GeneratedProtocolMessageType('RectifyRequest', (_message.Message,), dict(
  DESCRIPTOR = _RECTIFYREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.RectifyRequest)
  ))
_sym_db.RegisterMessage(RectifyRequest)

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

FindPredResponse = _reflection.GeneratedProtocolMessageType('FindPredResponse', (_message.Message,), dict(
  DESCRIPTOR = _FINDPREDRESPONSE,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.FindPredResponse)
  ))
_sym_db.RegisterMessage(FindPredResponse)

FindSucclistResponse = _reflection.GeneratedProtocolMessageType('FindSucclistResponse', (_message.Message,), dict(
  DESCRIPTOR = _FINDSUCCLISTRESPONSE,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.FindSucclistResponse)
  ))
_sym_db.RegisterMessage(FindSucclistResponse)

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

LogEntry = _reflection.GeneratedProtocolMessageType('LogEntry', (_message.Message,), dict(
  DESCRIPTOR = _LOGENTRY,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.LogEntry)
  ))
_sym_db.RegisterMessage(LogEntry)

ReplicateRequest = _reflection.GeneratedProtocolMessageType('ReplicateRequest', (_message.Message,), dict(
  DESCRIPTOR = _REPLICATEREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.ReplicateRequest)
  ))
_sym_db.RegisterMessage(ReplicateRequest)

ReplicateResponse = _reflection.GeneratedProtocolMessageType('ReplicateResponse', (_message.Message,), dict(
  DESCRIPTOR = _REPLICATERESPONSE,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.ReplicateResponse)
  ))
_sym_db.RegisterMessage(ReplicateResponse)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.GetRequest)
  ))
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETRESPONSE,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.GetResponse)
  ))
_sym_db.RegisterMessage(GetResponse)

PutRequest = _reflection.GeneratedProtocolMessageType('PutRequest', (_message.Message,), dict(
  DESCRIPTOR = _PUTREQUEST,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.PutRequest)
  ))
_sym_db.RegisterMessage(PutRequest)

PutResponse = _reflection.GeneratedProtocolMessageType('PutResponse', (_message.Message,), dict(
  DESCRIPTOR = _PUTRESPONSE,
  __module__ = 'server_pb2'
  # @@protoc_insertion_point(class_scope:server.PutResponse)
  ))
_sym_db.RegisterMessage(PutResponse)



_SERVER = _descriptor.ServiceDescriptor(
  name='Server',
  full_name='server.Server',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=933,
  serialized_end=1529,
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
  _descriptor.MethodDescriptor(
    name='find_succlist',
    full_name='server.Server.find_succlist',
    index=2,
    containing_service=None,
    input_type=_EMPTYREQUEST,
    output_type=_FINDSUCCLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='find_predecessor',
    full_name='server.Server.find_predecessor',
    index=3,
    containing_service=None,
    input_type=_EMPTYREQUEST,
    output_type=_FINDPREDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='rectify',
    full_name='server.Server.rectify',
    index=4,
    containing_service=None,
    input_type=_RECTIFYREQUEST,
    output_type=_EMPTYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_node_status',
    full_name='server.Server.get_node_status',
    index=5,
    containing_service=None,
    input_type=_EMPTYREQUEST,
    output_type=_NODESTATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='replicate_entries',
    full_name='server.Server.replicate_entries',
    index=6,
    containing_service=None,
    input_type=_REPLICATEREQUEST,
    output_type=_REPLICATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='server.Server.get',
    index=7,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_GETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='put',
    full_name='server.Server.put',
    index=8,
    containing_service=None,
    input_type=_PUTREQUEST,
    output_type=_PUTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVER)

DESCRIPTOR.services_by_name['Server'] = _SERVER

# @@protoc_insertion_point(module_scope)
