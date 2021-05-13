---
title: NdisQueryMdlOffset macro
description: The NdisQueryMdlOffset macro retrieves the offset within a physical page at which a given MDL buffer begins and the length of the buffer.
ms.date: 07/18/2017
keywords:
 - NdisQueryMdlOffset macro Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NdisQueryMdlOffset macro


The **NdisQueryMdlOffset** macro retrieves the offset within a physical page at which a given MDL buffer begins and the length of the buffer.

## Syntax

```ManagedCPlusPlus
VOID NdisQueryMdlOffset(
    _Mdl,
    _Offset,
    _Length
);
```

## Parameters

*\_Mdl*   
A pointer to an MDL.

*\_Offset*   
A pointer to a caller-supplied variable in which this macro returns the zero-based byte offset within the physical page that contains the MDL-specified buffer.

*\_Length*   
A pointer to a caller-supplied variable in which this macro returns the length, in bytes, of the virtual address range that is specified by the MDL.

## Return value

None

## Remarks

The **NdisQueryMdlOffset** macro provides an MDL-based version of the [**NdisQueryBufferOffset**](/previous-versions/windows/hardware/network/ff554411(v=vs.85)) function.

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


[**NdisQueryBufferOffset**](/previous-versions/windows/hardware/network/ff554411(v=vs.85))

