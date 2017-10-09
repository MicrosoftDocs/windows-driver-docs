---
title: GUID\_DEVINTERFACE\_PARALLEL
description: GUID\_DEVINTERFACE\_PARALLEL
ms.assetid: 3c7c27ba-aad6-4ca5-ba26-fba206f967b9
keywords: ["GUID_DEVINTERFACE_PARALLEL Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_PARALLEL
api_location:
- Ntddpar.h
api_type:
- HeaderDef
---

# GUID\_DEVINTERFACE\_PARALLEL


The GUID\_DEVINTERFACE\_PARALLEL [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [parallel ports](https://msdn.microsoft.com/library/windows/hardware/ff544263) that support an IEEE 1284-compatible hardware interface.

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
<td align="left"><p>GUID_DEVINTERFACE_PARALLEL</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{97F76EF0-F883-11D0-AF1F-0000F800845C}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for parallel ports register instances of GUID\_DEVINTERFACE\_PARALLEL to notify the operating system and applications of the presence of parallel ports.

The system-supplied function driver for parallel ports registers an instance of this device class for a parallel port.

For information about parallel devices and drivers, see [Introduction to Parallel Ports and Devices](https://msdn.microsoft.com/library/windows/hardware/ff543964).

For information about the device interface class for devices that are attached to a parallel port, see [**GUID\_DEVINTERFACE\_PARCLASS**](guid-devinterface-parclass.md).

[**GUID\_PARALLEL\_DEVICE**](guid-parallel-device.md) is an obsolete identifier for this device interface class; for new instances of this class, use GUID\_DEVINTERFACE\_PARALLEL instead.

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


[**GUID\_DEVINTERFACE\_PARCLASS**](guid-devinterface-parclass.md)

[**GUID\_PARALLEL\_DEVICE**](guid-parallel-device.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_DEVINTERFACE_PARALLEL%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





