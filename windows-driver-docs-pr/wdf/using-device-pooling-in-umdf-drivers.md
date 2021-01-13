---
title: Using Device Pooling in UMDF Drivers
description: Using Device Pooling in UMDF Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Device Pooling in UMDF Drivers


## User-Mode Driver Framework (UMDF) Versions 1.11 and 2.0


If your User-Mode Driver Framework (UMDF) driver was built with version 1.11 or 2.0 and is running on Windows 8 or later, the framework creates a single instance of Wudfhost that can host multiple device stacks. This technique is called *device pooling*. The main benefit of device pooling is reduced memory consumption in an environment with multiple UMDF devices.

If a pooled device fails, the framework terminates the instance of Wudfhost and attempts to restart all of the devices that were previously in the pool. If the device fails again while pooled, the framework creates a separate Wudfhost process for the device and attempts to start the device again.

If the device fails in the separate host process, the framework attempts to restart it up to five times. The framework resets the device error count to one when thirty minutes have elapsed since the last failure.

If the system is rebooted, the framework repools devices except for those that have failed while running in a separate process.

To disable device pooling for a specific device, use the **UmdfHostProcessSharing** directive in the WDF-specific *DDInstall* section of the INF. For information about **UmdfHostProcessSharing**, see [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).

If your driver uses [direct I/O](./accessing-data-buffers-in-umdf-1-x-drivers.md), you must set **UmdfHostProcessSharing** to **ProcessSharingDisabled**. Otherwise your driver may fail to start. If **WdfDeviceIoBufferedOrDirect** is selected and the device is pooled, the framework changes the buffer access method to [buffered I/O](./accessing-data-buffers-in-umdf-1-x-drivers.md). If **WdfDeviceIoBufferedOrDirect** is selected and the device is not pooled, the framework changes the buffer access method to direct I/O.

To select a buffer access method, your driver must call the [**IWDFDeviceInitialize2::SetIoTypePreference**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdeviceinitialize2-setiotypepreference) method from its [**IDriverEntry::OnDeviceAdd**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) callback function. For information about access methods, see [Accessing Data Buffers in UMDF-Based Drivers](./accessing-data-buffers-in-umdf-1-x-drivers.md).

## UMDF Versions 1.9 and earlier


If your driver was built with UMDF version 1.9 or earlier, the framework creates a separate instance of the host process (Wudfhost) for each device stack.

If the device fails to start, the framework attempts to restart it up to five times. The framework resets the device error count to one when thirty minutes have elapsed since the last failure.

In a non-pooled environment, if multiple device stacks share the same UMDF driver:

-   Each device stack loads in a separate WudfHost process.
-   The framework calls the driver’s [**IDriverEntry::OnInitialize**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-oninitialize) and [**IDriverEntry::OnDeinitialize**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeinitialize) methods once for each device stack.
-   The framework calls the driver’s [**IDriverEntry::OnDeviceAdd**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) method once for each device stack. Each device object is associated with a separate driver object.

In a pooled environment, if multiple device stacks share the same user mode driver:

-   Each device stack loads in the same WudfHost process.
-   The framework calls the driver’s [**IDriverEntry::OnInitialize**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-oninitialize) and [**IDriverEntry::OnDeinitialize**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeinitialize) methods only once.
-   The framework calls the driver’s [**IDriverEntry::OnDeviceAdd**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) method once for each device stack. Each device object is associated with the same driver object.

Because there is only one driver object in a pooled configuration, the driver must not store any per-device context in global variables or in objects that are shared across the devices, such as the driver callback object. Instead, the driver must store per-device context in an object that is not shared between the device stacks, such as the driver’s device callback object.

 

