# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/core/future.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.core import tasks_pb2 as flyteidl_dot_core_dot_tasks__pb2
from flyteidl.core import literals_pb2 as flyteidl_dot_core_dot_literals__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/core/future.proto',
  package='flyteidl.core',
  syntax='proto3',
  serialized_pb=_b('\n\x1a\x66lyteidl/core/future.proto\x12\rflyteidl.core\x1a\x19\x66lyteidl/core/tasks.proto\x1a\x1c\x66lyteidl/core/literals.proto\"\x82\x01\n\x12\x46utureTaskDocument\x12,\n\x05tasks\x18\x01 \x03(\x0b\x32\x1d.flyteidl.core.FutureTaskNode\x12\x15\n\rmin_successes\x18\x02 \x01(\x03\x12\'\n\x07outputs\x18\x03 \x03(\x0b\x32\x16.flyteidl.core.Binding\"\x8c\x02\n\x0e\x46utureTaskNode\x12\x13\n\x0bgenerate_id\x18\x01 \x01(\t\x12\x30\n\x04kind\x18\x02 \x01(\x0e\x32\".flyteidl.core.FutureTaskNode.Kind\x12(\n\x05\x61rray\x18\x03 \x01(\x0b\x32\x17.flyteidl.core.ArrayJobH\x00\x12:\n\x0chive_queries\x18\x04 \x01(\x0b\x32\".flyteidl.core.HiveQueryCollectionH\x00\"C\n\x04Kind\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x13\n\x0f\x41RRAY_CONTAINER\x10\x01\x12\x0f\n\x0b\x41RRAY_SWARM\x10\x02\x12\x08\n\x04HIVE\x10\x03\x42\x08\n\x06target\"I\n\tHiveQuery\x12\r\n\x05query\x18\x01 \x01(\t\x12-\n\x08metadata\x18\x02 \x01(\x0b\x32\x1b.flyteidl.core.TaskMetadata\"@\n\x13HiveQueryCollection\x12)\n\x07queries\x18\x02 \x03(\x0b\x32\x18.flyteidl.core.HiveQuery\"\xaf\x01\n\x0fSwarmDefinition\x12\x33\n\x11primary_container\x18\x01 \x01(\x0b\x32\x18.flyteidl.core.Container\x12\x31\n\x0finit_containers\x18\x02 \x03(\x0b\x32\x18.flyteidl.core.Container\x12\x34\n\x12sidecar_containers\x18\x03 \x03(\x0b\x32\x18.flyteidl.core.Container\"\xdc\x01\n\x08\x41rrayJob\x12-\n\x08metadata\x18\x01 \x01(\x0b\x32\x1b.flyteidl.core.TaskMetadata\x12\r\n\x05slots\x18\x02 \x01(\x03\x12\x13\n\x0b\x63ompletions\x18\x03 \x01(\x03\x12-\n\tcontainer\x18\x04 \x01(\x0b\x32\x18.flyteidl.core.ContainerH\x00\x12/\n\x05swarm\x18\x05 \x01(\x0b\x32\x1e.flyteidl.core.SwarmDefinitionH\x00\x12\x11\n\tinput_ref\x18\x06 \x01(\tB\n\n\x08runnableB2Z0github.com/lyft/flyteidl/gen/pb-go/flyteidl/coreb\x06proto3')
  ,
  dependencies=[flyteidl_dot_core_dot_tasks__pb2.DESCRIPTOR,flyteidl_dot_core_dot_literals__pb2.DESCRIPTOR,])



_FUTURETASKNODE_KIND = _descriptor.EnumDescriptor(
  name='Kind',
  full_name='flyteidl.core.FutureTaskNode.Kind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARRAY_CONTAINER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARRAY_SWARM', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIVE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=427,
  serialized_end=494,
)
_sym_db.RegisterEnumDescriptor(_FUTURETASKNODE_KIND)


