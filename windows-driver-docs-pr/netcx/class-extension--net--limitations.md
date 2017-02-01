---
title: NDIS-WDF Class Extension (Cx) Limitation
description: Due to some NetAdapterCx implementation details, certain existing WDF APIs need to be used carefully
ms.assetid: 
---

# NDIS-WDF Class Extension (Cx) Limitations

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The following WDF APIs have restrictions when used in a NetAdapterCx client driver.

|Function | Description |
|-|-|
| WdfDeviceInitAssignSDDLString | By default NetAdapterDeviceInitConfig assigns `SDDL_DEVOBJ_SYS_ALL_ADM_RWX_WORLD_RW_RES_R` as the default SDDL. Any more restrictive SDDL can have an impact on how the OS communicates with the adapter. For example, the adapter's statistics page might not be able to query the needed info |
|WdfDeviceInitSetFileObjectConfig| The client driver must not set **WdfFileObjectWdfCanUseFsContext** in the **FileObjectClass** member of [WDF_FILEOBJECT_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff551319). |
| WdfDeviceInitAssignName, WdfDeviceInitSetReleaseHardwareOrderOnFailure, WdfDeviceInitSetDeviceType, WdfDeviceInitSetCharacteristics,  WdfDeviceInitSetIoType, WdfDeviceInitSetPowerPageable | All of these APIs are called from NetAdapterDeviceInitConfig on behalf of the client driver. Calling these might result in unpredictable behavior. |
| WdfDeviceCreateDeviceInterface | If the client driver calls this API with the ReferenceString parameter equal to NULL, all the IO sent to the device interface will be intercepted by NDIS. To bypass this the client driver can specify any reference string. |
