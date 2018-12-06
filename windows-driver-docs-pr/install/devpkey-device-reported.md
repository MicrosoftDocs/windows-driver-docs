---
title: DEVPKEY_Device_Reported
description: DEVPKEY_Device_Reported
ms.assetid: dfec9e24-4d4e-42e4-a229-ad3d060fb1b5
keywords: ["DEVPKEY_Device_Reported Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_Reported
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_Reported


The DEVPKEY_Device_Reported device property represents a Boolean value that indicates whether a device instance is a root-enumerated device that the driver for the device reported to the Plug and Play (PnP) manager by calling [**IoReportDetectedDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549597).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_Reported</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-boolean.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_BOOLEAN&lt;/strong&gt;](devprop-type-boolean.md)"><strong>DEVPROP_TYPE_BOOLEAN</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The PnP manager sets the value of DEVPKEY_Device_Reported to DEVPROP_TRUE if the device is a root-enumerated device that the driver for the device reported to the PnP manager by calling IoReportDetectedDevice. Otherwise, the PnP manager sets the value of the property to DEVPROP_FALSE.

You can call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) to retrieve the value of DEVPKEY_Device_Reported.

Windows Server 2003, Windows XP, and Windows 2000 do not support this property.

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
<td align="left"><p>Available in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

## See also


[**IoReportDetectedDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549597)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

 

 