_FUTURETASKDOCUMENT = _descriptor.Descriptor(
  name='FutureTaskDocument',
  full_name='flyteidl.core.FutureTaskDocument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='flyteidl.core.FutureTaskDocument.tasks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_successes', full_name='flyteidl.core.FutureTaskDocument.min_successes', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='flyteidl.core.FutureTaskDocument.outputs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=233,
)


_FUTURETASKNODE = _descriptor.Descriptor(
  name='FutureTaskNode',
  full_name='flyteidl.core.FutureTaskNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='generate_id', full_name='flyteidl.core.FutureTaskNode.generate_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='flyteidl.core.FutureTaskNode.kind', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='array', full_name='flyteidl.core.FutureTaskNode.array', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hive_queries', full_name='flyteidl.core.FutureTaskNode.hive_queries', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FUTURETASKNODE_KIND,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='target', full_name='flyteidl.core.FutureTaskNode.target',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=236,
  serialized_end=504,
)


_HIVEQUERY = _descriptor.Descriptor(
  name='HiveQuery',
  full_name='flyteidl.core.HiveQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='flyteidl.core.HiveQuery.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='flyteidl.core.HiveQuery.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=506,
  serialized_end=579,
)


_HIVEQUERYCOLLECTION = _descriptor.Descriptor(
  name='HiveQueryCollection',
  full_name='flyteidl.core.HiveQueryCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queries', full_name='flyteidl.core.HiveQueryCollection.queries', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=581,
  serialized_end=645,
)


_SWARMDEFINITION = _descriptor.Descriptor(
  name='SwarmDefinition',
  full_name='flyteidl.core.SwarmDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='primary_container', full_name='flyteidl.core.SwarmDefinition.primary_container', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='init_containers', full_name='flyteidl.core.SwarmDefinition.init_containers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sidecar_containers', full_name='flyteidl.core.SwarmDefinition.sidecar_containers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=648,
  serialized_end=823,
)


_ARRAYJOB = _descriptor.Descriptor(
  name='ArrayJob',
  full_name='flyteidl.core.ArrayJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='flyteidl.core.ArrayJob.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slots', full_name='flyteidl.core.ArrayJob.slots', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='completions', full_name='flyteidl.core.ArrayJob.completions', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='container', full_name='flyteidl.core.ArrayJob.container', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='swarm', full_name='flyteidl.core.ArrayJob.swarm', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_ref', full_name='flyteidl.core.ArrayJob.input_ref', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='runnable', full_name='flyteidl.core.ArrayJob.runnable',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=826,
  serialized_end=1046,
)

_FUTURETASKDOCUMENT.fields_by_name['tasks'].message_type = _FUTURETASKNODE
_FUTURETASKDOCUMENT.fields_by_name['outputs'].message_type = flyteidl_dot_core_dot_literals__pb2._BINDING
_FUTURETASKNODE.fields_by_name['kind'].enum_type = _FUTURETASKNODE_KIND
_FUTURETASKNODE.fields_by_name['array'].message_type = _ARRAYJOB
_FUTURETASKNODE.fields_by_name['hive_queries'].message_type = _HIVEQUERYCOLLECTION
_FUTURETASKNODE_KIND.containing_type = _FUTURETASKNODE
_FUTURETASKNODE.oneofs_by_name['target'].fields.append(
  _FUTURETASKNODE.fields_by_name['array'])
_FUTURETASKNODE.fields_by_name['array'].containing_oneof = _FUTURETASKNODE.oneofs_by_name['target']
_FUTURETASKNODE.oneofs_by_name['target'].fields.append(
  _FUTURETASKNODE.fields_by_name['hive_queries'])
