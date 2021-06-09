---
title: DIF_UNREMOVE
description: DIF_UNREMOVE
keywords: ["DIF_UNREMOVE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_UNREMOVE
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DIF_UNREMOVE


A DIF_UNREMOVE request notifies the installer that Windows is about to reinstate a device in a given hardware profile and gives the installer an opportunity to participate in the operation. Windows only sends this request for non-PnP devices.

### When Sent

When a root-enumerated, non-PnP device is reinstated to a hardware profile.

### Who Handles

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Class Co-installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
<tr class="even">
<td align="left"><p>Device Co-installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Class Installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
</tbody>
</table>

 

### Installer Input

<a href="" id="deviceinfoset"></a>*DeviceInfoSet*  
Supplies a handle to the [device information set](./device-information-sets.md) that contains the device.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
Supplies a pointer to an [**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data) structure that identifies the device in the device information set.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters ([**SP_DEVINSTALL_PARAMS**](/windows/win32/api/setupapi/ns-setupapi-sp_devinstall_params_a)) associated with the *DeviceInfoData*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An [**SP_UNREMOVEDEVICE_PARAMS**](/windows/win32/api/setupapi/ns-setupapi-sp_unremovedevice_params) structure is associated with the *DeviceInfoData*. The **Scope** field must be set to DI_UNREMOVEDEVICE_CONFIGSPECIFIC and a hardware profile must be specified in the **HwProfile** field.

### Installer Output

<a href="" id="none"></a>None  

### Installer Return Value

A co-installer can return NO_ERROR, ERROR_DI_POSTPROCESSING_REQUIRED, or a Win32 error code.

If a class installer successfully handles this request and [**SetupDiCallClassInstaller**](/windows/win32/api/setupapi/nf-setupapi-setupdicallclassinstaller) should subsequently call the default handler, the class installer returns ERROR_DI_DO_DEFAULT.

If the class installer successfully handles this request, including directly calling the default handler, the class installer should return NO_ERROR and **SetupDiCallClassInstaller** will not subsequently call the default handler again.

**Note**   The class installer can directly call the default handler, but the class installer should never attempt to supersede the operations of the default handler.

 

For more information about calling the default handler, see [Calling Default DIF Code Handlers](./calling-the-default-dif-code-handlers.md).

If the class installer encounters an error, the installer should return an appropriate Win32 error code and **SetupDiCallClassInstaller** will not subsequently call the default handler.

### Default DIF Code Handler

[**SetupDiUnremoveDevice**](/windows/win32/api/setupapi/nf-setupapi-setupdiunremovedevice)

### Installer Operation

"Unremoving" a device basically means that Windows clears a flag that previously marked a device as "not present" in a particular hardware profile.

For more information about DIF codes, see [Handling DIF Codes](./handling-dif-codes.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Supported in Microsoft Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Setupapi.h (include Setupapi.h)</td>
</tr>
</tbody>
</table>

## See also


[**SetupDiUnremoveDevice**](/windows/win32/api/setupapi/nf-setupapi-setupdiunremovedevice)

[**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data)

[**SP_DEVINSTALL_PARAMS**](/windows/win32/api/setupapi/ns-setupapi-sp_devinstall_params_a)

[**SP_UNREMOVEDEVICE_PARAMS**](/windows/win32/api/setupapi/ns-setupapi-sp_unremovedevice_params)

 

