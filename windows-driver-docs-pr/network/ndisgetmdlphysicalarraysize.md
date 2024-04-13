---
title: NdisGetMdlPhysicalArraySize macro
description: The NdisGetMdlPhysicalArraySize macro retrieves the number of disconnected physical memory blocks that are associated with an MDL.
ms.date: 07/18/2017
keywords:
 - NdisGetMdlPhysicalArraySize macro Network Drivers Starting with Windows Vista
---

# NdisGetMdlPhysicalArraySize macro


The **NdisGetMdlPhysicalArraySize** macro retrieves the number of disconnected physical memory blocks that are associated with an MDL.

## Syntax

```ManagedCPlusPlus
VOID NdisGetMdlPhysicalArraySize(
    _Mdl,
    _ArraySize
);
```

## Parameters

*\_Mdl*   
A pointer to an MDL.

*\_ArraySize*   
A pointer to a caller-supplied variable in which this macro returns the number of disconnected physical memory blocks that are associated with the specified MDL.

## Return value

None

## Remarks

The **NdisGetMdlPhysicalArraySize** macro provides an MDL-based version of the [**NdisGetBufferPhysicalArraySize**](/previous-versions/windows/hardware/network/ff552033(v=vs.85)) function.

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
<td><p>&lt;= DISPATCH_LEVEL</p></td>
</tr>
<tr class="odd">
<td><p>DDI compliance rules</p></td>
<td><a href="/windows-hardware/drivers/devtest/ndis-irql-netbuffer-function" data-raw-source="[&lt;strong&gt;Irql_NetBuffer_Function&lt;/strong&gt;](../devtest/ndis-irql-netbuffer-function.md)"><strong>Irql_NetBuffer_Function</strong></a></td>
</tr>
</tbody>
</table>

## See also


[**NdisGetBufferPhysicalArraySize**](/previous-versions/windows/hardware/network/ff552033(v=vs.85))

