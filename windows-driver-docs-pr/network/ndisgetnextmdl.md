---
title: NdisGetNextMdl macro
description: The NdisGetNextMdl macro retrieves the next MDL in an MDL chain, given a pointer to the current MDL.
ms.assetid: 5b59ca7c-0998-4d53-9553-4946ef85327c
ms.date: 07/18/2017
keywords:
 - NdisGetNextMdl macro Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NdisGetNextMdl macro


The **NdisGetNextMdl** macro retrieves the next MDL in an MDL chain, given a pointer to the current MDL.

Syntax
------

```ManagedCPlusPlus
VOID NdisGetNextMdl(
    _CurrentMdl,
    _NextMdl
);
```

Parameters
----------

*\_CurrentMdl*   
A pointer to the specified current MDL.

*\_NextMdl*   
A pointer to a caller-supplied variable in which this macro returns a pointer to the next MDL in the MDL chain, if any, that follows the MDL at *\_CurrentMdl* .

Return value
------------

None

Remarks
-------

The **NdisGetNextMdl** macro provides an MDL-based version of the [**NdisGetNextBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff552070) function.

Requirements
------------

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


[**NdisGetNextBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff552070)

 

 




