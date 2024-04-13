---
title: Registering a PSHED Plug-In
description: Registering a PSHED Plug-In
keywords:
- platform-specific hardware error driver plug-ins WDK WHEA , registering
- registering PSHED plug-ins WDK WHEA
- PSHED plug-ins WDK WHEA , registering
ms.date: 03/03/2023
---

# Registering a PSHED Plug-In


A PSHED plug-in registers itself with the PSHED by calling the [**PshedRegisterPlugin**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-pshedregisterplugin) function, passing a pointer to an initialized [**WHEA\_PSHED\_PLUGIN\_REGISTRATION\_PACKET**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_whea_pshed_plugin_registration_packet) structure. A PSHED plug-in typically calls the **PshedRegisterPlugin** function from within either its [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) function or its [**AddDevice**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) function.

A PSHED plug-in can call [**PshedIsSystemWheaEnabled**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-pshedissystemwheaenabled) to check whether the system is WHEA-enabled before it calls **PshedRegisterPlugin**.

There are two versions of PSHED plugins. The major difference between the two are that V2 plugins can be deregistered. After a V1 PSHED plug-in has successfully registered itself with the PSHED, it cannot be deregistered for the duration of the operating system session. Therefore, a registered PSHED plug-in must not be unloaded from the system or a bug check might occur. V2 plugins do allow deregistering. 

The following code example demonstrates registering a PSHED plug-in that participates in error information retrieval and error record persistence. Note the V1 and V2 differences.

```cpp
// Prototypes for the callback functions for
// participating in error information retrieval
NTSTATUS
  RetrieveErrorInfo(
    IN OUT PVOID  PluginContext,
    IN PWHEA_ERROR_SOURCE_DESCRIPTOR  ErrorSource,
    IN ULONG64  BufferLength,
    IN OUT PWHEA_ERROR_PACKET  Packet
    );

NTSTATUS
  FinalizeErrorRecord(
    IN OUT PVOID  PluginContext,
    IN PWHEA_ERROR_SOURCE_DESCRIPTOR  ErrorSource,
    IN ULONG  BufferLength,
    IN OUT PWHEA_ERROR_RECORD  ErrorRecord
    );

NTSTATUS
  ClearErrorStatus(
    IN OUT PVOID  PluginContext,
    IN PWHEA_ERROR_SOURCE_DESCRIPTOR  ErrorSource,
    IN ULONG  BufferLength,
    IN PWHEA_ERROR_RECORD  ErrorRecord
    );

// Prototypes for the callback functions for
// participating in error record persistence.
NTSTATUS
  WriteErrorRecord(
    IN OUT PVOID  PluginContext,
    IN ULONG  Flags,
    IN ULONG  RecordLength,
    IN PWHEA_ERROR_RECORD  ErrorRecord
    );

NTSTATUS
  ReadErrorRecord(
    IN OUT PVOID  PluginContext,
    IN ULONG  Flags,
    IN ULONGLONG  ErrorRecordId
    IN PULONGLONG  NextErrorRecordId
 IN OUT PULONG  RecordLength,
    OUT PWHEA_ERROR_RECORD  *ErrorRecord
    );

NTSTATUS
  ClearErrorRecord(
    IN OUT PVOID  PluginContext,
    IN ULONG  Flags,
    IN ULONGLONG  ErrorRecordId
    );

// The PSHED plug-in registration packet for a V1 PSHED plugin
WHEA_PSHED_PLUGIN_REGISTRATION_PACKET_V1 RegPacket =
{
  sizeof(WHEA_PSHED_PLUGIN_REGISTRATION_PACKET_V1),
 WHEA_PSHED_PLUGIN_REGISTRATION_PACKET_V1,
 NULL,
 PshedFAErrorInfoRetrieval | PshedFAErrorRecordPersistence,
  0,
  {
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    WriteErrorRecord,
    ReadErrorRecord,
    ClearErrorRecord,
    RetrieveErrorInfo,
    FinalizeErrorRecord,
    ClearErrorStatus,
    NULL,
    NULL,
    NULL
  }
}

// The PSHED plug-in registration packet for a V2 PSHED plugin
WHEA_PSHED_PLUGIN_REGISTRATION_PACKET RegPacket =
{
  sizeof(WHEA_PSHED_PLUGIN_REGISTRATION_PACKET),
 WHEA_PLUGIN_REGISTRATION_PACKET_VERSION,
 NULL,
 PshedFAErrorInfoRetrieval | PshedFAErrorRecordPersistence,
  0,
  {
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    WriteErrorRecord,
    ReadErrorRecord,
    ClearErrorRecord,
    RetrieveErrorInfo,
    FinalizeErrorRecord,
    ClearErrorStatus,
    NULL,
    NULL,
    NULL
  },
  PluginHandle
}

//
// The PSHED plug-in's DriverEntry function for a V1 PSHED Plugin
//
NTSTATUS
  DriverEntry(
    IN PDRIVER_OBJECT DriverObject,
    IN PUNICODE_STRING RegistryPath
    )
{
  BOOLEAN IsWheaEnabled;
  NTSTATUS Status;

  ...

  // No unload function for V1 PSHED plugins
  DriverObject->DriverUnload = NULL;

  // Query if the system is WHEA-enabled
  IsWheaEnabled =
    PshedIsSystemWheaEnabled(
      );

  // Check result
  if (IsWheaEnabled == FALSE)
  {
    // Return "not supported" status
    return STATUS_NOT_SUPPORTED;
  }

  // Register the PSHED plug-in
  Status =
    PshedRegisterPlugin(
      &RegPacket
      );

  // Check status
  if (Status != STATUS_SUCCESS)
  {
    // Handle error
    ...
  }

  ...

  // Return success
  return STATUS_SUCCESS;
}


//
// The PSHED plug-in's DriverEntry function for a V2 PSHED Plugin
//
NTSTATUS
  DriverEntry(
    IN PDRIVER_OBJECT DriverObject,
    IN PUNICODE_STRING RegistryPath
    )
{
  BOOLEAN IsWheaEnabled;
  NTSTATUS Status;

  ...

  // There is an unload function for V2 PSHED plugin
  DriverObject->DriverUnload = PluginUnload;

  // Query if the system is WHEA-enabled
  IsWheaEnabled =
    PshedIsSystemWheaEnabled(
      );

  // Check result
  if (IsWheaEnabled == FALSE)
  {
    // Return "not supported" status
    return STATUS_NOT_SUPPORTED;
  }

  // Register the PSHED plug-in
  Status =
    PshedRegisterPlugin(
      &RegPacket
      );

  // Check status
  if (Status != STATUS_SUCCESS)
  {
    // Handle error
    ...
  }

  ...

  // Return success
  return STATUS_SUCCESS;
}
```
