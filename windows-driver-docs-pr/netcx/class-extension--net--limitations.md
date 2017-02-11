---
title: NDIS-WDF Class Extension (Cx) Limitation
---

# NDIS-WDF Class Extension (Cx) Limitations

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The following WDF APIs have restrictions when used in a NetAdapterCx client driver.

|Function | Description |
|-|-|
| [**WdfDeviceInitAssignSDDLString**](https://msdn.microsoft.com/library/windows/hardware/ff546035) | By default NetAdapterDeviceInitConfig assigns `SDDL_DEVOBJ_SYS_ALL_ADM_RWX_WORLD_RW_RES_R` as the default SDDL. Any more restrictive SDDL can have an impact on how the OS communicates with the adapter. For example, the application might not be able to send query OIDs to the adapter. |
|[**WdfDeviceInitSetFileObjectConfig**](https://msdn.microsoft.com/library/windows/hardware/ff546107)| The client driver must not set **WdfFileObjectWdfCanUseFsContext** in the **FileObjectClass** member of [WDF_FILEOBJECT_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff551319). |
| [**WdfDeviceInitAssignName**](https://msdn.microsoft.com/library/windows/hardware/ff546029), [**WdfDeviceInitSetReleaseHardwareOrderOnFailure**](https://msdn.microsoft.com/library/windows/hardware/hh706196), [**WdfDeviceInitSetDeviceType**](https://msdn.microsoft.com/library/windows/hardware/ff546090), [**WdfDeviceInitSetCharacteristics**](https://msdn.microsoft.com/library/windows/hardware/ff546074),  [**WdfDeviceInitSetIoType**](https://msdn.microsoft.com/library/windows/hardware/ff546128), [**WdfDeviceInitSetPowerPageable**](https://msdn.microsoft.com/library/windows/hardware/ff546766) | All of these APIs are called from NetAdapterDeviceInitConfig on behalf of the client driver. Calling these might result in unpredictable behavior. |
| [**WdfDeviceCreateDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff545935) | If the client driver calls this API with the ReferenceString parameter equal to NULL, all the IO sent to the device interface will be intercepted by NDIS. To bypass this the client driver can specify any reference string. |
