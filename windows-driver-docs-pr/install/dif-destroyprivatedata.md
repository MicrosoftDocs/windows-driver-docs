---
title: DIF_DESTROYPRIVATEDATA
description: DIF_DESTROYPRIVATEDATA
keywords: ["DIF_DESTROYPRIVATEDATA Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_DESTROYPRIVATEDATA
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DIF_DESTROYPRIVATEDATA


A DIF_DESTROYPRIVATEDATA request directs a class installer to free any memory or resources it allocated and stored in the **ClassInstallReserved** field of the [**SP_DEVINSTALL_PARAMS**](/windows/win32/api/setupapi/ns-setupapi-sp_devinstall_params_a) structure.

### When Sent

When Windows destroys a [device information set](./device-information-sets.md) or an [**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data) element, or when Windows discards its list of co-installers and class installer for a device.

### Who Handles

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Class Co-installer</p></td>
<td align="left"><p>Does not handle</p></td>
</tr>
<tr class="even">
<td align="left"><p>Device Co-installer</p></td>
<td align="left"><p>Does not handle</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Class Installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
</tbody>
</table>

 

### Installer Input

<a href="" id="deviceinfoset"></a>*DeviceInfoSet*  
Supplies a handle to a device information set.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
Optionally supplies a pointer to an [**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data) structure that identifies a device in the device information set.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
Device installation parameters ([**SP_DEVINSTALL_PARAMS**](/windows/win32/api/setupapi/ns-setupapi-sp_devinstall_params_a)) are associated with the *DeviceInfoData*, if specified, or with the *DeviceInfoSet*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
None

### Installer Output

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
An installer can clear the **ClassInstallReserved** field in the device installation parameters ([**SP_DEVINSTALL_PARAMS**](/windows/win32/api/setupapi/ns-setupapi-sp_devinstall_params_a)).

### Installer Return Value

A co-installer does not handle this DIF request. It simply returns NO_ERROR in its preprocessing pass.

A class installer typically returns ERROR_DI_DO_DEFAULT or a Win32 error code.

### Default DIF Code Handler

None

### Installer Operation

In response to a DIF_DESTROYPRIVATEDATA request a class installer frees any memory or resources it allocated and stored in the **ClassInstallReserved** field of the [**SP_DEVINSTALL_PARAMS**](/windows/win32/api/setupapi/ns-setupapi-sp_devinstall_params_a) structure.

Co-installers should not use the **ClassInstallReserved** field.

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


[**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data)

[**SP_DEVINSTALL_PARAMS**](/windows/win32/api/setupapi/ns-setupapi-sp_devinstall_params_a)

 

