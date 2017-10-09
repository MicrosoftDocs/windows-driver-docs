---
title: DEVPKEY\_Numa\_Proximity\_Domain
description: DEVPKEY\_Numa\_Proximity\_Domain
ms.assetid: 384e167b-cb08-4264-a7b1-3cea2dda0d46
keywords: ["DEVPKEY_Numa_Proximity_Domain Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Numa_Proximity_Domain
api_location:
- Devpkey.h
api_type:
- HeaderDef
---

# DEVPKEY\_Numa\_Proximity\_Domain


The DEVPKEY\_Numa\_Proximity\_Domain device property represents the proximity domain of a Non-Uniform Memory Architecture (NUMA).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Numa_Proximity_Domain</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p>[<strong>DEVPROP_TYPE_INT32</strong>](devprop-type-int32.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers; read and write access by a device driver</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The value DEVPKEY\_Numa\_Proximity\_Domain is a numeric value that represents a domain ID.

Typically, the operating system sets the value of DEVPKEY\_Numa\_Proximity\_Domain by retrieving the corresponding information from system firmware.

You can retrieve the value of DEVPKEY\_Numa\_Proximity\_Domain by calling **IoSetDevicePropertyData** or **IoGetDevicePropertyData** in a device driver.

You can also call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) to retrieve the value of DEVPKEY\_Numa\_Proximity\_Domain.

The value of this property is owned by Windows and should be treated as read-only by drivers and applications.

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
<td align="left"><p>Available starting with Windows Vista.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPKEY_Numa_Proximity_Domain%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




