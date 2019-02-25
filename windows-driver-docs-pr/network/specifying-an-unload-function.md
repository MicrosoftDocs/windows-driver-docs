---
title: Specifying an Unload Function
description: Specifying an Unload Function
ms.assetid: 3bfac8a5-1367-40bd-81b5-4a7fb9aaaece
keywords:
- Windows Filtering Platform callout drivers WDK , initializing
- callout drivers WDK Windows Filtering Platform , initializing
- initializing callout drivers WDK Windows Filtering Platform
- WDM-based callout drivers WDK Windows Filtering Platform
- WDF-based callout drivers WDK Windows Filtering Platform
- unload function WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying an Unload Function


A callout driver must provide an unload function. The operating system calls this function when the callout driver is unloaded from the system. A callout driver's unload function must guarantee that the callout driver's callouts are unregistered from the filter engine before the callout driver is unloaded from system memory. A callout driver cannot be unloaded from the system if it does not provide an unload function.

How a callout driver specifies an unload function depends on whether the callout driver is based on the Windows Driver Model (WDM) or the Windows Driver Frameworks (WDF).

### WDM-Based Callout Drivers

If a callout driver is based on WDM, it specifies an [**Unload**](https://msdn.microsoft.com/library/windows/hardware/ff564886) function in its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) function. For example:

```C++
VOID
 Unload(
    IN PDRIVER_OBJECT DriverObject
    );

NTSTATUS
 DriverEntry(
    IN PDRIVER_OBJECT DriverObject,
    IN PUNICODE_STRING RegistryPath
    )
{
  ...

  // Specify the callout driver's Unload function
 DriverObject->DriverUnload = Unload;

  ...
}
```

### WDF-Based Callout Drivers

If a callout driver is based on WDF, it specifies an [*EvtDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff541694) function in its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) function. For example:

```C++
VOID
 Unload(
    IN WDFDRIVER Driver
    );

NTSTATUS
 DriverEntry(
    IN PDRIVER_OBJECT DriverObject,
    IN PUNICODE_STRING RegistryPath
    )
{
  NTSTATUS status;
  WDF_DRIVER_CONFIG config;
  WDFDRIVER driver;

  ...

  // Initialize the driver config structure
  WDF_DRIVER_CONFIG_INIT(&config, NULL);

  // Indicate that this is a non-PNP driver
 config.DriverInitFlags = WdfDriverInitNonPnpDriver;

  // Specify the callout driver's Unload function
 config.EvtDriverUnload = Unload;

  // Create a WDFDRIVER object
 status =
 WdfDriverCreate(
 DriverObject,
 RegistryPath,
      NULL,
      &config,
      &driver
      );

  ...

 return status;
}
```

For information about how to implement a callout driver's unload function, see [Unloading a Callout Driver](unloading-a-callout-driver.md).

 

 





