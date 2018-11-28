---
title: Registering for Synchronous Driver Notification
description: Registering for Synchronous Driver Notification
ms.assetid: 852a2b69-c71f-4127-946e-8179954d504c
keywords: ["driver notification WDK dynamic hardware partitioning , registering", "synchronous notification WDK dynamic hardware partitioning , registering", "notification WDK dynamic hardware partitioning , registering", "synchronous driver notification WDK dynamic hardware partitioning , registering", "registering for driver notifications WDK dynamic hardware partitioning"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Registering for Synchronous Driver Notification


To use synchronous driver notification, a device driver implements a callback function that the operating system calls when you dynamically add a new processor to the hardware partition. The following code example is a prototype for such a callback function:

```cpp
// Prototype for the synchronous
// notification callback function
VOID
  SyncProcessorCallback(
    IN PVOID CallbackContext,
    IN PKE_PROCESSOR_CHANGE_NOTIFY_CONTEXT ChangeContext,
    IN PNTSTATUS OperationStatus
    );
```

A device driver registers for synchronous driver notification by calling the [**KeRegisterProcessorChangeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff553120) function. A device driver typically calls the **KeRegisterProcessorChangeCallback** function from within its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) function. If the device driver specifies the KE\_PROCESSOR\_CHANGE\_ADD\_EXISTING flag, the callback function is immediately called for each active processor that currently exists in the hardware partition, in addition to being called when a new processor is added to the hardware partition. The following code example shows how to register for the synchronous driver notifications:

```cpp
PVOID CallbackRegistrationHandle;
NTSTATUS CallbackStatus = STATUS_SUCCESS;

// The driver&#39;s DriverEntry routine
NTSTATUS  DriverEntry(
    PDRIVER_OBJECT DriverObject,
    PUNICODE_STRING RegistryPath
    )
{
  ...

  // Register the callback function
  CallbackRegistrationHandle =
    KeRegisterProcessorChangeCallback(
      SyncProcessorCallback,
      &CallbackStatus,
      KE_PROCESSOR_CHANGE_ADD_EXISTING
      );

  // Check the result
  if (CallbackRegistrationHandle == NULL)
  {
    // Perform any necessary cleanup
    ...

    // Check the callback status
    if (CallbackStatus != STATUS_SUCCESS)
    {
      // Return the error status from the callback function
      return CallbackStatus;
    }
    else
    {
      // Return a generic error status
      return STATUS_UNSUCCESSFUL;
    }
  }

  ...

  return STATUS_SUCCESS;
}
```

When a device driver must stop receiving synchronous driver notifications, such as when it is being unloaded, it must unregister the callback function by calling the [**KeDeregisterProcessorChangeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff552015) function. A device driver typically calls the **KeDeregisterProcessorChangeCallback** function from within its [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) function. The following code example shows how to unregister the callback function:

```cpp
// The driver&#39;s Unload routine
VOID
  Unload(
    IN PDRIVER_OBJECT DriverObject
    );
{
  ...

  // Unregister the callback function
  KeDeregisterProcessorChangeCallback(
    CallbackRegistrationHandle
    );

  ...
}
```

 

 




