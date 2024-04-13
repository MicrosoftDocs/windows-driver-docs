---
title: Finding and Mapping Hardware Resources
description: This topic describes how a Kernel-Mode Driver Framework (KMDF) driver or User-Mode Driver Framework (UMDF) driver starting in version 2 maps a translated memory resource (CmResourceTypeMemory) that it receives in its EvtDevicePrepareHardware callback function.
ms.date: 04/20/2017
---

# Finding and Mapping Hardware Resources


This topic describes how a Kernel-Mode Driver Framework (KMDF) driver or User-Mode Driver Framework (UMDF) driver starting in version 2 maps a translated memory resource (**CmResourceTypeMemory**) that it receives in its [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback function.

A UMDF 1.x driver can also receive this type of resource in its [**IPnpCallbackHardware2::OnPrepareHardware**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardware2-onpreparehardware) method. For more info, see [Finding and Mapping Hardware Resources in UMDF 1.x Drivers](finding-and-mapping-hardware-resources-in-umdf-1-x-drivers.md).

Your driver receives [raw and translated](raw-and-translated-resources.md) versions of hardware resources in the device's resource list in its [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback function. The driver can save the resource list, which is valid until the framework calls the driver's [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) callback function.

Typically, the driver calls [**WdfCmResourceListGetCount**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfcmresourcelistgetcount) from its [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback function to determine the number of resource descriptors in the translated resource list, and then calls [**WdfCmResourceListGetDescriptor**](/windows-hardware/drivers/ddi/wdfresource/nf-wdfresource-wdfcmresourcelistgetdescriptor) in a loop to identify memory-mapped registers, I/O ports, and interrupts.

If a driver is assigned a translated memory resource (**CmResourceTypeMemory**), it must map the physical address into an address through which it can access device registers.

A KMDF driver calls [**MmMapIoSpace**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmapiospace) to map the given physical address range to nonpaged system space. Then it uses the [**HAL Library Routines**](/previous-versions/windows/hardware/drivers/ff546644(v=vs.85)) to read and write to registers.

A UMDF driver calls [**WdfDeviceMapIoSpace**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicemapiospace) to map the physical address to a pseudo base address that it can use in conjunction with [WDF Register/Port Access Functions](/windows-hardware/drivers/ddi/wdfhwaccess/) to read and write to registers and ports.

The driver unmaps the resources by calling [**MmUnmapIoSpace**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunmapiospace) or [**WdfDeviceUnmapIoSpace**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceunmapiospace) from its [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) callback function.

You do not need to map resources in I/O space (**CmResourceTypePort**, **CmResourceTypeInterrupt**, **CmResourceTypeDma**).

If your UMDF driver calls [**WdfDeviceMapIoSpace**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicemapiospace), you must set the **UmdfDirectHardwareAccess** INF directive to **AllowDirectHardwareAccess**.

For an example that shows how a driver finds and maps memory-mapped register resources, see [Reading and Writing to Device Registers](reading-and-writing-to-device-registers.md).

 

