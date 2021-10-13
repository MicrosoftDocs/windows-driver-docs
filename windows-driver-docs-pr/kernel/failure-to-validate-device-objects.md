---
title: Failure to Validate Device Objects
description: Failure to Validate Device Objects
keywords: ["reliability WDK kernel , device object validations", "device objects WDK kernel , validation failures", "validation failures WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Failure to Validate Device Objects





Many drivers create more than one kind of device object by calling [**IoCreateDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice). Some drivers create control device objects in their **DriverEntry** routines to allow applications to communicate with the driver, even before the driver creates an FDO. For example, file system drivers create device objects to handle file system notifications when they register themselves as file systems with **IoRegisterFileSystem**.

A driver should be ready for [**IRP\_MJ\_CREATE**](./irp-mj-create.md) requests for any device object it creates. After completing the request with a success status, the driver should expect to receive any user-accessible I/O requests on the created file object. Consequently, any driver that creates more than one device object must check which device object each I/O request specifies.

For example, suppose a driver creates overall control device objects in [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize), and then creates another set of device objects in its [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine. Suppose the *AddDevice* routine initializes the device extension with information about lower-level drivers, but the control device objects do not contain this information. In this case, all dispatch routines must be careful to check each device object that they receive. Otherwise, the driver might crash when trying to use device extension information.

 

