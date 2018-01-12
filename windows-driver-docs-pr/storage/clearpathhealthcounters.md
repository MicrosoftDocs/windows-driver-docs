---
title: ClearPathHealthCounters function
description: The ClearPathHealthCounters method is used to clear all gathered MPIO health statistics for a particular path of an MPIO disk.
ms.assetid: 97f110c9-50c4-4570-ad5e-d1d17b711c6a
keywords: ["ClearPathHealthCounters function Storage Devices"]
topic_type:
- apiref
api_name:
- ClearPathHealthCounters
api_location:
- MPIOwmi.h
api_type:
- HeaderDef
---

# ClearPathHealthCounters function


The ClearPathHealthCounters method is used to clear all gathered MPIO health statistics for a particular path of an MPIO disk.

Syntax
------

```ManagedCPlusPlus
void ClearPathHealthCounters(
   [in, Description("64-bit Path Identifier"):amended] uint64 PathID
);
```

Parameters
----------

*PathID*   
A 64-bitfield that specifies the path that is associated with the device.

Return value
------------

None

Remarks
-------

This WMI method belongs to the MPIO\_WMI\_METHODS WMI class.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">MPIOwmi.h (include MPIOwmi.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20ClearPathHealthCounters%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




