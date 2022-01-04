---
title: Specifying an Unload Function
description: Specifying an Unload Function
keywords:
- Windows Filtering Platform callout drivers WDK , initializing
- callout drivers WDK Windows Filtering Platform , initializing
- initializing callout drivers WDK Windows Filtering Platform
- WDM-based callout drivers WDK Windows Filtering Platform
- WDF-based callout drivers WDK Windows Filtering Platform
- unload function WDK Windows Filtering Platform
ms.date: 04/20/2017
---

# Specifying an Unload Function


A callout driver must provide an unload function. The operating system calls this function when the callout driver is unloaded from the system. A callout driver's unload function must guarantee that the callout driver's callouts are unregistered from the filter engine before the callout driver is unloaded from system memory. A callout driver cannot be unloaded from the system if it does not provide an unload function.

How a callout driver specifies an unload function depends on whether the callout driver is based on the Windows Driver Model (WDM) or the Windows Driver Frameworks (WDF).

### WDM-Based Callout Drivers

If a callout driver is based on WDM, it specifies an [**Unload**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) function in its [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) function. For example:

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

If a callout driver is based on WDF, it specifies an [*EvtDriverUnload*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_unload) function in its [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) function. For example:

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

 

