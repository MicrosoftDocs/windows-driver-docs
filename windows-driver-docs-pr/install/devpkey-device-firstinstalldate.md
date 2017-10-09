---
title: DEVPKEY\_Device\_FirstInstallDate
description: DEVPKEY\_Device\_FirstInstallDate
ms.assetid: aedc4f18-51be-4c42-a172-c1fd88cc49b3
keywords: ["DEVPKEY_Device_FirstInstallDate Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_FirstInstallDate
api_location:
- Devpkey.h
api_type:
- HeaderDef
---

# DEVPKEY\_Device\_FirstInstallDate


The DEVPKEY\_Device\_FirstInstallDate device property specifies the time stamp when the device instance was first installed in the system.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_FirstInstallDate</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p>[<strong>DEVPROP_TYPE_FILETIME</strong>](devprop-type-filetime.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Windows sets the value of DEVPKEY\_Device\_FirstInstallDate with the time stamp that specifies when the device instance was first installed in the system.

**Note**   Unlike the [**DEVPKEY\_Device\_InstallDate**](devpkey-device-installdate.md) property, the value of the DEVPKEY\_Device\_FirstInstallDate property does not change with each successive update of the device driver. For example, a driver that was updated through Windows Update does not change the value of this property,

 

You can call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) to retrieve the value of DEVPKEY\_Device\_FirstInstallDate property.

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
<td align="left"><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

## See also


[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPKEY_Device_FirstInstallDate%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





