---
title: Unloading a Callout Driver
description: Unloading a Callout Driver
ms.assetid: a8c1bb33-41f8-420c-a761-669864eb9444
keywords:
- Windows Filtering Platform callout drivers WDK , unloading
- callout drivers WDK Windows Filtering Platform , unloading
- unloading drivers WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unloading a Callout Driver


To unload a callout driver, the operating system calls the callout driver's unload function. For more information about how to specify a callout driver's unload function, see [Specifying an Unload Function](specifying-an-unload-function.md).

A callout driver's unload function guarantees that the callout driver's callouts are unregistered from the filter engine before the callout driver is unloaded from system memory. A callout driver calls either the [**FwpsCalloutUnregisterById0**](https://msdn.microsoft.com/library/windows/hardware/ff551144) function or the [**FwpsCalloutUnregisterByKey0**](https://msdn.microsoft.com/library/windows/hardware/ff551145) function to unregister a callout from the filter engine. A callout driver must not return from its unload function until after it has successfully unregistered all its callouts from the filter engine.

After a callout driver has unregistered all its callouts from the filter engine, it must delete the device object that it created before it originally registered its callouts. A callout driver that is based on the Windows Driver Model (WDM) calls the [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083) function to delete the device object. A callout driver that is based on the Windows Driver Frameworks (WDF) calls the [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) function to delete the framework device object.

A callout driver must also destroy any packet injection handle that it previously created by calling the [**FwpsInjectionHandleDestroy0**](https://msdn.microsoft.com/library/windows/hardware/ff551181) function before it returns from its unload function.

For example:

```C++
// Device object
PDEVICE_OBJECT deviceObject;

// Variable for the run-time callout identifier
UINT32 CalloutId;

// Injection handle
HANDLE injectionHandle;

// Unload function
VOID
 Unload(
    IN PDRIVER_OBJECT DriverObject
    )
{
  NTSTATUS status;

  // Unregister the callout
 status =
 FwpsCalloutUnregisterById0(
 CalloutId
      );

  // Check result
 if (status == STATUS_DEVICE_BUSY)
  {
    // For each data flow that is being processed by the
    // callout that has an associated context, clean up
    // the context and then call FwpsFlowRemoveContext0
    // to remove the context from the data flow.
    ...

    // Finish unregistering the callout
 status =
 FwpsCalloutUnregisterById0(
 CalloutId
        );
  }

  // Check status
 if (status != STATUS_SUCCESS)
  {
    // Handle error
    ...
  }

  // Delete the device object
 IoDeleteDevice(
 deviceObject
    );

  // Destroy the injection handle
 status =
 FwpsInjectionHandleDestroy0(
 injectionHandle
      );

  // Check status
 if (status != STATUS_SUCCESS)
  {
    // Handle error
    ...
  }
}
```

The previous example assumes a WDM-based callout driver. For a WDF-based callout driver, the only difference is the parameter that is passed to the callout driver's unload function and how the callout driver deletes the framework device object.

```C++
WDFDEVICE wdfDevice;

VOID
 Unload(
    IN WDFDRIVER Driver;
    )
{

  ...

  // Delete the framework device object
 WdfObjectDelete(
 wdfDevice
    );

  ...
}
```

 

 





