---
title: NetAdapterCx limitations
description: NetAdapterCx limitations
ms.assetid: 2333F2D9-A369-4124-9365-ABC49E8B5595
keywords:
- Network Adapter WDF Class Extension limitations, NetAdapterCx limitations, NetCx limitations
ms.author: windowsdriverdev
ms.date: 06/05/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NetAdapterCx limitations

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

This topic describes caveats you should be aware of when calling WDF functions from a NetAdapterCx client driver.

|Function | Description |
|-|-|
| [**WdfDeviceInitAssignSDDLString**](https://msdn.microsoft.com/library/windows/hardware/ff546035) | By default [**NetAdapterDeviceInitConfig**](netadapterdeviceinitconfig.md) assigns `SDDL_DEVOBJ_SYS_ALL_ADM_RWX_WORLD_RW_RES_R` as the default SDDL. If you specify a more restrictive SDDL, the application might not be able to send query OIDs to the adapter. |
|[**WdfDeviceInitSetFileObjectConfig**](https://msdn.microsoft.com/library/windows/hardware/ff546107)| The client driver must not set **WdfFileObjectWdfCanUseFsContext** in the **FileObjectClass** member of [WDF_FILEOBJECT_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff551319). |
| [**WdfDeviceInitAssignName**](https://msdn.microsoft.com/library/windows/hardware/ff546029), [**WdfDeviceInitSetReleaseHardwareOrderOnFailure**](https://msdn.microsoft.com/library/windows/hardware/hh706196), [**WdfDeviceInitSetDeviceType**](https://msdn.microsoft.com/library/windows/hardware/ff546090), [**WdfDeviceInitSetCharacteristics**](https://msdn.microsoft.com/library/windows/hardware/ff546074),  [**WdfDeviceInitSetIoType**](https://msdn.microsoft.com/library/windows/hardware/ff546128), [**WdfDeviceInitSetPowerPageable**](https://msdn.microsoft.com/library/windows/hardware/ff546766) | [**NetAdapterDeviceInitConfig**](netadapterdeviceinitconfig.md) calls these routines on behalf of the client driver. The client driver should not call these.
| [**WdfDeviceCreateDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff545935) | If the client driver calls [**WdfDeviceCreateDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff545935) with the **ReferenceString** parameter equal to **NULL**, NDIS intercepts I/O requests sent to the device interface. To avoid this behavior, specify any reference string.
