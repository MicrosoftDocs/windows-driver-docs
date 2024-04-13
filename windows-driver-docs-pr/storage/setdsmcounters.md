---
title: SetDSMCounters Function
description: The SetDSMCounters method is used to set the timer counters for a particular DSM.
keywords: ["SetDSMCounters function Storage Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- SetDSMCounters
api_location:
- MPIOwmi.h
api_type:
- HeaderDef
ms.date: 10/17/2018
---

# SetDSMCounters function


The SetDSMCounters method is used to set the timer counters for a particular DSM.

## Syntax

```ManagedCPlusPlus
void SetDSMCounters(
   [in, Description("DSM Context"):amended] uint64              DSMcontext,
   [in, Description("DSM Timer Counters"):amended] DSM_COUNTERS DsmCounters
);
```

## Parameters

*DSMcontext*   
A 64-bitfield that provides the DSM context.

*DsmCounters*   
A DSM\_COUNTERS structure.

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

 

 





