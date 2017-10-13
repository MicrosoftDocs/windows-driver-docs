---
title: GUID_DEVICE_BATTERY
description: GUID_DEVICE_BATTERY
ms.assetid: 8391b167-0d17-46bf-9320-4fceed54aead
keywords: ["GUID_DEVICE_BATTERY Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVICE_BATTERY
api_location:
- Batclass.h
api_type:
- HeaderDef
---

# GUID_DEVICE_BATTERY


The GUID_DEVICE_BATTERY [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [battery devices](https://msdn.microsoft.com/library/windows/hardware/ff536281).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Attribute</th>
<th align="left">Setting</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Identifier</p></td>
<td align="left"><p>GUID_DEVICE_BATTERY</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{72631E54-78A4-11D0-BCF7-00AA00B7B32A}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied [battery class driver](https://msdn.microsoft.com/library/windows/hardware/ff536278) registers an instance of this device interface class for a battery device on behalf of a battery miniclass driver.

For information about battery devices and drivers, see [Overview of System Battery Management](https://msdn.microsoft.com/library/windows/hardware/ff536300).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Batclass.h (include Batclass.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_DEVICE_BATTERY%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




