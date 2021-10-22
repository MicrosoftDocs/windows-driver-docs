---
title: Setting Up ControllerControl Routines
description: Describes how a driver's DispatchPnP routine sets up a ControllerControl routine when it receives an IRP_MN_START_DEVICE request. 
keywords: ["controller objects WDK kernel , writing ControllerControl routines", "ControllerControl routines, writing", "ControllerControl routines, setting up"]
ms.date: 07/22/2021
ms.localizationpriority: medium
---

# Setting Up ControllerControl Routines

A driver's [*DispatchPnP*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine must do the following when it receives an [**IRP_MN_START_DEVICE**](./irp-mn-start-device.md) request, to set up a [*ControllerControl*](writing-controllercontrolroutines.md) routine:

1. Call [**IoCreateController**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatecontroller) to set up the controller object, specifying the driver-determined *Size* for the controller extension, which the system allocates from nonpaged pool and initializes with zeros.

1. Save the *ControllerObject* pointer returned by **IoCreateController**, usually in the device extension of each device object representing a physical or logical device that is controlled by the hardware represented by the controller object.

1. Set up and/or initialize the driver-determined contents of the *ControllerObject***->ControllerExtension**.

The returned *ControllerObject* pointer, the entry point of the driver's *ControllerControl* routine, the *DeviceObject* pointer representing the target device for the current IRP, and a *Context* pointer to an area already set up for the *ControllerControl* routine must be passed in the driver's calls to [**IoAllocateController**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioallocatecontroller). Usually, a driver's [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine sets up the area at *Context* before it calls **IoAllocateController**.
