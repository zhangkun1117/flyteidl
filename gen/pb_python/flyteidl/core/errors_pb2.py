# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/core/errors.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/core/errors.proto',
  package='flyteidl.core',
  syntax='proto3',
  serialized_options=_b('Z0github.com/lyft/flyteidl/gen/pb-go/flyteidl/core'),
  serialized_pb=_b('\n\x1a\x66lyteidl/core/errors.proto\x12\rflyteidl.core\"\x8f\x01\n\x0e\x43ontainerError\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x30\n\x04kind\x18\x03 \x01(\x0e\x32\".flyteidl.core.ContainerError.Kind\",\n\x04Kind\x12\x13\n\x0fNON_RECOVERABLE\x10\x00\x12\x0f\n\x0bRECOVERABLE\x10\x01\"=\n\rErrorDocument\x12,\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1d.flyteidl.core.ContainerErrorB2Z0github.com/lyft/flyteidl/gen/pb-go/flyteidl/coreb\x06proto3')
)



_CONTAINERERROR_KIND = _descriptor.EnumDescriptor(
  name='Kind',
  full_name='flyteidl.core.ContainerError.Kind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NON_RECOVERABLE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RECOVERABLE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=145,
  serialized_end=189,
)
_sym_db.RegisterEnumDescriptor(_CONTAINERERROR_KIND)


_CONTAINERERROR = _descriptor.Descriptor(
  name='ContainerError',
  full_name='flyteidl.core.ContainerError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='flyteidl.core.ContainerError.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='flyteidl.core.ContainerError.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='flyteidl.core.ContainerError.kind', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONTAINERERROR_KIND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=189,
)


_ERRORDOCUMENT = _descriptor.Descriptor(
  name='ErrorDocument',
  full_name='flyteidl.core.ErrorDocument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='flyteidl.core.ErrorDocument.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=191,
  serialized_end=252,
)

_CONTAINERERROR.fields_by_name['kind'].enum_type = _CONTAINERERROR_KIND
_CONTAINERERROR_KIND.containing_type = _CONTAINERERROR
_ERRORDOCUMENT.fields_by_name['error'].message_type = _CONTAINERERROR
DESCRIPTOR.message_types_by_name['ContainerError'] = _CONTAINERERROR
DESCRIPTOR.message_types_by_name['ErrorDocument'] = _ERRORDOCUMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContainerError = _reflection.GeneratedProtocolMessageType('ContainerError', (_message.Message,), dict(
  DESCRIPTOR = _CONTAINERERROR,
  __module__ = 'flyteidl.core.errors_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.ContainerError)
  ))
_sym_db.RegisterMessage(ContainerError)

ErrorDocument = _reflection.GeneratedProtocolMessageType('ErrorDocument', (_message.Message,), dict(
  DESCRIPTOR = _ERRORDOCUMENT,
  __module__ = 'flyteidl.core.errors_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.ErrorDocument)
  ))
_sym_db.RegisterMessage(ErrorDocument)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
