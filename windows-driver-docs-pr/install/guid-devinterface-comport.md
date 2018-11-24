---
title: GUID_DEVINTERFACE_COMPORT
description: GUID_DEVINTERFACE_COMPORT
ms.assetid: ce7fbe64-1445-4702-898e-2fc92f96ebf9
keywords: ["GUID_DEVINTERFACE_COMPORT Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_COMPORT
api_location:
- Ntddser.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_COMPORT


The GUID_DEVINTERFACE_COMPORT [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [COM ports](https://msdn.microsoft.com/library/windows/hardware/ff546485).

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
<td align="left"><p>GUID_DEVINTERFACE_COMPORT</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{86E0D1E0-8089-11D0-9CE4-08003E301F73}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for serial ports register instances of this device interface class to notify the operating system and applications of the presence of COM ports.

The system-supplied function driver for serial ports registers an instance of this device interface class for a [serial port](https://msdn.microsoft.com/library/windows/hardware/ff547451).

The following samples (on Github) register an instance of this class for a serial port:

-   [The Serial sample](http://go.microsoft.com/fwlink/p/?LinkId=617962)
-   [The Virtual serial driver sample](http://go.microsoft.com/fwlink/p/?LinkId=617963) (UMDF 1.0)
-   [The Virtual serial2 driver sample](http://go.microsoft.com/fwlink/p/?LinkId=722209) (KMDF)

[**GUID_CLASS_COMPORT**](guid-class-comport.md) is an obsolete identifier for this device interface class; for new instances of this class, use GUID_DEVINTERFACE_COMPORT instead.

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
<td align="left">Ntddser.h (include Ntddser.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_CLASS_COMPORT**](guid-class-comport.md)

 

 






