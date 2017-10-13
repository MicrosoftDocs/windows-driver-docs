---
title: Dispatch(Internal)DeviceControl in Class/Port Drivers
author: windows-driver-content
description: Dispatch(Internal)DeviceControl in Class/Port Drivers
ms.assetid: 94f6050d-c47e-4fb2-8b7f-afadcf12e0b8
keywords: ["dispatch routines WDK kernel , DispatchDeviceControl routine", "dispatch DispatchDeviceControl routine", "IRP_MJ_DEVICE_CONTROL I/O function code", "device control dispatch routines WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Dispatch(Internal)DeviceControl in Class/Port Drivers


## <a href="" id="ddk-dispatch-internal-devicecontrol-in-class-port-drivers-kg"></a>


The higher-level driver of a class/port pair can sometimes complete IRPs in its [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routine. For example a class driver could, during initialization, gather and store information about the features of the underlying device, which might be sought in a subsequent [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) request, and thus save processing time by satisfying the request without passing it on to the underlying device driver. A class driver might also be designed to check the IRP's parameters and send only requests with valid parameters to the port driver.

Closely coupled class/port drivers also can define a set of driver-specific or device-specific internal I/O control codes that the class driver can use for [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) requests to the port driver.

For example, the *DispatchCreateClose* routines in the system keyboard and mouse class drivers send system-defined internal device control requests to enable or disable keyboard and mouse interrupts to the underlying port drivers. These system class drivers set up **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests for an underlying port driver. Any new keyboard or mouse port driver that interoperates with these system class drivers also must support these public internal device control requests.

The system parallel class/port driver model has similar features. New parallel class drivers can get support from the system parallel port driver by setting up IRPs for **IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL** requests with public IOCTL\_PARALLEL\_PORT\_*XXX* control codes. You can replace the system parallel port driver, but any new driver also must support this set of public internal device control requests.

For more information about these public internal device control requests, see device-specific documentation in the Windows Driver Kit (WDK). For information about how to define private I/O control codes, see [Using I/O Control Codes](using-i-o-control-codes.md).

For a closely coupled pair of port/class drivers, the class driver might handle the processing of certain device control requests without passing them on to the port driver. In a new class/port driver pair, the class driver's *DispatchDeviceControl* routine can do either of the following:

-   Check the validity of the parameters in its own I/O stack location, set the I/O status block if it finds any parameter errors, and call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) with a *PriorityBoost* of IO\_NO\_INCREMENT; otherwise, call [**IoGetNextIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549266) copy its own I/O stack location into the port driver's, and pass the IRP on with [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

-   Or, do nothing more than set up the port driver's I/O stack location in the IRP without checking parameters and pass it on to the port driver for processing.

SCSI class drivers have special requirements for handling device control requests. For more information about these requirements, see [Storage Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566976).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Dispatch%28Internal%29DeviceControl%20in%20Class/Port%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


