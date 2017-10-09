---
title: GUID_DISPLAY_DEVICE_ARRIVAL
description: GUID_DISPLAY_DEVICE_ARRIVAL
ms.assetid: 4915c6b0-b9a7-4602-ae43-032e20353719
keywords: ["GUID_DISPLAY_DEVICE_ARRIVAL Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DISPLAY_DEVICE_ARRIVAL
api_location:
- Ntddvdeo.h
api_type:
- HeaderDef
---

# GUID_DISPLAY_DEVICE_ARRIVAL


The GUID_DISPLAY_DEVICE_ARRIVAL [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [display adapters](https://msdn.microsoft.com/library/windows/hardware/ff554044).

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
<td align="left"><p>GUID_DISPLAY_DEVICE_ARRIVAL</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{1CA05180-A699-450A-9A0C-DE4FBE3DDD89}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied components of the [Windows Vista Display Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff570593) register instances of this device interface class to notify the operating system and applications of the presence of display adapters.

For information about the device interface class for display views that are supported by display adapters, see [**GUID_DEVINTERFACE_DISPLAY_ADAPTER**](guid-devinterface-display-adapter.md).

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
<td align="left">Ntddvdeo.h (include Ntddvdeo.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_DISPLAY_ADAPTER**](guid-devinterface-display-adapter.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_DISPLAY_DEVICE_ARRIVAL%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





