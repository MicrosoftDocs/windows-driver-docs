---
title: ClearPathHealthCounters function
description: The ClearPathHealthCounters method is used to clear all gathered MPIO health statistics for a particular path of an MPIO disk.
keywords: ["ClearPathHealthCounters function Storage Devices"]
topic_type:
- apiref
api_name:
- ClearPathHealthCounters
api_location:
- MPIOwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ClearPathHealthCounters function


The ClearPathHealthCounters method is used to clear all gathered MPIO health statistics for a particular path of an MPIO disk.

## Syntax

```ManagedCPlusPlus
void ClearPathHealthCounters(
   [in, Description("64-bit Path Identifier"):amended] uint64 PathID
);
```

## Parameters

*PathID*   
A 64-bitfield that specifies the path that is associated with the device.

## Return value

None

## Remarks

This WMI method belongs to the MPIO\_WMI\_METHODS WMI class.

## Requirements

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

 

 





