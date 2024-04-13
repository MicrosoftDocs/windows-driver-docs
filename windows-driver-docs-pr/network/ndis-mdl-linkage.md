---
title: NDIS_MDL_LINKAGE macro
ms.topic: reference
description: The NDIS_MDL_LINKAGE macro retrieves a pointer to the next MDL that is associated with the specified MDL.
ms.date: 03/02/2023
keywords:
 - NDIS_MDL_LINKAGE macro Network Drivers Starting with Windows Vista
---

# NDIS\_MDL\_LINKAGE macro


The **NDIS\_MDL\_LINKAGE** macro retrieves a pointer to the next MDL that is associated with the specified MDL.

## Syntax

```ManagedCPlusPlus
PVOID NDIS_MDL_LINKAGE(
   PMDL _Mdl
);
```

## Parameters

*\_Mdl*   
A pointer to an MDL.

## Return value

**NDIS\_MDL\_LINKAGE** returns a pointer to an MDL or **NULL** if there is no next MDL.

## Remarks

The **NDIS\_MDL\_LINKAGE** macro provides an MDL-based version of the [**NDIS\_BUFFER\_LINKAGE**](/previous-versions/windows/hardware/network/ff556919(v=vs.85)) function.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
<tr class="even">
<td><p>IRQL</p></td>
<td><p>Any level</p></td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_BUFFER\_LINKAGE**](/previous-versions/windows/hardware/network/ff556919(v=vs.85))

 

