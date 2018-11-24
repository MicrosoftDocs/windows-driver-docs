---
title: MPIOMoveDevice function
description: The MPIOMoveDevice method is used to set the active path on the device.
ms.assetid: aa3da461-ea55-4f60-b957-eb6b6cc3aeec
keywords: ["MPIOMoveDevice function Storage Devices"]
topic_type:
- apiref
api_name:
- MPIOMoveDevice
api_location:
- MPIOwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MPIOMoveDevice function


The MPIOMoveDevice method is used to set the active path on the device.

Syntax
------

```ManagedCPlusPlus
void MPIOMoveDevice(
   [in, Description("MPIO Disk Ordinal"):amended] uint32    DiskOrdinal,
   [in, Description("Move Flags."):amended] uint32          Flags,
   [in, Description("PathID to set Active"):amended] uint64 PathID
);
```

Parameters
----------

*DiskOrdinal*   
A 32-bitfield that specifies the MPIO disk ordinal value.

*Flags*   
A 32-bitfield that specifies the flags that are associated with the device move.

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

 

 





