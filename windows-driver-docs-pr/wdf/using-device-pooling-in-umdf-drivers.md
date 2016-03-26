---
title: Using Device Pooling in UMDF Drivers
description: Using Device Pooling in UMDF Drivers
ms.assetid: EC36CB33-3877-445B-8AC6-1D41E6397FF9
---

# Using Device Pooling in UMDF Drivers


## User-Mode Driver Framework (UMDF) Versions 1.11 and 2.0


If your User-Mode Driver Framework (UMDF) driver was built with version 1.11 or 2.0 and is running on Windows 8 or later, the framework creates a single instance of Wudfhost that can host multiple device stacks. This technique is called *device pooling*. The main benefit of device pooling is reduced memory consumption in an environment with multiple UMDF devices.

If a pooled device fails, the framework terminates the instance of Wudfhost and attempts to restart all of the devices that were previously in the pool. If the device fails again while pooled, the framework creates a separate Wudfhost process for the device and attempts to start the device again.

If the device fails in the separate host process, the framework attempts to restart it up to five times. The framework resets the device error count to one when thirty minutes have elapsed since the last failure.

If the system is rebooted, the framework repools devices except for those that have failed while running in a separate process.

To disable device pooling for a specific device, use the **UmdfHostProcessSharing** directive in the WDF-specific *DDInstall* section of the INF. For information about **UmdfHostProcessSharing**, see [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).

If your driver uses [direct I/O](https://msdn.microsoft.com/library/windows/hardware/ff554413), you must set **UmdfHostProcessSharing** to **ProcessSharingDisabled**. Otherwise your driver may fail to start. If **WdfDeviceIoBufferedOrDirect** is selected and the device is pooled, the framework changes the buffer access method to [buffered I/O](https://msdn.microsoft.com/library/windows/hardware/ff554413). If **WdfDeviceIoBufferedOrDirect** is selected and the device is not pooled, the framework changes the buffer access method to direct I/O.

To select a buffer access method, your driver must call the [**IWDFDeviceInitialize2::SetIoTypePreference**](https://msdn.microsoft.com/library/windows/hardware/ff556969) method from its [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) callback function. For information about access methods, see [Accessing Data Buffers in UMDF-Based Drivers](https://msdn.microsoft.com/library/windows/hardware/ff554413).

## UMDF Versions 1.9 and earlier


If your driver was built with UMDF version 1.9 or earlier, the framework creates a separate instance of the host process (Wudfhost) for each device stack.

If the device fails to start, the framework attempts to restart it up to five times. The framework resets the device error count to one when thirty minutes have elapsed since the last failure.

In a non-pooled environment, if multiple device stacks share the same UMDF driver:

-   Each device stack loads in a separate WudfHost process.
-   The framework calls the driver’s [**IDriverEntry::OnInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff554900) and [**IDriverEntry::OnDeinitialize**](https://msdn.microsoft.com/library/windows/hardware/ff554890) methods once for each device stack.
-   The framework calls the driver’s [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) method once for each device stack. Each device object is associated with a separate driver object.

In a pooled environment, if multiple device stacks share the same user mode driver:

-   Each device stack loads in the same WudfHost process.
-   The framework calls the driver’s [**IDriverEntry::OnInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff554900) and [**IDriverEntry::OnDeinitialize**](https://msdn.microsoft.com/library/windows/hardware/ff554890) methods only once.
-   The framework calls the driver’s [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) method once for each device stack. Each device object is associated with the same driver object.

Because there is only one driver object in a pooled configuration, the driver must not store any per-device context in global variables or in objects that are shared across the devices, such as the driver callback object. Instead, the driver must store per-device context in an object that is not shared between the device stacks, such as the driver’s device callback object.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Using%20Device%20Pooling%20in%20UMDF%20Drivers%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




