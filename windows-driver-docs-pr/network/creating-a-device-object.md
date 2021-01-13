---
title: Creating a Device Object (Windows Filtering Platform)
description: Creating a Device Object
keywords:
- Windows Filtering Platform callout drivers WDK , initializing
- callout drivers WDK Windows Filtering Platform , initializing
- initializing callout drivers WDK Windows Filtering Platform
- device objects WDK Windows Filtering Platform
- WDM-based callout drivers WDK Windows Filtering Platform
- WDF-based callout drivers WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Device Object (Windows Filtering Platform)


A callout driver must create a device object before it can register its callouts with the filter engine. How a callout driver creates a device object depends on whether the callout driver is based on the Windows Driver Model (WDM) or the Windows Driver Frameworks (WDF).

### WDM-Based Callout Drivers

If a callout driver is based on WDM, it creates a device object by calling the [**IoCreateDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice) function. For example:

```C++
PDEVICE_OBJECT deviceObject;

NTSTATUS
 DriverEntry(
    IN PDRIVER_OBJECT DriverObject,
    IN PUNICODE_STRING RegistryPath
    )
{
  NTSTATUS status;

  ...

  // Create a device object
 status =
 IoCreateDevice(
 DriverObject,
      0,
      NULL,
      FILE_DEVICE_UNKNOWN,
      FILE_DEVICE_SECURE_OPEN,
      FALSE,
      &deviceObject
      );

  ...

 return status;
}
```

### WDF-Based Callout Drivers

If a callout driver is based on WDF, it creates a framework device object by calling the [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) function. To register its callouts with the filter engine, a WDF-based callout driver must obtain a pointer to the WDM device object that is associated with the framework device object. A WDF-based callout driver obtains a pointer to this WDM device object by calling the [**WdfDeviceWdmGetDeviceObject**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmgetdeviceobject) function. For example:

```C++
WDFDEVICE wdfDevice;

NTSTATUS
 DriverEntry(
    IN PDRIVER_OBJECT DriverObject,
    IN PUNICODE_STRING RegistryPath
    )
{
  WDFDRIVER driver;
  PWDFDEVICE_INIT deviceInit;
  PDEVICE_OBJECT deviceObject;
  NTSTATUS status;

  ...

  // Allocate a device initialization structure
 deviceInit =
 WdfControlDeviceInitAllocate(
    driver;
    &SDDL_DEVOBJ_KERNEL_ONLY
    );

  // Set the device characteristics
 WdfDeviceInitSetCharacteristics(
    deviceInit,
    FILE_DEVICE_SECURE_OPEN,
    FALSE
    );

  // Create a framework device object
 status =
 WdfDeviceCreate(
    &deviceInit,
    WDF_NO_OBJECT_ATTRIBUTES,
    &wdfDevice
    );

  // Check status
 if (status == STATUS_SUCCESS) {

    // Initialization of the framework device object is complete
    WdfControlFinishInitializing(
      wdfDevice
    );

    // Get the associated WDM device object
    deviceObject = WdfDeviceWdmGetDeviceObject(wdfDevice);
  }

  ...

 return status;
}
```

 

