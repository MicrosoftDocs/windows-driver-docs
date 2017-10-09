---
title: KSCATEGORY_PREFERRED_MIDIOUT_DEVICE
description: KSCATEGORY_PREFERRED_MIDIOUT_DEVICE
ms.assetid: b3d93d21-d4f8-4f00-9947-034790f3f7b1
keywords: ["KSCATEGORY_PREFERRED_MIDIOUT_DEVICE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_PREFERRED_MIDIOUT_DEVICE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSCATEGORY_PREFERRED_MIDIOUT_DEVICE


The KSCATEGORY_PREFERRED_MIDIOUT_DEVICE [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff568277) (KS) functional category for the preferred MIDI output device.

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
<td align="left"><p>KSCATEGORY_PREFERRED_WAVEOUT_DEVICE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{D6C50674-72C1-11D2-9755-0000F8004788}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

A user selects the preferred MIDI output device in the Multimedia property pages in the Control Panel.

This functional category is reserved for exclusive use by the system-supplied [WDM Audio Components](https://msdn.microsoft.com/library/windows/hardware/ff538905).

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
<td align="left"><p>Available in Windows Server 2003, Windows XP, Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20KSCATEGORY_PREFERRED_MIDIOUT_DEVICE%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




