---
title: NetAdapterCx limitations
description: NetAdapterCx limitations
ms.assetid: 2333F2D9-A369-4124-9365-ABC49E8B5595
keywords:
- Network Adapter WDF Class Extension limitations, NetAdapterCx limitations, NetCx limitations
ms.date: 06/05/2017
ms.localizationpriority: medium
---

# NetAdapterCx limitations

This topic describes caveats you should be aware of when calling WDF functions from a NetAdapterCx client driver.

|Function | Description |
|-|-|
| [**WdfDeviceInitAssignSDDLString**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceinitassignsddlstring) | By default [**NetAdapterDeviceInitConfig**](https://review.docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadapterdeviceinitconfig) assigns `SDDL_DEVOBJ_SYS_ALL_ADM_RWX_WORLD_RW_RES_R` as the default SDDL. If you specify a more restrictive SDDL, the application might not be able to send query OIDs to the adapter. |
|[**WdfDeviceInitSetFileObjectConfig**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceinitsetfileobjectconfig)| The client driver must not set **WdfFileObjectWdfCanUseFsContext** in the **FileObjectClass** member of [WDF_FILEOBJECT_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/ns-wdfdevice-_wdf_fileobject_config). |
| [**WdfDeviceInitAssignName**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceinitassignname), [**WdfDeviceInitSetReleaseHardwareOrderOnFailure**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceinitsetreleasehardwareorderonfailure), [**WdfDeviceInitSetDeviceType**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceinitsetdevicetype), [**WdfDeviceInitSetCharacteristics**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceinitsetcharacteristics),  [**WdfDeviceInitSetIoType**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceinitsetiotype), [**WdfDeviceInitSetPowerPageable**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerpageable) | [**NetAdapterDeviceInitConfig**](https://review.docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadapterdeviceinitconfig) calls these routines on behalf of the client driver. The client driver should not call these.
| [**WdfDeviceCreateDeviceInterface**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreatedeviceinterface) | If the client driver calls [**WdfDeviceCreateDeviceInterface**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreatedeviceinterface) with the **ReferenceString** parameter equal to **NULL**, NDIS intercepts I/O requests sent to the device interface. To avoid this behavior, specify any reference string.
