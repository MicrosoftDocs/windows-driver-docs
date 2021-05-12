---
title: NetAdapterCx limitations
description: NetAdapterCx limitations
keywords:
- Network Adapter WDF Class Extension limitations, NetAdapterCx limitations, NetCx limitations
ms.date: 06/05/2017
ms.localizationpriority: medium
---

# NetAdapterCx limitations

This topic describes caveats you should be aware of when calling WDF functions from a NetAdapterCx client driver.

|Function | Description |
|-|-|
| [**WdfDeviceInitAssignSDDLString**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitassignsddlstring) | By default [**NetAdapterDeviceInitConfig**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterdeviceinitconfig) assigns `SDDL_DEVOBJ_SYS_ALL_ADM_RWX_WORLD_RW_RES_R` as the default SDDL. If you specify a more restrictive SDDL, the application might not be able to send query OIDs to the adapter. |
|[**WdfDeviceInitSetFileObjectConfig**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetfileobjectconfig)| The client driver must not set **WdfFileObjectWdfCanUseFsContext** in the **FileObjectClass** member of [WDF_FILEOBJECT_CONFIG](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_fileobject_config). |
| [**WdfDeviceInitAssignName**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitassignname), [**WdfDeviceInitSetReleaseHardwareOrderOnFailure**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetreleasehardwareorderonfailure), [**WdfDeviceInitSetDeviceType**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetdevicetype), [**WdfDeviceInitSetCharacteristics**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetcharacteristics),  [**WdfDeviceInitSetIoType**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetiotype), [**WdfDeviceInitSetPowerPageable**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerpageable) | [**NetAdapterDeviceInitConfig**](/windows-hardware/drivers/ddi/netadapter/nf-netadapter-netadapterdeviceinitconfig) calls these routines on behalf of the client driver. The client driver should not call these.
| [**WdfDeviceCreateDeviceInterface**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreatedeviceinterface) | If the client driver calls [**WdfDeviceCreateDeviceInterface**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreatedeviceinterface) with the **ReferenceString** parameter equal to **NULL**, NDIS intercepts I/O requests sent to the device interface. To avoid this behavior, specify any reference string.
