---
title: BUS1394_CLASS_GUID
description: BUS1394_CLASS_GUID
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
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# BUS1394_CLASS_GUID


The BUS1394_CLASS_GUID [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [1394 bus devices](https://msdn.microsoft.com/library/windows/hardware/ff537209).

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

The WDK samples include the [1394api sample](https://msdn.microsoft.com/library/windows/hardware/ff536887) application. This application uses BUS1394_CLASS_GUID to register to be notified of the presence of instances of this device interface class.

For information about the device interface class for IEEE 1394 devices in the 61883 [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509) that support the IEC-61883 protocol, see [**GUID_61883_CLASS**](guid-61883-class.md).

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


[**GUID_61883_CLASS**](guid-61883-class.md)

 

 






