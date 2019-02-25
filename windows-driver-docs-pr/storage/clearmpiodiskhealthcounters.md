---
title: ClearMpioDiskHealthCounters function
description: The ClearMpioDiskHealthCounters method is used to clear the gathered MPIO statistics of an MPIO disk.
ms.assetid: 1ac415b2-87d4-430d-8713-a871c6af1006
keywords: ["ClearMpioDiskHealthCounters function Storage Devices"]
topic_type:
- apiref
api_name:
- ClearMpioDiskHealthCounters
api_location:
- MPIOwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ClearMpioDiskHealthCounters function


The ClearMpioDiskHealthCounters method is used to clear the gathered MPIO statistics of an MPIO disk.

Syntax
------

```ManagedCPlusPlus
void ClearMpioDiskHealthCounters(
   [in, Description("MPIO Disk Ordinal"):amended] uint32 DiskOrdinal
);
```

Parameters
----------

*DiskOrdinal*   
A 32-bitfield that represents the MPIO disk ordinal value.

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

 

 