_FUTURETASKNODE.fields_by_name['hive_queries'].containing_oneof = _FUTURETASKNODE.oneofs_by_name['target']
_HIVEQUERY.fields_by_name['metadata'].message_type = flyteidl_dot_core_dot_tasks__pb2._TASKMETADATA
_HIVEQUERYCOLLECTION.fields_by_name['queries'].message_type = _HIVEQUERY
_SWARMDEFINITION.fields_by_name['primary_container'].message_type = flyteidl_dot_core_dot_tasks__pb2._CONTAINER
_SWARMDEFINITION.fields_by_name['init_containers'].message_type = flyteidl_dot_core_dot_tasks__pb2._CONTAINER
_SWARMDEFINITION.fields_by_name['sidecar_containers'].message_type = flyteidl_dot_core_dot_tasks__pb2._CONTAINER
_ARRAYJOB.fields_by_name['metadata'].message_type = flyteidl_dot_core_dot_tasks__pb2._TASKMETADATA
_ARRAYJOB.fields_by_name['container'].message_type = flyteidl_dot_core_dot_tasks__pb2._CONTAINER
_ARRAYJOB.fields_by_name['swarm'].message_type = _SWARMDEFINITION
_ARRAYJOB.oneofs_by_name['runnable'].fields.append(
  _ARRAYJOB.fields_by_name['container'])
_ARRAYJOB.fields_by_name['container'].containing_oneof = _ARRAYJOB.oneofs_by_name['runnable']
_ARRAYJOB.oneofs_by_name['runnable'].fields.append(
  _ARRAYJOB.fields_by_name['swarm'])
_ARRAYJOB.fields_by_name['swarm'].containing_oneof = _ARRAYJOB.oneofs_by_name['runnable']
DESCRIPTOR.message_types_by_name['FutureTaskDocument'] = _FUTURETASKDOCUMENT
DESCRIPTOR.message_types_by_name['FutureTaskNode'] = _FUTURETASKNODE
DESCRIPTOR.message_types_by_name['HiveQuery'] = _HIVEQUERY
DESCRIPTOR.message_types_by_name['HiveQueryCollection'] = _HIVEQUERYCOLLECTION
DESCRIPTOR.message_types_by_name['SwarmDefinition'] = _SWARMDEFINITION
DESCRIPTOR.message_types_by_name['ArrayJob'] = _ARRAYJOB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FutureTaskDocument = _reflection.GeneratedProtocolMessageType('FutureTaskDocument', (_message.Message,), dict(
  DESCRIPTOR = _FUTURETASKDOCUMENT,
  __module__ = 'flyteidl.core.future_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.FutureTaskDocument)
  ))
_sym_db.RegisterMessage(FutureTaskDocument)

FutureTaskNode = _reflection.GeneratedProtocolMessageType('FutureTaskNode', (_message.Message,), dict(
  DESCRIPTOR = _FUTURETASKNODE,
  __module__ = 'flyteidl.core.future_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.FutureTaskNode)
  ))
_sym_db.RegisterMessage(FutureTaskNode)

HiveQuery = _reflection.GeneratedProtocolMessageType('HiveQuery', (_message.Message,), dict(
  DESCRIPTOR = _HIVEQUERY,
  __module__ = 'flyteidl.core.future_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.HiveQuery)
  ))
_sym_db.RegisterMessage(HiveQuery)

HiveQueryCollection = _reflection.GeneratedProtocolMessageType('HiveQueryCollection', (_message.Message,), dict(
  DESCRIPTOR = _HIVEQUERYCOLLECTION,
  __module__ = 'flyteidl.core.future_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.HiveQueryCollection)
  ))
_sym_db.RegisterMessage(HiveQueryCollection)

SwarmDefinition = _reflection.GeneratedProtocolMessageType('SwarmDefinition', (_message.Message,), dict(
  DESCRIPTOR = _SWARMDEFINITION,
  __module__ = 'flyteidl.core.future_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.SwarmDefinition)
  ))
_sym_db.RegisterMessage(SwarmDefinition)

ArrayJob = _reflection.GeneratedProtocolMessageType('ArrayJob', (_message.Message,), dict(
  DESCRIPTOR = _ARRAYJOB,
  __module__ = 'flyteidl.core.future_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.core.ArrayJob)
  ))
_sym_db.RegisterMessage(ArrayJob)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z0github.com/lyft/flyteidl/gen/pb-go/flyteidl/core'))
# @@protoc_insertion_point(module_scope)
