---
title: DIF_POWERMESSAGEWAKE
description: DIF_POWERMESSAGEWAKE
ms.assetid: 73f6e763-0900-4297-ac88-20bbb3ac424d
keywords: ["DIF_POWERMESSAGEWAKE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_POWERMESSAGEWAKE
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DIF_POWERMESSAGEWAKE


A DIF_POWERMESSAGEWAKE request allows an installer to supply custom text that Windows displays on the power management properties page of the device properties.

### When Sent

When a user clicks on a menu item or tab to display the properties of a device.

Windows only sends this DIF request if the drivers for the device support power management. Otherwise, Windows does not display any power properties for the device.

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
Supplies a handle to the [device information set](https://msdn.microsoft.com/library/windows/hardware/ff541247) that contains the device.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
Supplies a pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that identifies the device in the device information set.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters ([**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)) associated with the *DeviceInfoData*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An [**SP_POWERMESSAGEWAKE_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553311) structure is associated with the *DeviceInfoData*.

### Installer Output

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An installer can modify the [**SP_POWERMESSAGEWAKE_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553311) to supply custom text for a device's power properties page.

### Installer Return Value

A co-installer typically returns NO_ERROR, ERROR_DI_POSTPROCESSING_REQUIRED, or a Win32 error code.

A class installer returns NO_ERROR if it successfully supplies power properties text. Otherwise, a class installer returns ERROR_DI_DO_DEFAULT or a Win32 error code.

### Default DIF Code Handler

None

### Installer Operation

A DIF_POWERMESSAGEWAKE request allows an installer to supply text that Windows displays on the power properties page for a device.

If a co-installer supplies power-properties text, it should do so in its postprocessing phase. A co-installer should be careful when overwriting any power-properties text supplied by an installer that handled the request before the co-installer.

For more information about DIF codes, see [Handling DIF Codes](https://msdn.microsoft.com/library/windows/hardware/ff546094).

Requirements
------------

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


[**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

[**SP_POWERMESSAGEWAKE_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553311)

 

 






