---
title: Required Dispatch Routines
author: windows-driver-content
description: Required Dispatch Routines
ms.assetid: 9b760ac7-7f31-47ad-bf84-7d79c6b24ebd
keywords: ["dispatch routines WDK kernel , required", "required dispatch routines WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Required Dispatch Routines


## <a href="" id="ddk-required-dispatch-routines-kg"></a>


Most drivers must handle the following *Dispatch* routines:

-   [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341)

    [**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772) indicates a request involving PnP device recognition, hardware configuration, or resource allocation. Such requests are typically sent to a device driver from the PnP manager or from a closely coupled higher-level driver.

-   [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354)

    [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784) indicates a request pertaining to the power state of either the device or the system. Such requests are sent to the device driver by either the power manager or a closely coupled higher-level driver.

-   [*DispatchCreate*](https://msdn.microsoft.com/library/windows/hardware/ff543266)

    [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729) indicates either that a user-mode protected subsystem, possibly on behalf of an application or subsystem-specific driver, has requested a handle for the file object associated with the target device object, or that a higher-level driver is connecting or attaching its device object to the target device object.

-   [*DispatchClose*](https://msdn.microsoft.com/library/windows/hardware/ff543255)

    [**IRP\_MJ\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/ff550720) indicates that the last handle of the file object that was associated the target device object has been closed and released. All I/O requests have been completed or canceled, so there are no outstanding references to the file object pointer.

-   [*DispatchRead*](https://msdn.microsoft.com/library/windows/hardware/ff543376)

    [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) indicates an I/O request to transfer data from the underlying physical device to the system.

-   [*DispatchWrite*](https://msdn.microsoft.com/library/windows/hardware/ff544034)

    [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819) indicates an I/O request to transfer data from the system to the underlying physical device.

-   [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287)

    [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) indicates a request that contains a system-defined, device-type-specific I/O control code specifying a device type-specific operation. Higher-level drivers pass these IRPs on to their underlying device drivers, which typically process the request by accessing the device.

-   [*DispatchInternalDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543326)

    [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) indicates a request sent to the device driver, in most cases from a closely coupled higher-level driver, usually with a privately defined, driver-specific and device-type-specific or device-specific I/O control code requesting a device-type-specific or device-specific operation.

    Only certain kinds of drivers are required to handle system-defined internal device I/O control requests, including certain SCSI drivers, keyboard or mouse device drivers, and parallel drivers that interoperate with system-supplied drivers.

-   [*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412)

    [**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813) is used to specify WMI requests to drivers. For more information about WMI, see [Windows Management Instrumentation](implementing-wmi.md).

The dispatch routines that a driver must provide vary according to the type and functionality of the underlying physical device. For device-type-specific information about IRP major function codes that drivers must handle, see the device-type specific documentation in the Windows Driver Kit (WDK).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Required%20Dispatch%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


