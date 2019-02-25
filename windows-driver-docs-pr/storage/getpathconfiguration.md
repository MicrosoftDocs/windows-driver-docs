---
title: GetPathConfiguration function
description: The GetPathConfiguration method is used to retrieve the device information for each path.
ms.assetid: 1661746f-5a5a-48af-b876-c57f19de4923
keywords: ["GetPathConfiguration function Storage Devices"]
topic_type:
- apiref
api_name:
- GetPathConfiguration
api_location:
- MPIOwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GetPathConfiguration function


The GetPathConfiguration method is used to retrieve the device information for each path.

Syntax
------

```ManagedCPlusPlus
void GetPathConfiguration(
   [in, Description("64-bit Path Identifier"):amended] uint64 PathID,
   [out] uint32                                               EntryCount,
   [out, WmiSizeIs("EntryCount")] SCSI_ADDR                   Address[]
);
```

Parameters
----------

*PathID*   
A 64-bitfield that specifies the path that is associated with the device.

*EntryCount*   
A 32-bitfield that indicates the number of entries that the output contains.

*Address\[\]*   
An array that contains as many SCSI\_ADDR structures as specified by the *EntryCount* parameter.

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

 

 





