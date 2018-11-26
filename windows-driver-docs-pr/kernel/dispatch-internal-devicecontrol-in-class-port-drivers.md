---
title: Dispatch(Internal)DeviceControl in Class/Port Drivers
description: Dispatch(Internal)DeviceControl in Class/Port Drivers
ms.assetid: 94f6050d-c47e-4fb2-8b7f-afadcf12e0b8
keywords: ["dispatch routines WDK kernel , DispatchDeviceControl routine", "dispatch DispatchDeviceControl routine", "IRP_MJ_DEVICE_CONTROL I/O function code", "device control dispatch routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Dispatch(Internal)DeviceControl in Class/Port Drivers





The higher-level driver of a class/port pair can sometimes complete IRPs in its [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routine. For example a class driver could, during initialization, gather and store information about the features of the underlying device, which might be sought in a subsequent [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) request, and thus save processing time by satisfying the request without passing it on to the underlying device driver. A class driver might also be designed to check the IRP's parameters and send only requests with valid parameters to the port driver.

Closely coupled class/port drivers also can define a set of driver-specific or device-specific internal I/O control codes that the class driver can use for [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) requests to the port driver.

For example, the *DispatchCreateClose* routines in the system keyboard and mouse class drivers send system-defined internal device control requests to enable or disable keyboard and mouse interrupts to the underlying port drivers. These system class drivers set up **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests for an underlying port driver. Any new keyboard or mouse port driver that interoperates with these system class drivers also must support these public internal device control requests.

The system parallel class/port driver model has similar features. New parallel class drivers can get support from the system parallel port driver by setting up IRPs for **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests with public IOCTL\_PARALLEL\_PORT\_*XXX* control codes. You can replace the system parallel port driver, but any new driver also must support this set of public internal device control requests.

For more information about these public internal device control requests, see device-specific documentation in the Windows Driver Kit (WDK). For information about how to define private I/O control codes, see [Using I/O Control Codes](using-i-o-control-codes.md).

For a closely coupled pair of port/class drivers, the class driver might handle the processing of certain device control requests without passing them on to the port driver. In a new class/port driver pair, the class driver's *DispatchDeviceControl* routine can do either of the following:

-   Check the validity of the parameters in its own I/O stack location, set the I/O status block if it finds any parameter errors, and call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with a *PriorityBoost* of IO\_NO\_INCREMENT; otherwise, call [**IoGetNextIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549266) copy its own I/O stack location into the port driver's, and pass the IRP on with [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

-   Or, do nothing more than set up the port driver's I/O stack location in the IRP without checking parameters and pass it on to the port driver for processing.

SCSI class drivers have special requirements for handling device control requests. For more information about these requirements, see [Storage Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566976).

 

 




