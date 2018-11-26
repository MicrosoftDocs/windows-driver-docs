---
title: Registering a PSHED Plug-In
description: Registering a PSHED Plug-In
ms.assetid: 8b710aa2-1477-4906-b5cb-d269d821ea28
keywords:
- platform-specific hardware error driver plug-ins WDK WHEA , registering
- registering PSHED plug-ins WDK WHEA
- PSHED plug-ins WDK WHEA , registering
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering a PSHED Plug-In


A PSHED plug-in registers itself with the PSHED by calling the [**PshedRegisterPlugin**](https://msdn.microsoft.com/library/windows/hardware/ff559466) function, passing a pointer to an initialized [**WHEA\_PSHED\_PLUGIN\_REGISTRATION\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff560617) structure. A PSHED plug-in typically calls the **PshedRegisterPlugin** function from within either its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) function or its [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) function.

A PSHED plug-in can call [**PshedIsSystemWheaEnabled**](https://msdn.microsoft.com/library/windows/hardware/ff559465) to check whether the system is WHEA-enabled before it calls **PshedRegisterPlugin**.

After a PSHED plug-in has successfully registered itself with the PSHED, it cannot be deregistered for the duration of the operating system session. Therefore, a registered PSHED plug-in must not be unloaded from the system or a bug check might occur. Therefore, PSHED plug-ins do not implement an [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) function.

The following code example demonstrates registering a PSHED plug-in that participates in error information retrieval and error record persistence.

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

// The PSHED plug-in registration packet
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
  }
}

//
// The PSHED plug-in&#39;s DriverEntry function
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

  // No unload function
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
```

 

 




