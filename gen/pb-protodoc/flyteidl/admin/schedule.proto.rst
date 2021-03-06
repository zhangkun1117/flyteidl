.. _api_file_flyteidl/admin/schedule.proto:

schedule.proto
=============================

.. _api_msg_flyteidl.admin.FixedRate:

flyteidl.admin.FixedRate
------------------------

`[flyteidl.admin.FixedRate proto] <https://github.com/lyft/flyteidl/blob/master/protos/flyteidl/admin/schedule.proto#L13>`_

Option for schedules run at a certain frequency, e.g. every 2 minutes.

.. code-block:: json

  {
    "value": "...",
    "unit": "..."
  }

.. _api_field_flyteidl.admin.FixedRate.value:

value
  (`uint32 <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) 
  
.. _api_field_flyteidl.admin.FixedRate.unit:

unit
  (:ref:`flyteidl.admin.FixedRateUnit <api_enum_flyteidl.admin.FixedRateUnit>`) 
  


.. _api_msg_flyteidl.admin.Schedule:

flyteidl.admin.Schedule
-----------------------

`[flyteidl.admin.Schedule proto] <https://github.com/lyft/flyteidl/blob/master/protos/flyteidl/admin/schedule.proto#L19>`_

Defines complete set of information required to trigger an execution on a schedule.

.. code-block:: json

  {
    "cron_expression": "...",
    "rate": "{...}",
    "kickoff_time_input_arg": "..."
  }

.. _api_field_flyteidl.admin.Schedule.cron_expression:

cron_expression
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) Uses AWS syntax: "Minutes Hours Day-of-month Month Day-of-week Year"
  e.g. for a schedule that runs every 15 minutes: "0/15 * * * ? *"
  
  
  
  Only one of :ref:`cron_expression <api_field_flyteidl.admin.Schedule.cron_expression>`, :ref:`rate <api_field_flyteidl.admin.Schedule.rate>` may be set.
  
.. _api_field_flyteidl.admin.Schedule.rate:

rate
  (:ref:`flyteidl.admin.FixedRate <api_msg_flyteidl.admin.FixedRate>`) 
  
  
  Only one of :ref:`cron_expression <api_field_flyteidl.admin.Schedule.cron_expression>`, :ref:`rate <api_field_flyteidl.admin.Schedule.rate>` may be set.
  
.. _api_field_flyteidl.admin.Schedule.kickoff_time_input_arg:

kickoff_time_input_arg
  (`string <https://developers.google.com/protocol-buffers/docs/proto#scalar>`_) Name of the input variable that the kickoff time will be supplied to when the workflow is kicked off.
  
  

.. _api_enum_flyteidl.admin.FixedRateUnit:

Enum flyteidl.admin.FixedRateUnit
---------------------------------

`[flyteidl.admin.FixedRateUnit proto] <https://github.com/lyft/flyteidl/blob/master/protos/flyteidl/admin/schedule.proto#L6>`_

Represents a frequency at which to run a schedule.

.. _api_enum_value_flyteidl.admin.FixedRateUnit.MINUTE:

MINUTE
  *(DEFAULT)* ⁣
  
.. _api_enum_value_flyteidl.admin.FixedRateUnit.HOUR:

HOUR
  ⁣
  
.. _api_enum_value_flyteidl.admin.FixedRateUnit.DAY:

DAY
  ⁣
  
