---
title: BUS1394\_CLASS\_GUID
description: BUS1394\_CLASS\_GUID
ms.assetid: 5452c829-b1d2-4a15-93ef-3d82ac6c04d0
keywords: ["BUS1394_CLASS_GUID Device and Driver Installation"]
topic_type:
- apiref
api_name:
- BUS1394_CLASS_GUID
api_location:
- 1394.h
api_type:
- HeaderDef
---

# BUS1394\_CLASS\_GUID


The BUS1394\_CLASS\_GUID [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [1394 bus devices](https://msdn.microsoft.com/library/windows/hardware/ff537209).

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
<td align="left"><p>BUS1394_CLASS_GUID</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{6BDD1FC1-810F-11d0-BEC7-08002BE2092F}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Bus drivers for 1394 buses register instances of this device interface class to notify the operating system and applications of the presence of 1394 bus devices.

For information about 1394 buses, see [1394 bus devices](https://msdn.microsoft.com/library/windows/hardware/ff537209).

The WDK samples include the [1394api sample](https://msdn.microsoft.com/library/windows/hardware/ff536887) application. This application uses BUS1394\_CLASS\_GUID to register to be notified of the presence of instances of this device interface class.

For information about the device interface class for IEEE 1394 devices in the 61883 [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509) that support the IEC-61883 protocol, see [**GUID\_61883\_CLASS**](guid-61883-class.md).

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
<td align="left"><p>Available in Windows XP and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">1394.h (include 1394.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID\_61883\_CLASS**](guid-61883-class.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20BUS1394_CLASS_GUID%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





