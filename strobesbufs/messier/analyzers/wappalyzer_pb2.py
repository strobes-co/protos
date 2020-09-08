# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: strobesbufs/messier/analyzers/wappalyzer.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from strobesbufs.messier import common_pb2 as strobesbufs_dot_messier_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='strobesbufs/messier/analyzers/wappalyzer.proto',
  package='strobesbufs.messier.analyzer',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.strobesbufs/messier/analyzers/wappalyzer.proto\x12\x1cstrobesbufs.messier.analyzer\x1a strobesbufs/messier/common.proto\"^\n\nWappalyzer\x12\x0e\n\x06target\x18\x01 \x01(\t\x12\x31\n\x03log\x18\x02 \x01(\x0e\x32$.strobesbufs.messier.common.LogLevel\x12\r\n\x05probe\x18\x03 \x01(\x08\x62\x06proto3'
  ,
  dependencies=[strobesbufs_dot_messier_dot_common__pb2.DESCRIPTOR,])




_WAPPALYZER = _descriptor.Descriptor(
  name='Wappalyzer',
  full_name='strobesbufs.messier.analyzer.Wappalyzer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='strobesbufs.messier.analyzer.Wappalyzer.target', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log', full_name='strobesbufs.messier.analyzer.Wappalyzer.log', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='probe', full_name='strobesbufs.messier.analyzer.Wappalyzer.probe', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=114,
  serialized_end=208,
)

_WAPPALYZER.fields_by_name['log'].enum_type = strobesbufs_dot_messier_dot_common__pb2._LOGLEVEL
DESCRIPTOR.message_types_by_name['Wappalyzer'] = _WAPPALYZER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Wappalyzer = _reflection.GeneratedProtocolMessageType('Wappalyzer', (_message.Message,), {
  'DESCRIPTOR' : _WAPPALYZER,
  '__module__' : 'strobesbufs.messier.analyzers.wappalyzer_pb2'
  # @@protoc_insertion_point(class_scope:strobesbufs.messier.analyzer.Wappalyzer)
  })
_sym_db.RegisterMessage(Wappalyzer)


# @@protoc_insertion_point(module_scope)