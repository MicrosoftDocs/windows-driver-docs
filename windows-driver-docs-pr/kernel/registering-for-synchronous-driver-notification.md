---
title: Registering for Synchronous Driver Notification
author: windows-driver-content
description: Registering for Synchronous Driver Notification
ms.assetid: 852a2b69-c71f-4127-946e-8179954d504c
keywords: ["driver notification WDK dynamic hardware partitioning , registering", "synchronous notification WDK dynamic hardware partitioning , registering", "notification WDK dynamic hardware partitioning , registering", "synchronous driver notification WDK dynamic hardware partitioning , registering", "registering for driver notifications WDK dynamic hardware partitioning"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Registering for Synchronous Driver Notification


To use synchronous driver notification, a device driver implements a callback function that the operating system calls when you dynamically add a new processor to the hardware partition. The following code example is a prototype for such a callback function:

```
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

```
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
      &amp;CallbackStatus,
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Registering%20for%20Synchronous%20Driver%20Notification%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


