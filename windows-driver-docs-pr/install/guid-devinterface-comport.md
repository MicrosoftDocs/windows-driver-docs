---
title: GUID\_DEVINTERFACE\_COMPORT
description: GUID\_DEVINTERFACE\_COMPORT
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
---

# GUID\_DEVINTERFACE\_COMPORT


The GUID\_DEVINTERFACE\_COMPORT [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [COM ports](https://msdn.microsoft.com/library/windows/hardware/ff546485).

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

[**GUID\_CLASS\_COMPORT**](guid-class-comport.md) is an obsolete identifier for this device interface class; for new instances of this class, use GUID\_DEVINTERFACE\_COMPORT instead.

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


[**GUID\_CLASS\_COMPORT**](guid-class-comport.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_DEVINTERFACE_COMPORT%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





