---
title: GUID_DEVINTERFACE_PARCLASS
description: GUID_DEVINTERFACE_PARCLASS
ms.assetid: d55195d4-f4f5-464f-a1ca-5fe0eafccb2a
keywords: ["GUID_DEVINTERFACE_PARCLASS Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_PARCLASS
api_location:
- Ntddpar.h
api_type:
- HeaderDef
---

# GUID_DEVINTERFACE_PARCLASS


The GUID_DEVINTERFACE_PARCLASS [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for devices that are attached to a [parallel port](https://msdn.microsoft.com/library/windows/hardware/ff544263).

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
<td align="left"><p>GUID_DEVINTERFACE_PARCLASS</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{811FC6A5-F728-11D0-A537-0000F8753ED1}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for parallel devices that are attached to parallel ports register instances of GUID_DEVINTERFACE_PARCLASS to notify the operating system and applications of the presence of parallel devices.

The system-supplied bus driver for parallel ports creates an instance of this device interface class for each hardware device that is attached to a parallel port.

For information about parallel devices and drivers, see [Parallel Devices Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff544263).

For information about the device interface class for parallel ports, see [**GUID_DEVINTERFACE_PARALLEL**](guid-devinterface-parallel.md).

[**GUID_PARCLASS_DEVICE**](guid-parclass-device.md) is an obsolete identifier for this device interface class; for new instances of this class, use GUID_DEVINTERFACE_PARCLASS instead.

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
<td align="left"><p>Available in Microsoft Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddpar.h (include Ntddpar.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_DEVINTERFACE_PARALLEL**](guid-devinterface-parallel.md)

[**GUID_PARCLASS_DEVICE**](guid-parclass-device.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_DEVINTERFACE_PARCLASS%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





